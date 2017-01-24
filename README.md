# Fraser's tool for the ILSP-FC

Hello and welcome to my python tool to make using the ILSP Focused Crawler easier.

## Set-up

First of all, clone this git page into your favourite directory. Then, download the webcrawler, and extract it into the same directory:

http://nlp.ilsp.gr/redmine/projects/ilsp-fc/files

~~~ Optional ~~~

I like to alter the log files that the crawler creates by adding a single line of code into the crawler before you compile it. It's in ilsp-fc-2.2.3/src/main/java/gr/ilsp/fc/main/Crawl.java at around line 496, depending on which release you're using. At the point where it prints how many pages it has visited at each iteration, I like knowing how many interations we have left. The "checkup.py" tool uses this to how slowly things are running.

`LOGGER.info("Iteration " + curLoop + " out of " + endLoop);`

~~~ No longer optional ~~~

You can compile the crawler by using the following command:

`mvn clean install`

This will create the all important ilsp-fc-2.2.3-jar-with-dependencies.jar file. This file can be found in the ilsp-fc-2.2.3/target directory after building. Move this file into the main directory.

## Preparing a webcrawl

This tool takes as input a list of websites and a language specification, and outputs a merged tmx file of all the aligned pairs from those websites. Key is that you use a consistent basename for your webcrawl. For example, if I want to make a resource from german government websites I would call it "de\_government".

The input "seed website" file should be in the /seeds directory, and should be named, for example, "de\_government.txt". It should have the following format:

```
https://www.bundesregierung.de/
http://www.auswaertiges-amt.de/
http://www.bmi.bund.de/
http://www.bmj.de/
http://www.bundesfinanzministerium.de/
http://www.bmas.de/
http://www.bmwi.de/
http://www.bmel.de/
https://www.bmvg.de
https://www.bmfsfj.de/
http://www.bundesgesundheitsministerium.de/
http://www.bmvbs.de/
http://www.bmub.de/
https://www.bmbf.de/
http://www.bmz.de/
```

The crawler has a "filter" option, which restricts the URLs checked to ones fitting a certain regular expression. This tool generates this filter automatically for each website. For example, for the first three, it will be "bundesregierung.de", "auswaertiges-amt.de" and "bmi.bund.de". There is a danger that despite this filter, unwanted websites will appear, however there is a script that we can use later on to weed out the unwanted websites.

If you have a website in which the filter would not work, you must seperate all the possible URLs it could use with a semicolon. For example, The Saarland tourism website is offered in four languages, each with its own domain:

`https://www.urlaub.saarland/;https://www.visitsaarland.co.uk/;https://www.visiter-la-sarre.fr/;https://www.toerisme-saarland.nl`

## Generating the shell script

There is a python file in the main directory called "webcrawl.py". This will generate the shell script that you use to run the webcrawl. It requires two inputs, your basename, and the languages you're crawling for. Knowing the basename, it will look for the seed file in /seeds, generate directories in /corpora, /logs and /crawldata and prepare the five stages of the crawler. Here is an example of its use:

`python webcrawl.py "de_government" "en;de"`

You can also optionally add a third argument, a number, to specify the number of iterations "n". By default, this is 100, but I recommend boosting it up to 200 if you're just crawling a couple of hefty websites.

`python webcrawl.py "de_government" "en;de" 200`

Although the crawler can be used in one command, this tool runs 4 seperate commands in a loop for each website, crawl, export, pairdetect and align. This is so it can print a statement to the log in between each one. After each "align", it also deletes some of the large files which take up lots of space, but aren't needed for the tmx merge, namely the pdfs and the html files.

The script will be generated in /shellscripts, and might look like "de\_government.sh". I recommend using "screen" to run the crawl, as running several crawls can take days, weeks...

Your final corpus should be in /corpora, all the crawl data in /crawldata, the logs in /logs, the seed files in /seeds and the shellscripts in /shellscripts. One note about crawl data: even though the tool deletes a lot of redundant data, the xml files can still take up a lot of space. I recommend compressing this information and storing it somewhere, so that it is possible to return to it without having to wait for it to crawl again.

## Extra tools

* The coolest tool here is definitely pythonscripts/processtmx.py. It looks at your tmx that you generated, and figures out how many TUs came from each website. It also lists all of the other websites that it picked up, despite the filter. It then created a new tmx file with "\_reduced" added to the filename, which only contains the seed websites. Then, if you so wish, you can put some of those extra seeds into a separate seed file called "seeds/de\_government\_extra.txt", and it will include them in the reduced version.
* checkup.py takes a look at the log files for you, if you're too lazy to see how far along your crawl is. It only works if you made that change to the crawler I mentioned at the beginning. It will tell you which website it's on, and how many takes it's taken so far.
* combinetmx.py is an old file which should still work. It concatenates two tmx files together!
* tmx\_eval.px and tmx\_eval\_read.py. There was talk of getting human evaluators to check the tmx files. This was my test run!
* tmxlist.py is actually used by webcrawl.py, so don't get rid of that! It gathers all the directories of all the crawl data.
* duplicate\_checker.py this is just to check if I didn't put two websites twice in the seed list, happens all the time.
