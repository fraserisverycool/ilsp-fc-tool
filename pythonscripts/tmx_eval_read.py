#This script takes an evaluation file generated from tmx_eval.py and assigns a score, as well as generating a new TMX file without the TUs labeled with something

from lxml import etree
import sys
import os

if len(sys.argv) < 2:
	print("do it like this: python tmx_eval_read.py \"path to annotated file\"")
	sys.exit()

filename = sys.argv[1]

with open(filename) as f:
	data = f.readlines()


#Read the evaluation file and save new labels to a dictionary

label_dict = {}
index = 0
result = []

line_number = 9
while True:
	if "~END~" in data[line_number]:
		break
	if "#" == data[line_number][0]:
		result.append(data[line_number][2:-1])
		label_dict[index] = result
	if "~~~>>>" in data[line_number]:
		result = []
		index = int(data[line_number][6:])
		label_dict[index] = ""
		line_number += 2
	line_number += 1

print(label_dict)


#Calculate points!

point_system = {"A": 3, "L": 3, "U": 1, "M": 5, "Incorrect Alignment": 3, "Lexical Error": 3, "Poor Usage of Target Language": 1, "Machine Translated Content": 5} 
score = 0
for key, value in label_dict.items():
	for problem in value:
		score += point_system[problem]
print(score)


#Open the original file, find out which languages it's in
original_file = data[0][6:-1]
with open(original_file) as g:
	original_data = g.read()
root = etree.fromstring(original_data)
newroot = etree.Element("tmx", version="1.4b")
body = etree.SubElement(newroot, "body")

headprops = root.find("header").findall(".//prop")
for headprop in headprops:
	if headprop.get("type") == "l1" and headprop.text is not None:
		L1 = headprop.text
	if headprop.get("type") == "l2" and headprop.text is not None:
		L2 = headprop.text


#Edit the original file, removing the labeled TUs

TUcount, L1words, L2words = 0, 0, 0
L1unique, L2unique = set(), set()
new_index = 0
for tu in root.findall(".//tu"):
	new_index += 1
	segs = tu.findall(".//seg")
	check1 = 1
	if new_index in label_dict and len(label_dict[new_index]) > 0: #if it is labeled with something
		check1 = 0
	if check1 == 1:
		TUcount += 1
		body.append(tu)
		for word in segs[0].text.split():
			L1unique.add(word.lower())
		for word in segs[1].text.split():
			L2unique.add(word.lower())
		L1words += len(segs[0].text.split())
		L2words += len(segs[1].text.split())


#Save the original file to a new tmx file

tree = etree.ElementTree(newroot)
tree.write("tmp.tmx", encoding="UTF-8", pretty_print=True)
with open("tmp.tmx") as f:
	middata = f.read()
middata = middata[29:-22]
newfilename = filename[:-4] + "_clean.tmx"
with open(newfilename, "w") as f:
	f.write("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>\n<tmx version=\"1.4b\">\n    <header adminlang=\"en\" creationdate=\"2016-06-02T12:02:06+02:00\" creationtool=\"mALIGNa\" creationtoolversion=\"2\" datatype=\"plaintext\" o-tmf=\"al\" segtype=\"block\" srclang=\"de\">\n        <prop type=\"distributor\">ELRC project</prop>\n        <prop type=\"description\">Acquisition of bilingual data (from multilingual websites), normalization, cleaning, deduplication and identification of parallel documents have been done by ILSP-FC tool. Maligna aligner was used for alignment of segments. Merging/filtering of segment pairs has also been applied.</prop>\n        <prop type=\"availability\">unknown</prop>\n        <prop type=\"l1\">")
	f.write(L1)
	f.write("</prop>\n        <prop type=\"l2\">")
	f.write(L2)
	f.write("</prop>\n        <prop type=\"lengthInTUs\">")
	f.write(str(TUcount))
	f.write("</prop>\n        <prop type=\"# of words in l1\">")
	f.write(str(L1words))
	f.write("</prop>\n        <prop type=\"# of words in l2\">")
	f.write(str(L2words))
	f.write("</prop>\n        <prop type=\"# of unique words in l1\">")
	f.write(str(len(L1unique)))
	f.write("</prop>\n        <prop type=\"# of unique words in l2\">")
	f.write(str(len(L2unique)))
	f.write("</prop>\n    </header>\n	<body>\n        ")
	f.write(middata)
	f.write(">\n    </body>\n</tmx>")
os.remove("tmp.tmx")

print("saved tmx!")


#Save an updated metadata file

with open(filename[:-9] + ".md.xml") as f:
	sample = f.read()
opener = sample[:55]

meta = etree.parse(filename[:-9] + ".md.xml")
metaroot = meta.getroot()
title = metaroot[0][0]
title.text = "Combined TMX " + L1 + "-" + L2
description = metaroot[0][1]
description.text = "Parallel (" + L1 + "-" + L2 + ") corpus of " + str(TUcount) + " translation units."
organisation_name = metaroot[2][0][0][0]
organisation_name.text = "DFKI"
organisation_url = metaroot[2][0][0][1][0]
organisation_url.text = "http://www.dfki.de/"
lang1 = metaroot[3][0][1][0][2][0]
lang1.text = L1
l1words = metaroot[3][0][1][0][2][1][0]
l1words.text = str(L1words)
l1unique = metaroot[3][0][1][0][2][2][0]
l1unique.text = str(len(L1unique))
lang2 = metaroot[3][0][1][0][3][0]
lang2.text = L2
l2words = metaroot[3][0][1][0][3][1][0]
l2words.text = str(L2words)
l2unique = metaroot[3][0][1][0][3][2][0]
l2unique.text = str(len(L2unique))
tunits = metaroot[3][0][1][0][4][0]
tunits.text = str(TUcount)

midmetafilename = "tmpmeta.xml"
meta.write(midmetafilename, encoding="UTF-8", pretty_print=True)
with open(midmetafilename) as f:
	midmeta = f.read()
with open(filename[:-4] + "_clean.md.xml", "w") as f:
	f.write(opener + "\n" + midmeta)
os.remove("tmpmeta.xml")
