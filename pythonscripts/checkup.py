#python script to check the progress on a webcrawl
#in order to run this code you need to modify the ilsp-fc crawler ever so slightly using modifycrawler.py
#it's possibly the worse/most unclear code I've ever written, I'm so sorry
#input example: python pythonscripts/checkup.py de_museums

import glob
import sys
import re

if len(sys.argv) < 2:
	print("Do it like this: python pythonscripts/checkup.py \"basename\"")

basename = sys.argv[1]
logs = glob.glob("logs/" + basename + "/*")

class Sitelog():
	def __init__(self, c, e, a, p):
		self.crawl = c
		self.export = e
		self.align = a
		self.pairdetect = p

	def __str__(self):
		return self.crawl + " - " + self.export + " - " + self.align + " - " + self.pairdetect

tmxmerge = ""
crawls, exports, aligns, pairdetects = [], [], [], []
for log in logs:
	if log.endswith("tmxmerge"):
		tmxmerge = log
	if log.endswith("crawl"):
		crawls.append(log)
	if log.endswith("export"):
		exports.append(log)
	if log.endswith("align"):
		aligns.append(log)
	if log.endswith("pairdetect"):
		pairdetects.append(log)

numberofsites = len(crawls)

listofsites = []
for x in range(numberofsites):
	listofsites.append(Sitelog(basename + "_" + str(x) + "_crawl",basename + "_" + str(x) + "_export",basename + "_" + str(x) + "_align",basename + "_" + str(x) + "_pairdetect"))

print("This is a report about the progress of " + basename)

counter = 0
currenthour = 0
num_of_days = 0
for site in listofsites:
	print("***********************************")
	try:
		with open("logs/" + basename + "/" + site.crawl) as f:
			data = f.readlines()
	except IOError:
		print("That's as far as we've got! Stay patient! Still pairdetecting the previous site")
		break
	starttime = data[0][6:14]
	newhour = int(starttime[:2])
	if newhour < currenthour:
		print("Dawn of a new day!")
		num_of_days += 1
	currenthour = newhour
	print("Website " + str(counter) + " crawl - " + starttime + " - START")
	dontprinttoomuch = 0
	for line in data:
		if "Iteration" in line:
			if (dontprinttoomuch + 1) % 5 == 0:
				print("Website " + str(counter) + " crawl - " + line[6:-18])
				newhour = int(line[6:8])
				if newhour < currenthour:
					print("Dawn of a new day!")
					num_of_days += 1
				currenthour = newhour
			dontprinttoomuch += 1
	try:
		with open("logs/" + basename + "/" + site.export) as f:
			expdata = f.readlines()[0][6:14]
		print("Website " + str(counter) + " export - " + expdata)
		newhour = int(expdata[:2])		
		if newhour < currenthour:
			print("Dawn of a new day!")
			num_of_days += 1
		currenthour = newhour
	except IOError:
		print("That's as far as we've got! Stay patient! Still crawling")
		break
	try:
		with open("logs/" + basename + "/" + site.align) as f:
			aligndata = f.readlines()[0][6:14]
		print("Website " + str(counter) + " align - " + aligndata)
		newhour = int(aligndata[:2])
		if newhour < currenthour:
			print("Dawn of a new day!")
			num_of_days += 1
		currenthour = newhour
	except IOError:
		print("That's as far as we've got! Stay patient! Still exporting")
		break
	try:
		with open("logs/" + basename + "/" + site.pairdetect) as f:
			pairdata = f.readlines()
	except IOError:
		print("That's as far as we've got! Stay patient! Still aligning")
		break
	for line in pairdata:
		if "Detection of pairs of parallel" in line:
			print("Website " + str(counter) + " pairdetect - " + line[6:14] + " Language pair: " + line[-43:-36])
			newhour = int(line[6:8])
			if newhour < currenthour:
				print("Dawn of a new day!")
				num_of_days += 1
			currenthour = newhour
	try:
		with open("bladeresults/" + basename + "/" + basename + "_" + str(counter) + ".tmxlist.txt") as f:
			tmxdata = f.readlines()
	except IOError:
		with open("bladeresults/" + basename + "/" + basename + "_" + str(counter) + "_A.tmxlist.txt") as f:
			tmxdata = f.readlines()
	if len(tmxdata) == 11:
		print("Nothing from this site...")
	else:
		tmxdata = tmxdata[:-14]
		score = 0
		for line in tmxdata:
			m = re.search(":: (.*) alignments", line)
			if m:
				score += int(m.groups()[0])
		print(str(score) + " alignments from this website") 
	counter += 1
try:
	with open(tmxmerge) as f:
		mergedata = f.readlines()[0][6:14]
	print("TMX Merge: " + mergedata)
	newhour = int(mergedata[:2])
	if newhour < currenthour:
		print("Dawn of a new day!")
		num_of_days += 1
	currenthour = newhour
except IOError:
	pass

print("This whole thing has taken " + str(num_of_days) + " days!")






