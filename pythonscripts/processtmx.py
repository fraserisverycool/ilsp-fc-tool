#Python script to cut down a tmx into only websites accepted from a seed list
#This exists because the crawler sometimes picks up TUs from websites not from the seed list
#It also prints lots of useful information about how many TUs are found in each website
#The system checks the corpora/basename/ directory for the tmx file you specify in the command line argument 

import os
import sys
import re
import glob
from lxml import etree

if len(sys.argv) < 2:
	print("Like this: python websiterank.py \"name of tmx file\"")
	sys.exit()

tmxname = sys.argv[1]
m = re.search("(.*)_A_", tmxname)
if m:
	basename = m.groups()[0]
else:
	print("There's a problem with the tmx file you specified!")
	sys.exit()
print("Checking " + basename + " with the tmx: " + tmxname + ".")
extraseeds = False
if os.path.isfile("seeds/" + basename + "_extra.txt"):
	print("Also including the extra seeds you specified!")
	extraseeds = True

class Website():

	def __init__(self, i, u, s, l, sd):
		self.index = i
		self.url = u
		self.score = s
		self.license = l
		self.seed = sd
		self.ratings = []
		self.variance = 0
		self.mean = 0

	def __str__(self):
		if self.license != "":
			message = "Website number " + str(self.index) + " has a score of " + str(self.score) + ". The URL is " + self.url + ". And bonus! License: " + self.license
		else:
			message = "Website number " + str(self.index) + " has a score of " + str(self.score) + ". The URL is " + self.url
		return message

	def change_score(self, s):
		self.score = s

	def up_score(self, s):
		self.score += s

	def set_license(self, l):
		self.license = l

#sorting out the seed files
def get_seeds():
	with open("seeds/" + basename + ".txt") as f:
		old_seeds = [x.strip() for x in f.readlines()]
	if extraseeds:
		with open("seeds/" + basename + "_extra.txt") as f:
			new_seeds = [x.strip() for x in f.readlines()]
		old_seeds = old_seeds + new_seeds	
	list_of_seeds = []
	for seed in old_seeds:
		if seed.endswith("/"):
			list_of_seeds.append(seed[0:-1])
		else:
			list_of_seeds.append(seed)	
	return list_of_seeds

#my regex didn't work so I'm doing this nonsense, forgive me
#takes a url and returns just the domain, like "berlin.de"
def find_domain(s):
	number_of_slashes = 0
	domain = ""
	for char in s:		
		if number_of_slashes == 2:
			domain = domain + char
		if number_of_slashes > 2:
			break
		if char == "/":
			number_of_slashes += 1
	number_of_dots = 0
	dot_threshold = 2
	domainagain = ""
	double_dots = False
	if ".co.uk" in s or ".gv.at" in s:
		double_dots = True
	for char in domain[::-1]:
		if double_dots:
			dot_threshold = 3		#because of .co.uk!!
		if char == ".":
			number_of_dots += 1
		if number_of_dots < dot_threshold:
			domainagain = domainagain + char
		if number_of_dots == dot_threshold:
			break
	domain = domainagain[::-1]
	if len(domain) == 0:
		domain = "ERROR.com"
	elif domain[-1] == "/":
		domain = domain[:-1]
	return domain

#feeds input into find_domain function, splits up multiple seeds
def find_url(s):
	multidomain = ""
	if ";" in s:
		for part in s.split(";"):
			multidomain = multidomain + find_domain(part) + ";"
		multidomain == multidomain[:-1]
	else:
		multidomain = find_domain(s)
	return multidomain

#check to see if a url is already in the list of websites
def find_site_index_in_list(test):
	for index in range(len(list_of_sites)):
		if test in list_of_sites[index].url:
			return index
	return -1

seeds = get_seeds()

#calculate scores from tmx
with open("corpora/" + basename + "/" + tmxname) as f:
	data = f.read()
root = etree.fromstring(data)

list_of_tus = root.findall(".//tu")
list_of_sites = []

