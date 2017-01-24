#this is a program that lets you manually evaluate your corpora. We might use this in the future!

import sys
from lxml import etree
from random import randint

if len(sys.argv) < 2:
	print("do it like this: python tmx_eval.py \"directory\" \"number of tests\"")
	sys.exit()

filename = sys.argv[1]


#Open and read the TMX file we want to evaluate - decide how many TUs to test

with open(filename) as f:
    data = f.read()
root = etree.fromstring(data)
allTUs = root.findall(".//tu")
numOfTUs = len(allTUs)
print(numOfTUs)
numOfTests = numOfTUs * 3/100
if len(sys.argv) > 2:
    numOfTests = int(sys.argv[2])
sometus = {}


#Pick out the random TUs and add them to an indexed dictionary

for index in range(0, numOfTests):
    realindex = randint(0, numOfTUs)
    sometus[realindex] = allTUs[realindex]


#Write the text file used for evaluating

with open(filename[:-4] + "_eval.txt", "w") as f:
	f.write("File: " + filename + "\n\n")
	f.write("Here are " + str(numOfTests) + " Translation Units. Please write in the line below each pair what the issue is, if there is one.\nUse a \"#\" symbol followed by one of the following issues:\n - A: Incorrect Alignment\n - L: Lexical Errors\n - U: Poor Usage of Target Language\n - M: Machine Translated Content\n\n")
	for ind, tu in sometus.items():
		segments = tu.findall(".//seg")
		f.write("~~~>>>" + str(ind) + "\n")
		for segment in segments:
			f.write(segment.text.encode('utf-8') + "\n")
		f.write("\n")
	f.write("~END~")


#To read a completed evaluation, use tmx_eval_read.py!
