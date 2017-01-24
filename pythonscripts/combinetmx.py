#script to merge tmx's without the use of the ILSP-FC crawler
#relatively old file, but should still work

import sys
import os
import glob
import time
from lxml import etree

class Corpus():
	def __init__(self, directory, basename):
		"""
		takes one command line argument, a directory with all your tmx files,
		and then reads the files and initiliases some important attributes with raw data
		"""
		start = time.clock()
		self.bn = basename
		self.files = []
		for filename in directory:
			with open(filename) as f:
				self.files.append(f.read())
		if self.files == []:
			print("You typed the name of the folder with the TMX files wrong!")
			sys.exit()
		self.TUs = 0
		self.L1w = 0
		self.L2w = 0
		self.L1u = set()
		self.L2u = set()
		self.L1 = ""
		self.L2 = ""
		end = time.clock()
		print("Initialisation time: " + str(end - start))

	def combine_tmx(self):
		"""turns all the tmxs into etrees"""
		newstart = time.clock()
		newroot = etree.Element("tmx", version="1.4b")
		body = etree.SubElement(newroot, "body")

		for filestring in self.files:
			starttime = time.clock()			
			root = etree.fromstring(filestring)
			TUcount, L1words, L2words = 0, 0, 0
			L1unique, L2unique = set(), set()
			headprops = root.find("header").findall(".//prop")
			for headprop in headprops:
				if headprop.get("type") == "l1" and headprop.text is not None:
					self.L1 = headprop.text
				if headprop.get("type") == "l2" and headprop.text is not None:
					self.L2 = headprop.text
			for tu in root.findall(".//tu"):
				segs = tu.findall(".//seg")
				check1, check2, check3 = 0, 1, 0
				if len(segs) == 2:
					check1 = 1
				if segs[0].text == segs[1].text:
					check2 = 0
				if check1 + check2 == 2:
					TUcount += 1
					body.append(tu)
					for word in segs[0].text.split():
						L1unique.add(word)
					for word in segs[1].text.split():
						L2unique.add(word)
					L1words += len(segs[0].text.split())
					L2words += len(segs[1].text.split())
			self.L1u = self.L1u.union(L1unique)
			self.L2u = self.L2u.union(L2unique)
			self.TUs += TUcount
			self.L1w += L1words
			self.L2w += L2words
			endtime = time.clock()
			print("This TMX has " + str(TUcount) + " TUs, and it took this much time to process: " + str(endtime - starttime))
		
		tree = etree.ElementTree(newroot)
		tree.write("tmp.tmx", encoding="UTF-8", pretty_print=True)
		with open("tmp.tmx") as f:
			middata = f.read()
		middata = middata[29:-22]
		newfilename = self.bn + ".tmx"
		with open(newfilename, "w") as f:
			f.write("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>\n<tmx version=\"1.4b\">\n    <header adminlang=\"en\" creationdate=\"2016-06-02T12:02:06+02:00\" creationtool=\"mALIGNa\" creationtoolversion=\"2\" datatype=\"plaintext\" o-tmf=\"al\" segtype=\"block\" srclang=\"de\">\n        <prop type=\"distributor\">ELRC project</prop>\n        <prop type=\"description\">Acquisition of bilingual data (from multilingual websites), normalization, cleaning, deduplication and identification of parallel documents have been done by ILSP-FC tool. Maligna aligner was used for alignment of segments. Merging/filtering of segment pairs has also been applied.</prop>\n        <prop type=\"availability\">unknown</prop>\n        <prop type=\"l1\">")
			f.write(self.L1)
			f.write("</prop>\n        <prop type=\"l2\">")
			f.write(self.L2)
			f.write("</prop>\n        <prop type=\"lengthInTUs\">")
			f.write(str(self.TUs))
			f.write("</prop>\n        <prop type=\"# of words in l1\">")
			f.write(str(self.L1w))
			f.write("</prop>\n        <prop type=\"# of words in l2\">")
			f.write(str(self.L2w))
			f.write("</prop>\n        <prop type=\"# of unique words in l1\">")
			f.write(str(len(self.L1u)))
			f.write("</prop>\n        <prop type=\"# of unique words in l2\">")
			f.write(str(len(self.L2u)))
			f.write("</prop>\n    </header>\n	<body>\n        ")
			f.write(middata)
			f.write("u>\n    </body>\n</tmx>")
		os.remove("tmp.tmx")			
		
		newend = time.clock()
		print("The combined TMX has " + str(self.TUs) + " TUs, and around " + str(self.L1w) + " words. It took this much time to process: " + str(newend-newstart))

	def make_metadata(self, sample):
		"""use a sample metadata file, copy it and fill it in with good metadata"""
		starttime = time.clock()
		
		opener = sample[:55]

		meta = etree.parse("samplemetadata.xml")
		metaroot = meta.getroot()
		title = metaroot[0][0]
		title.text = "Combined TMX " + self.L1 + "-" + self.L2
		description = metaroot[0][1]
		description.text = "Parallel (" + self.L1 + "-" + self.L2 + ") corpus of " + str(self.TUs) + " translation units."
		organisation_name = metaroot[2][0][0][0]
		organisation_name.text = "DFKI"
		organisation_url = metaroot[2][0][0][1][0]
		organisation_url.text = "http://www.dfki.de/"
		lang1 = metaroot[3][0][1][0][2][0]
		lang1.text = self.L1
		l1words = metaroot[3][0][1][0][2][1][0]
		l1words.text = str(self.L1w)
		l1unique = metaroot[3][0][1][0][2][2][0]
		l1unique.text = str(len(self.L1u))
		lang2 = metaroot[3][0][1][0][3][0]
		lang2.text = self.L2
		l2words = metaroot[3][0][1][0][3][1][0]
		l2words.text = str(self.L2w)
		l2unique = metaroot[3][0][1][0][3][2][0]
		l2unique.text = str(len(self.L2u))
		tunits = metaroot[3][0][1][0][4][0]
		tunits.text = str(self.TUs)

		midmetafilename = "tmpmeta.xml"
		meta.write(midmetafilename, encoding="UTF-8", pretty_print=True)
		with open(midmetafilename) as f:
			midmeta = f.read()
		with open(self.bn + ".md.xml", "w") as f:
			f.write(opener + "\n" + midmeta)
		os.remove("tmpmeta.xml")
		endtime = time.clock()
		print("Metadata created! Time taken: " + str(endtime - starttime))

if len(sys.argv) < 2:
	print("Do it like this: python combinetmx.py <directory of tmx> <preferred path and name of output files>")
	sys.exit()

directory = glob.glob(sys.argv[1] + "/*.tmx")

basename = "combined"
if len(sys.argv) > 2:
	basename = sys.argv[2]

banana = Corpus(directory, basename)
banana.combine_tmx()

with open("samplemetadata.xml") as f:
	sample = f.read()

banana.make_metadata(sample)