#instantiate website for all the seeds first
for index in range(len(seeds)):
	list_of_sites.append(Website(index, find_url(seeds[index]), 0, "", True))

#calculate the scores for all the websites, and instantiate all the other detected websites too
for tu in list_of_tus:
	props = tu.findall(".//prop")
	list_of_tu_sites = []
	license = ""
	for prop in props:
		tag = prop.get("type")
		value = prop.text	
		if tag == "l1-url":
			list_of_tu_sites.append(find_url(value))
		if tag == "l2-url":
			list_of_tu_sites.append(find_url(value))
		if tag == "license":
			if value != None:
				license = value
	site_index = find_site_index_in_list(list_of_tu_sites[0])		#decided to just look at the first url
	if site_index != -1:											#if this tu is already in the website list
		list_of_sites[site_index].up_score(1)
		if license != "":
			list_of_sites[site_index].set_license(license)
	else:
		list_of_sites.append(Website(-1, list_of_tu_sites[0], 1, license, False))
	
#sort the list into websites with most TUs first
list_of_sites.sort(key=lambda x: x.score, reverse=True)

#create new etree - generate new file!
newroot = etree.Element("tmx", version="1.4b")
body = etree.SubElement(newroot, "body")

oldcount, newcount, newL1, newL2 = 0, 0, 0, 0
L1words, L2words = set(), set()
language1, language2, originaltus = "", "", ""
headprops = root.find("header").findall(".//prop")
for headprop in headprops:
	if headprop.get("type") == "l1":
		language1 = headprop.text
	if headprop.get("type") == "l2":
		language2 = headprop.text
	if headprop.get("type") == "lengthInTUs":
		originaltus = headprop.text

#loop through all the TUs in the original etree and add relevant TUs to the new one
for tu in root.findall(".//tu"):
	oldcount += 1
	props = tu.findall(".//prop")
	check1, check2 = 0, 0
	rating, url1, url2 = 0, "", ""
	for prop in props:
		tag = prop.get("type")
		value = prop.text	
		if tag == "score":
			rating = float(value)
		if tag == "l1-url":
			url1 = find_url(value)
		if tag == "l2-url":
			url2 = find_url(value)

	for site in list_of_sites:
		if url1 in site.url and site.seed:
			check1 = 1
		if url2 in site.url and site.seed:
			check2 = 1
	
	if check1 + check2 == 2:

		for site in list_of_sites:
			if url1 in site.url:
				site.ratings.append(rating)
				site.mean += rating

		body.append(tu)	
		newcount += 1
		segs = tu.findall(".//seg")
		for word in segs[0].text.split():
			L1words.add(word.lower())
		for word in segs[1].text.split():
			L2words.add(word.lower())
		newL1 += len(segs[0].text.split())
		newL2 += len(segs[1].text.split())

#convert your completed tree into this ElementTree object, and make an intermediate file
#there must be a better way to do it, but this works!!
tree = etree.ElementTree(newroot)
midfilename = tmxname[:-4] + "_mid.tmx"
tree.write(midfilename, encoding="UTF-8", pretty_print=True)

#save the thing you just printed as a string (no idea how to save it directly to a string, but hey this works too!!)
with open(midfilename) as f:
	middata = f.read()
middata = middata[29:-22]
newfilename = "corpora/" + basename + "/" + tmxname[:-4] + "_reduced.tmx"
with open(newfilename, "w") as f:
	f.write("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>\n<tmx version=\"1.4b\">\n    <header adminlang=\"en\" creationdate=\"2016-06-02T12:02:06+02:00\" creationtool=\"mALIGNa\" creationtoolversion=\"2\" datatype=\"plaintext\" o-tmf=\"al\" segtype=\"block\" srclang=\"de\">\n        <prop type=\"distributor\">ELRC project</prop>\n        <prop type=\"description\">Acquisition of bilingual data (from multilingual websites), normalization, cleaning, deduplication and identification of parallel documents have been done by ILSP-FC tool. Maligna aligner was used for alignment of segments. Merging/filtering of segment pairs has also been applied.</prop>\n        <prop type=\"availability\">unknown</prop>\n        <prop type=\"l1\">" + language1 + "</prop>\n        <prop type=\"l2\">" + language2 + "</prop>\n        <prop type=\"lengthInTUs\">" + str(newcount) + "</prop>\n        <prop type=\"# of words in l1\">" + str(newL1) + "</prop>\n        <prop type=\"# of words in l2\">" + str(newL2) + "</prop>\n        <prop type=\"# of unique words in l1\">" + str(len(L1words)) + "</prop>\n        <prop type=\"# of unique words in l2\">" + str(len(L2words)) + "</prop>\n    </header>\n	<body>\n        ")
	f.write(middata)
	f.write("u>\n    </body>\n</tmx>")

