#I just use this when I have a long list of seed websites, I always put the same one in twice

import sys

if len(sys.argv) > 1:
	filename = sys.argv[1]
else:
	print("It should be like this: python duplicate_checker.py <filename>")
	sys.exit()

with open(filename) as f:
	data = f.readlines()

dup_list = set()

for thing in data:
	if thing in dup_list:
		print("Duplicate found! " + thing)
	dup_list.add(thing)
	
