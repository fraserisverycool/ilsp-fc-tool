#Python script to automatically generate the shell script used for step by step webcrawling
#Example input: python webcrawl.py "de_government" "en;de" 200
#The first argument is the "basename" of the set of crawls
#The second argument is the languages checked
#The third optional argument changes the "n" value - ie how many cycles the crawler uses in each website
#When you're only crawling one big website (like a government website), I like to make this 200, but the default is 100

import sys
import os
import shutil

#command line arguments

if len(sys.argv) < 2:
    print("It should look like this: python webcrawl.py \"de_government\" \"en;de\"")
    sys.exit()

basename = sys.argv[1] #"de_justice" (seed needs to be germantest.txt)
language = sys.argv[2] #"en;de"
filename = basename + ".sh"
nvalue = 100

if len(sys.argv) > 3:
    nvalue = int(sys.argv[3])

#two functions to help generate the relevant "filter" option for each crawl.
#the first one gets rid of the http://www. bit and escapes the "." character

def cut_up(site):
    newsite = ""
    if "http://" in site:
        site = site[7:]
    if "https://" in site:
        site = site[8:]
    if "www" in site:
        site = site[4:] 
    for letter in site:
        if letter == ".":
            newsite = newsite + "\\"
        newsite = newsite + letter
    return newsite.strip()

#the second checks for multiple seed URLs. Some websites like visitsaarland.co.uk need several
#it also adds a generic ".*" to the beginning and end of the regex

def generate_filter(sb):
    with open("seeds/" + basename + "/" + sb + ".txt") as f:
        info = f.readlines()
    if len(info) > 1:
        newstring = ".*("
        for line in info:        #look through each variation of the seed URL
            newstring = newstring + cut_up(line) + "|"
        newstring = newstring[:-1] + ").*"
        return newstring
    elif len(info) == 1:
        return ".*" + cut_up(info[0]) + ".*"
    else:
        print("Uh oh!")
        return ".*"

#You need the seed file in the /seeds directory to run this. This script will split it into several different files for later use

if not os.path.isdir("seeds/" + basename):
    with open("seeds/" + basename + ".txt") as f:
        data = f.readlines()

    os.mkdir("seeds/" + basename)

    for i in range(len(data)):
        newname = basename + "_" + str(i) + ".txt"
        with open("seeds/" + basename + "/" + newname, "w") as g:
            if ";" in data[i]:
                multiseeds = data[i].split(";")
                for multiseed in multiseeds:
                    g.write(multiseed + "\n")
            else:
                g.write(data[i])

numberofseeds = len(os.listdir("seeds/" + basename))

os.mkdir("logs/" + basename)
os.mkdir("corpora/" + basename)

with open("shellscripts/" + filename, "w") as f:
    f.write("#!/bin/bash\n")
    f.write("echo \"Let's get this webcrawl started!!\"\n")
    for i in range(numberofseeds):
        spec_basename = basename + "_" + str(i)
        filterexp = generate_filter(spec_basename)
        f.write("echo \"Starting crawl on Website " + str(i) + " - the time is `date`\"\n")
        f.write("java -Dlog4j.configuration=file:log4j.xml -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -crawl -f -k -a " + spec_basename + " -type p -lang \"" + language + "\" -n " + str(nvalue) + " -t 100 -len 0 -mtlen 40 -dest \"crawldata/" + basename + "\" -u \"seeds/" + basename + "/" + spec_basename + ".txt\" -filter \"" + filterexp + "\" &> logs/" + basename + "/" + spec_basename + "_crawl\n")
        f.write("DIR=$(ls crawldata/" + basename + " | grep " + spec_basename + ")\n")
        f.write("DIR2=$(ls crawldata/" + basename + "/$DIR)\n")
        f.write("echo \"Crawl finished! Now exporting... the time is `date`\"\n")
        f.write("java -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -export -lang \"" + language + "\" -i \"crawldata/" + basename + "/$DIR/$DIR2\" -bs  crawldata/" + basename + "/$DIR/$DIR2/" + basename + " -len 2 -mtlen 5 &> logs/" + basename + "/" + spec_basename + "_export\n")
        f.write("ls -d crawldata/" + basename + "/$DIR/$DIR2/* | grep -P \"/[-\dT]+$\" | xargs rm -r\n")
        f.write("echo \"Now pair detecting... the time is `date`\"\n")
        f.write("java -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -pairdetect -lang \"" + language + "\" -i \"crawldata/" + basename + "/$DIR/$DIR2/xml\" -bs crawldata/" + basename + "/$DIR/$DIR2/" + basename + " -ifp -pdm \"aupdih\" &> logs/" + basename + "/" + spec_basename + "_pairdetect\n")
        f.write("echo \"Now aligning... the time is `date`\"\n")
        f.write("java -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -align -lang \"" + language + "\" -i \"crawldata/" + basename + "/$DIR/$DIR2/xml\" -bs corpora/" + basename + "/" + spec_basename + " &> logs/" + basename + "/" + spec_basename + "_align\n")
        f.write("echo \"Website " + str(i) + " is finished! Now deleting some large binary files... the time is `date`\"\n")
        f.write("if [ -d crawldata/" + basename + "/$DIR/$DIR2/xml ]; then find crawldata/" + basename + "/$DIR/$DIR2/xml -type f -name \"*.html\" | xargs rm; ls -d crawldata/" + basename + "/$DIR/$DIR2/xml/* | grep -P \"/*.pdf$\" | xargs rm; fi\n")
    f.write("echo \"Now for the tmxmerge part...\"\n")
    f.write("python pythonscripts/tmxlist.py \"" + basename + "\"\n")
    f.write("java -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -tmxmerge -lang \"" + language + "\" -i \"corpora/" + basename + "/" + basename + "_tmx\" -oxslt -pdm \"aupdih\" -segtypes \"1:1\" -bs corpora/" + basename + "/" + basename + " -mtuvl 2 -mpa \"0.16\" -minlr \"0.6\" -maxlr \"1.6\" -ksn &> logs/" + basename + "/" + basename + "_tmxmerge\n")
    f.write("echo \"Webcrawl finished! Use websiterank.py to see how your corpus looks. The corpus is in /corpora, the xmls are all in /crawldata (consider archiving them!), and the logs are in /logs.\"\n")