#save metadata file
with open("corpora/" + basename + "/" + tmxname[:-3] + "md.xml") as f:
	opener = f.read()[:55]

#ugly manual way of making new metadata file - it automatically makes it DFKI - feel free to change it
meta = etree.parse("corpora/" + basename + "/" + tmxname[:-3] + "md.xml")
metaroot = meta.getroot()
description = metaroot[0][1]
description.text = "Parallel (" + language1 + "-" + language2 + ") corpus of " + str(newcount) + " translation units."
organisation_name = metaroot[2][0][0][0]
organisation_name.text = "DFKI"
organisation_url = metaroot[2][0][0][1][0]
organisation_url.text = "http://www.dfki.de/"
l1words = metaroot[3][0][1][0][2][1][0]
l1words.text = str(newL1)
l1unique = metaroot[3][0][1][0][2][2][0]
l1unique.text = str(len(L1words))
l2words = metaroot[3][0][1][0][3][1][0]
l2words.text = str(newL2)
l2unique = metaroot[3][0][1][0][3][2][0]
l2unique.text = str(len(L2words))
tunits = metaroot[3][0][1][0][4][0]
tunits.text = str(newcount)

midmetafilename = tmxname[:-3] + "_mid.md.xml"
meta.write(midmetafilename, encoding="UTF-8", pretty_print=True)
with open(midmetafilename) as f:
	midmeta = f.read()
with open("corpora/" + basename + "/" +  tmxname[:-3] + "_reduced.md.xml", "w") as f:
	f.write(opener + "\n" + midmeta)

#remove that intermediary file. Probably didn't need this
os.remove(midfilename)
os.remove(midmetafilename)

#calculate mean and variance for each site

for site in list_of_sites:
	if site.score > 0:
		site.mean = site.mean/float(site.score)
		summ = 0.0
		for rating in site.ratings:
			summ += (rating - site.mean) * (rating - site.mean)
		site.variance = summ / (site.score - 1)

#print some nice stuff!

newtus = 0
alltus = 0
for site in list_of_sites:
	alltus += site.score
	if site.seed:
		print(site)

#print("site URLs in order:")
#
#for site in list_of_sites:
#	if site.seed:
#		print(site.url)
#
#print("site indexes:")
#
#for site in list_of_sites:
#	if site.seed:	
#		print(site.index)
#
#print("TUs per site:")
#
#for site in list_of_sites:
#	if site.seed:
#		print(site.score)
#		newtus += site.score
#
#print("license?:")
#
#for site in list_of_sites:
#	if site.seed:	
#		print(site.license)
#
#print("means:")
#
#for site in list_of_sites:
#	if site.seed:
#		print(site.mean)
#
#print("variances:")
#
#for site in list_of_sites:
#	if site.seed:
#		print(site.variance)
#
#print("variance/mean ratios:")
#
#for site in list_of_sites:
#	if site.seed:
#		print(site.variance/site.mean)
#
print("Now check out these TUs from other websites which the crawler also found:")
for site in list_of_sites:
	if not site.seed and site.score > 9:
		print(site)

print("Original number of TUs: " + originaltus)

print("Total TUs from seeds: " + str(newtus))

print("Total TUs from unwanted sites: " + str(alltus - newtus))
