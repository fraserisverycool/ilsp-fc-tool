#This is used by webcrawl.py to tmxmerge several websites at once

import sys
import os
import re

basename = sys.argv[1]
final_list = []
list_of_files = os.listdir("bladeresults/" + basename)
new_list_of_files = []
p = re.compile(".*txt")
for thing in list_of_files:
	if p.match(thing) != None:
		new_list_of_files.append(thing)

for thing in new_list_of_files:
	with open("bladeresults/" + basename + "/" + thing) as f:
		data = f.readlines()
	if len(data) > 11:
		interestingline = data[0]
		directory = interestingline.split("xml")[0] + "xml"
		final_list.append(directory)

with open("bladeresults/" + basename + "/" + basename + "_tmx", "w") as f:
	for thing in final_list:
		f.write(thing + "\n")
