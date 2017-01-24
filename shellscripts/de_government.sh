#!/bin/bash
echo "Let's get this webcrawl started!!"
echo "Starting crawl on Website 0 - the time is `date`"
java -Dlog4j.configuration=file:log4j.xml -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -crawl -f -k -a de_government_0 -type p -lang "en;de" -n 100 -t 100 -len 0 -mtlen 40 -dest "crawldata/de_government" -u "seeds/de_government/de_government_0.txt" -filter ".*bundesregierung\.de/.*" &> logs/de_government/de_government_0_crawl
DIR=$(ls crawldata/de_government | grep de_government_0)
DIR2=$(ls crawldata/de_government/$DIR)
echo "Crawl finished! Now exporting... the time is `date`"
java -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -export -lang "en;de" -i "crawldata/de_government/$DIR/$DIR2" -bs  crawldata/de_government/$DIR/$DIR2/de_government -len 2 -mtlen 5 &> logs/de_government/de_government_0_export
ls -d crawldata/de_government/$DIR/$DIR2/* | grep -P "/[-\dT]+$" | xargs rm -r
echo "Now pair detecting... the time is `date`"
java -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -pairdetect -lang "en;de" -i "crawldata/de_government/$DIR/$DIR2/xml" -bs crawldata/de_government/$DIR/$DIR2/de_government -ifp -pdm "aupdih" &> logs/de_government/de_government_0_pairdetect
echo "Now aligning... the time is `date`"
java -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -align -lang "en;de" -i "crawldata/de_government/$DIR/$DIR2/xml" -bs corpora/de_government/de_government_0 &> logs/de_government/de_government_0_align
echo "Website 0 is finished! Now deleting some large binary files... the time is `date`"
if [ -d crawldata/de_government/$DIR/$DIR2/xml ]; then find crawldata/de_government/$DIR/$DIR2/xml -type f -name "*.html" | xargs rm; ls -d crawldata/de_government/$DIR/$DIR2/xml/* | grep -P "/*.pdf$" | xargs rm; fi
echo "Starting crawl on Website 1 - the time is `date`"
java -Dlog4j.configuration=file:log4j.xml -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -crawl -f -k -a de_government_1 -type p -lang "en;de" -n 100 -t 100 -len 0 -mtlen 40 -dest "crawldata/de_government" -u "seeds/de_government/de_government_1.txt" -filter ".*auswaertiges-amt\.de/.*" &> logs/de_government/de_government_1_crawl
DIR=$(ls crawldata/de_government | grep de_government_1)
DIR2=$(ls crawldata/de_government/$DIR)
echo "Crawl finished! Now exporting... the time is `date`"
java -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -export -lang "en;de" -i "crawldata/de_government/$DIR/$DIR2" -bs  crawldata/de_government/$DIR/$DIR2/de_government -len 2 -mtlen 5 &> logs/de_government/de_government_1_export
ls -d crawldata/de_government/$DIR/$DIR2/* | grep -P "/[-\dT]+$" | xargs rm -r
echo "Now pair detecting... the time is `date`"
java -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -pairdetect -lang "en;de" -i "crawldata/de_government/$DIR/$DIR2/xml" -bs crawldata/de_government/$DIR/$DIR2/de_government -ifp -pdm "aupdih" &> logs/de_government/de_government_1_pairdetect
echo "Now aligning... the time is `date`"
java -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -align -lang "en;de" -i "crawldata/de_government/$DIR/$DIR2/xml" -bs corpora/de_government/de_government_1 &> logs/de_government/de_government_1_align
echo "Website 1 is finished! Now deleting some large binary files... the time is `date`"
if [ -d crawldata/de_government/$DIR/$DIR2/xml ]; then find crawldata/de_government/$DIR/$DIR2/xml -type f -name "*.html" | xargs rm; ls -d crawldata/de_government/$DIR/$DIR2/xml/* | grep -P "/*.pdf$" | xargs rm; fi
echo "Starting crawl on Website 2 - the time is `date`"
java -Dlog4j.configuration=file:log4j.xml -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -crawl -f -k -a de_government_2 -type p -lang "en;de" -n 100 -t 100 -len 0 -mtlen 40 -dest "crawldata/de_government" -u "seeds/de_government/de_government_2.txt" -filter ".*bmi\.bund\.de/.*" &> logs/de_government/de_government_2_crawl
DIR=$(ls crawldata/de_government | grep de_government_2)
DIR2=$(ls crawldata/de_government/$DIR)
echo "Crawl finished! Now exporting... the time is `date`"
java -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -export -lang "en;de" -i "crawldata/de_government/$DIR/$DIR2" -bs  crawldata/de_government/$DIR/$DIR2/de_government -len 2 -mtlen 5 &> logs/de_government/de_government_2_export
ls -d crawldata/de_government/$DIR/$DIR2/* | grep -P "/[-\dT]+$" | xargs rm -r
echo "Now pair detecting... the time is `date`"
java -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -pairdetect -lang "en;de" -i "crawldata/de_government/$DIR/$DIR2/xml" -bs crawldata/de_government/$DIR/$DIR2/de_government -ifp -pdm "aupdih" &> logs/de_government/de_government_2_pairdetect
echo "Now aligning... the time is `date`"
java -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -align -lang "en;de" -i "crawldata/de_government/$DIR/$DIR2/xml" -bs corpora/de_government/de_government_2 &> logs/de_government/de_government_2_align
echo "Website 2 is finished! Now deleting some large binary files... the time is `date`"
if [ -d crawldata/de_government/$DIR/$DIR2/xml ]; then find crawldata/de_government/$DIR/$DIR2/xml -type f -name "*.html" | xargs rm; ls -d crawldata/de_government/$DIR/$DIR2/xml/* | grep -P "/*.pdf$" | xargs rm; fi
echo "Starting crawl on Website 3 - the time is `date`"
java -Dlog4j.configuration=file:log4j.xml -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -crawl -f -k -a de_government_3 -type p -lang "en;de" -n 100 -t 100 -len 0 -mtlen 40 -dest "crawldata/de_government" -u "seeds/de_government/de_government_3.txt" -filter ".*bmj\.de/.*" &> logs/de_government/de_government_3_crawl
DIR=$(ls crawldata/de_government | grep de_government_3)
DIR2=$(ls crawldata/de_government/$DIR)
echo "Crawl finished! Now exporting... the time is `date`"
java -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -export -lang "en;de" -i "crawldata/de_government/$DIR/$DIR2" -bs  crawldata/de_government/$DIR/$DIR2/de_government -len 2 -mtlen 5 &> logs/de_government/de_government_3_export
ls -d crawldata/de_government/$DIR/$DIR2/* | grep -P "/[-\dT]+$" | xargs rm -r
echo "Now pair detecting... the time is `date`"
java -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -pairdetect -lang "en;de" -i "crawldata/de_government/$DIR/$DIR2/xml" -bs crawldata/de_government/$DIR/$DIR2/de_government -ifp -pdm "aupdih" &> logs/de_government/de_government_3_pairdetect
echo "Now aligning... the time is `date`"
java -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -align -lang "en;de" -i "crawldata/de_government/$DIR/$DIR2/xml" -bs corpora/de_government/de_government_3 &> logs/de_government/de_government_3_align
echo "Website 3 is finished! Now deleting some large binary files... the time is `date`"
if [ -d crawldata/de_government/$DIR/$DIR2/xml ]; then find crawldata/de_government/$DIR/$DIR2/xml -type f -name "*.html" | xargs rm; ls -d crawldata/de_government/$DIR/$DIR2/xml/* | grep -P "/*.pdf$" | xargs rm; fi
echo "Starting crawl on Website 4 - the time is `date`"
java -Dlog4j.configuration=file:log4j.xml -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -crawl -f -k -a de_government_4 -type p -lang "en;de" -n 100 -t 100 -len 0 -mtlen 40 -dest "crawldata/de_government" -u "seeds/de_government/de_government_4.txt" -filter ".*bundesfinanzministerium\.de/.*" &> logs/de_government/de_government_4_crawl
DIR=$(ls crawldata/de_government | grep de_government_4)
DIR2=$(ls crawldata/de_government/$DIR)
echo "Crawl finished! Now exporting... the time is `date`"
java -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -export -lang "en;de" -i "crawldata/de_government/$DIR/$DIR2" -bs  crawldata/de_government/$DIR/$DIR2/de_government -len 2 -mtlen 5 &> logs/de_government/de_government_4_export
ls -d crawldata/de_government/$DIR/$DIR2/* | grep -P "/[-\dT]+$" | xargs rm -r
echo "Now pair detecting... the time is `date`"
java -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -pairdetect -lang "en;de" -i "crawldata/de_government/$DIR/$DIR2/xml" -bs crawldata/de_government/$DIR/$DIR2/de_government -ifp -pdm "aupdih" &> logs/de_government/de_government_4_pairdetect
echo "Now aligning... the time is `date`"
java -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -align -lang "en;de" -i "crawldata/de_government/$DIR/$DIR2/xml" -bs corpora/de_government/de_government_4 &> logs/de_government/de_government_4_align
echo "Website 4 is finished! Now deleting some large binary files... the time is `date`"
if [ -d crawldata/de_government/$DIR/$DIR2/xml ]; then find crawldata/de_government/$DIR/$DIR2/xml -type f -name "*.html" | xargs rm; ls -d crawldata/de_government/$DIR/$DIR2/xml/* | grep -P "/*.pdf$" | xargs rm; fi
echo "Starting crawl on Website 5 - the time is `date`"
java -Dlog4j.configuration=file:log4j.xml -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -crawl -f -k -a de_government_5 -type p -lang "en;de" -n 100 -t 100 -len 0 -mtlen 40 -dest "crawldata/de_government" -u "seeds/de_government/de_government_5.txt" -filter ".*bmas\.de/.*" &> logs/de_government/de_government_5_crawl
DIR=$(ls crawldata/de_government | grep de_government_5)
DIR2=$(ls crawldata/de_government/$DIR)
echo "Crawl finished! Now exporting... the time is `date`"
java -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -export -lang "en;de" -i "crawldata/de_government/$DIR/$DIR2" -bs  crawldata/de_government/$DIR/$DIR2/de_government -len 2 -mtlen 5 &> logs/de_government/de_government_5_export
ls -d crawldata/de_government/$DIR/$DIR2/* | grep -P "/[-\dT]+$" | xargs rm -r
echo "Now pair detecting... the time is `date`"
java -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -pairdetect -lang "en;de" -i "crawldata/de_government/$DIR/$DIR2/xml" -bs crawldata/de_government/$DIR/$DIR2/de_government -ifp -pdm "aupdih" &> logs/de_government/de_government_5_pairdetect
echo "Now aligning... the time is `date`"
java -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -align -lang "en;de" -i "crawldata/de_government/$DIR/$DIR2/xml" -bs corpora/de_government/de_government_5 &> logs/de_government/de_government_5_align
echo "Website 5 is finished! Now deleting some large binary files... the time is `date`"
if [ -d crawldata/de_government/$DIR/$DIR2/xml ]; then find crawldata/de_government/$DIR/$DIR2/xml -type f -name "*.html" | xargs rm; ls -d crawldata/de_government/$DIR/$DIR2/xml/* | grep -P "/*.pdf$" | xargs rm; fi
echo "Starting crawl on Website 6 - the time is `date`"
java -Dlog4j.configuration=file:log4j.xml -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -crawl -f -k -a de_government_6 -type p -lang "en;de" -n 100 -t 100 -len 0 -mtlen 40 -dest "crawldata/de_government" -u "seeds/de_government/de_government_6.txt" -filter ".*bmwi\.de/.*" &> logs/de_government/de_government_6_crawl
DIR=$(ls crawldata/de_government | grep de_government_6)
DIR2=$(ls crawldata/de_government/$DIR)
echo "Crawl finished! Now exporting... the time is `date`"
java -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -export -lang "en;de" -i "crawldata/de_government/$DIR/$DIR2" -bs  crawldata/de_government/$DIR/$DIR2/de_government -len 2 -mtlen 5 &> logs/de_government/de_government_6_export
ls -d crawldata/de_government/$DIR/$DIR2/* | grep -P "/[-\dT]+$" | xargs rm -r
echo "Now pair detecting... the time is `date`"
java -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -pairdetect -lang "en;de" -i "crawldata/de_government/$DIR/$DIR2/xml" -bs crawldata/de_government/$DIR/$DIR2/de_government -ifp -pdm "aupdih" &> logs/de_government/de_government_6_pairdetect
echo "Now aligning... the time is `date`"
java -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -align -lang "en;de" -i "crawldata/de_government/$DIR/$DIR2/xml" -bs corpora/de_government/de_government_6 &> logs/de_government/de_government_6_align
echo "Website 6 is finished! Now deleting some large binary files... the time is `date`"
if [ -d crawldata/de_government/$DIR/$DIR2/xml ]; then find crawldata/de_government/$DIR/$DIR2/xml -type f -name "*.html" | xargs rm; ls -d crawldata/de_government/$DIR/$DIR2/xml/* | grep -P "/*.pdf$" | xargs rm; fi
echo "Starting crawl on Website 7 - the time is `date`"
java -Dlog4j.configuration=file:log4j.xml -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -crawl -f -k -a de_government_7 -type p -lang "en;de" -n 100 -t 100 -len 0 -mtlen 40 -dest "crawldata/de_government" -u "seeds/de_government/de_government_7.txt" -filter ".*bmel\.de/.*" &> logs/de_government/de_government_7_crawl
DIR=$(ls crawldata/de_government | grep de_government_7)
DIR2=$(ls crawldata/de_government/$DIR)
echo "Crawl finished! Now exporting... the time is `date`"
java -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -export -lang "en;de" -i "crawldata/de_government/$DIR/$DIR2" -bs  crawldata/de_government/$DIR/$DIR2/de_government -len 2 -mtlen 5 &> logs/de_government/de_government_7_export
ls -d crawldata/de_government/$DIR/$DIR2/* | grep -P "/[-\dT]+$" | xargs rm -r
echo "Now pair detecting... the time is `date`"
java -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -pairdetect -lang "en;de" -i "crawldata/de_government/$DIR/$DIR2/xml" -bs crawldata/de_government/$DIR/$DIR2/de_government -ifp -pdm "aupdih" &> logs/de_government/de_government_7_pairdetect
echo "Now aligning... the time is `date`"
java -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -align -lang "en;de" -i "crawldata/de_government/$DIR/$DIR2/xml" -bs corpora/de_government/de_government_7 &> logs/de_government/de_government_7_align
echo "Website 7 is finished! Now deleting some large binary files... the time is `date`"
if [ -d crawldata/de_government/$DIR/$DIR2/xml ]; then find crawldata/de_government/$DIR/$DIR2/xml -type f -name "*.html" | xargs rm; ls -d crawldata/de_government/$DIR/$DIR2/xml/* | grep -P "/*.pdf$" | xargs rm; fi
echo "Starting crawl on Website 8 - the time is `date`"
java -Dlog4j.configuration=file:log4j.xml -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -crawl -f -k -a de_government_8 -type p -lang "en;de" -n 100 -t 100 -len 0 -mtlen 40 -dest "crawldata/de_government" -u "seeds/de_government/de_government_8.txt" -filter ".*bmvg\.de.*" &> logs/de_government/de_government_8_crawl
DIR=$(ls crawldata/de_government | grep de_government_8)
DIR2=$(ls crawldata/de_government/$DIR)
echo "Crawl finished! Now exporting... the time is `date`"
java -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -export -lang "en;de" -i "crawldata/de_government/$DIR/$DIR2" -bs  crawldata/de_government/$DIR/$DIR2/de_government -len 2 -mtlen 5 &> logs/de_government/de_government_8_export
ls -d crawldata/de_government/$DIR/$DIR2/* | grep -P "/[-\dT]+$" | xargs rm -r
echo "Now pair detecting... the time is `date`"
java -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -pairdetect -lang "en;de" -i "crawldata/de_government/$DIR/$DIR2/xml" -bs crawldata/de_government/$DIR/$DIR2/de_government -ifp -pdm "aupdih" &> logs/de_government/de_government_8_pairdetect
echo "Now aligning... the time is `date`"
java -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -align -lang "en;de" -i "crawldata/de_government/$DIR/$DIR2/xml" -bs corpora/de_government/de_government_8 &> logs/de_government/de_government_8_align
echo "Website 8 is finished! Now deleting some large binary files... the time is `date`"
if [ -d crawldata/de_government/$DIR/$DIR2/xml ]; then find crawldata/de_government/$DIR/$DIR2/xml -type f -name "*.html" | xargs rm; ls -d crawldata/de_government/$DIR/$DIR2/xml/* | grep -P "/*.pdf$" | xargs rm; fi
echo "Starting crawl on Website 9 - the time is `date`"
java -Dlog4j.configuration=file:log4j.xml -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -crawl -f -k -a de_government_9 -type p -lang "en;de" -n 100 -t 100 -len 0 -mtlen 40 -dest "crawldata/de_government" -u "seeds/de_government/de_government_9.txt" -filter ".*bmfsfj\.de/.*" &> logs/de_government/de_government_9_crawl
DIR=$(ls crawldata/de_government | grep de_government_9)
DIR2=$(ls crawldata/de_government/$DIR)
echo "Crawl finished! Now exporting... the time is `date`"
java -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -export -lang "en;de" -i "crawldata/de_government/$DIR/$DIR2" -bs  crawldata/de_government/$DIR/$DIR2/de_government -len 2 -mtlen 5 &> logs/de_government/de_government_9_export
ls -d crawldata/de_government/$DIR/$DIR2/* | grep -P "/[-\dT]+$" | xargs rm -r
echo "Now pair detecting... the time is `date`"
java -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -pairdetect -lang "en;de" -i "crawldata/de_government/$DIR/$DIR2/xml" -bs crawldata/de_government/$DIR/$DIR2/de_government -ifp -pdm "aupdih" &> logs/de_government/de_government_9_pairdetect
echo "Now aligning... the time is `date`"
java -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -align -lang "en;de" -i "crawldata/de_government/$DIR/$DIR2/xml" -bs corpora/de_government/de_government_9 &> logs/de_government/de_government_9_align
echo "Website 9 is finished! Now deleting some large binary files... the time is `date`"
if [ -d crawldata/de_government/$DIR/$DIR2/xml ]; then find crawldata/de_government/$DIR/$DIR2/xml -type f -name "*.html" | xargs rm; ls -d crawldata/de_government/$DIR/$DIR2/xml/* | grep -P "/*.pdf$" | xargs rm; fi
echo "Starting crawl on Website 10 - the time is `date`"
java -Dlog4j.configuration=file:log4j.xml -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -crawl -f -k -a de_government_10 -type p -lang "en;de" -n 100 -t 100 -len 0 -mtlen 40 -dest "crawldata/de_government" -u "seeds/de_government/de_government_10.txt" -filter ".*bundesgesundheitsministerium\.de/.*" &> logs/de_government/de_government_10_crawl
DIR=$(ls crawldata/de_government | grep de_government_10)
DIR2=$(ls crawldata/de_government/$DIR)
echo "Crawl finished! Now exporting... the time is `date`"
java -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -export -lang "en;de" -i "crawldata/de_government/$DIR/$DIR2" -bs  crawldata/de_government/$DIR/$DIR2/de_government -len 2 -mtlen 5 &> logs/de_government/de_government_10_export
ls -d crawldata/de_government/$DIR/$DIR2/* | grep -P "/[-\dT]+$" | xargs rm -r
echo "Now pair detecting... the time is `date`"
java -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -pairdetect -lang "en;de" -i "crawldata/de_government/$DIR/$DIR2/xml" -bs crawldata/de_government/$DIR/$DIR2/de_government -ifp -pdm "aupdih" &> logs/de_government/de_government_10_pairdetect
echo "Now aligning... the time is `date`"
java -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -align -lang "en;de" -i "crawldata/de_government/$DIR/$DIR2/xml" -bs corpora/de_government/de_government_10 &> logs/de_government/de_government_10_align
echo "Website 10 is finished! Now deleting some large binary files... the time is `date`"
if [ -d crawldata/de_government/$DIR/$DIR2/xml ]; then find crawldata/de_government/$DIR/$DIR2/xml -type f -name "*.html" | xargs rm; ls -d crawldata/de_government/$DIR/$DIR2/xml/* | grep -P "/*.pdf$" | xargs rm; fi
echo "Starting crawl on Website 11 - the time is `date`"
java -Dlog4j.configuration=file:log4j.xml -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -crawl -f -k -a de_government_11 -type p -lang "en;de" -n 100 -t 100 -len 0 -mtlen 40 -dest "crawldata/de_government" -u "seeds/de_government/de_government_11.txt" -filter ".*bmvbs\.de/.*" &> logs/de_government/de_government_11_crawl
DIR=$(ls crawldata/de_government | grep de_government_11)
DIR2=$(ls crawldata/de_government/$DIR)
echo "Crawl finished! Now exporting... the time is `date`"
java -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -export -lang "en;de" -i "crawldata/de_government/$DIR/$DIR2" -bs  crawldata/de_government/$DIR/$DIR2/de_government -len 2 -mtlen 5 &> logs/de_government/de_government_11_export
ls -d crawldata/de_government/$DIR/$DIR2/* | grep -P "/[-\dT]+$" | xargs rm -r
echo "Now pair detecting... the time is `date`"
java -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -pairdetect -lang "en;de" -i "crawldata/de_government/$DIR/$DIR2/xml" -bs crawldata/de_government/$DIR/$DIR2/de_government -ifp -pdm "aupdih" &> logs/de_government/de_government_11_pairdetect
echo "Now aligning... the time is `date`"
java -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -align -lang "en;de" -i "crawldata/de_government/$DIR/$DIR2/xml" -bs corpora/de_government/de_government_11 &> logs/de_government/de_government_11_align
echo "Website 11 is finished! Now deleting some large binary files... the time is `date`"
if [ -d crawldata/de_government/$DIR/$DIR2/xml ]; then find crawldata/de_government/$DIR/$DIR2/xml -type f -name "*.html" | xargs rm; ls -d crawldata/de_government/$DIR/$DIR2/xml/* | grep -P "/*.pdf$" | xargs rm; fi
echo "Starting crawl on Website 12 - the time is `date`"
java -Dlog4j.configuration=file:log4j.xml -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -crawl -f -k -a de_government_12 -type p -lang "en;de" -n 100 -t 100 -len 0 -mtlen 40 -dest "crawldata/de_government" -u "seeds/de_government/de_government_12.txt" -filter ".*bmub\.de/.*" &> logs/de_government/de_government_12_crawl
DIR=$(ls crawldata/de_government | grep de_government_12)
DIR2=$(ls crawldata/de_government/$DIR)
echo "Crawl finished! Now exporting... the time is `date`"
java -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -export -lang "en;de" -i "crawldata/de_government/$DIR/$DIR2" -bs  crawldata/de_government/$DIR/$DIR2/de_government -len 2 -mtlen 5 &> logs/de_government/de_government_12_export
ls -d crawldata/de_government/$DIR/$DIR2/* | grep -P "/[-\dT]+$" | xargs rm -r
echo "Now pair detecting... the time is `date`"
java -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -pairdetect -lang "en;de" -i "crawldata/de_government/$DIR/$DIR2/xml" -bs crawldata/de_government/$DIR/$DIR2/de_government -ifp -pdm "aupdih" &> logs/de_government/de_government_12_pairdetect
echo "Now aligning... the time is `date`"
java -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -align -lang "en;de" -i "crawldata/de_government/$DIR/$DIR2/xml" -bs corpora/de_government/de_government_12 &> logs/de_government/de_government_12_align
echo "Website 12 is finished! Now deleting some large binary files... the time is `date`"
if [ -d crawldata/de_government/$DIR/$DIR2/xml ]; then find crawldata/de_government/$DIR/$DIR2/xml -type f -name "*.html" | xargs rm; ls -d crawldata/de_government/$DIR/$DIR2/xml/* | grep -P "/*.pdf$" | xargs rm; fi
echo "Starting crawl on Website 13 - the time is `date`"
java -Dlog4j.configuration=file:log4j.xml -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -crawl -f -k -a de_government_13 -type p -lang "en;de" -n 100 -t 100 -len 0 -mtlen 40 -dest "crawldata/de_government" -u "seeds/de_government/de_government_13.txt" -filter ".*bmbf\.de/.*" &> logs/de_government/de_government_13_crawl
DIR=$(ls crawldata/de_government | grep de_government_13)
DIR2=$(ls crawldata/de_government/$DIR)
echo "Crawl finished! Now exporting... the time is `date`"
java -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -export -lang "en;de" -i "crawldata/de_government/$DIR/$DIR2" -bs  crawldata/de_government/$DIR/$DIR2/de_government -len 2 -mtlen 5 &> logs/de_government/de_government_13_export
ls -d crawldata/de_government/$DIR/$DIR2/* | grep -P "/[-\dT]+$" | xargs rm -r
echo "Now pair detecting... the time is `date`"
java -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -pairdetect -lang "en;de" -i "crawldata/de_government/$DIR/$DIR2/xml" -bs crawldata/de_government/$DIR/$DIR2/de_government -ifp -pdm "aupdih" &> logs/de_government/de_government_13_pairdetect
echo "Now aligning... the time is `date`"
java -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -align -lang "en;de" -i "crawldata/de_government/$DIR/$DIR2/xml" -bs corpora/de_government/de_government_13 &> logs/de_government/de_government_13_align
echo "Website 13 is finished! Now deleting some large binary files... the time is `date`"
if [ -d crawldata/de_government/$DIR/$DIR2/xml ]; then find crawldata/de_government/$DIR/$DIR2/xml -type f -name "*.html" | xargs rm; ls -d crawldata/de_government/$DIR/$DIR2/xml/* | grep -P "/*.pdf$" | xargs rm; fi
echo "Starting crawl on Website 14 - the time is `date`"
java -Dlog4j.configuration=file:log4j.xml -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -crawl -f -k -a de_government_14 -type p -lang "en;de" -n 100 -t 100 -len 0 -mtlen 40 -dest "crawldata/de_government" -u "seeds/de_government/de_government_14.txt" -filter ".*bmz\.de/.*" &> logs/de_government/de_government_14_crawl
DIR=$(ls crawldata/de_government | grep de_government_14)
DIR2=$(ls crawldata/de_government/$DIR)
echo "Crawl finished! Now exporting... the time is `date`"
java -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -export -lang "en;de" -i "crawldata/de_government/$DIR/$DIR2" -bs  crawldata/de_government/$DIR/$DIR2/de_government -len 2 -mtlen 5 &> logs/de_government/de_government_14_export
ls -d crawldata/de_government/$DIR/$DIR2/* | grep -P "/[-\dT]+$" | xargs rm -r
echo "Now pair detecting... the time is `date`"
java -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -pairdetect -lang "en;de" -i "crawldata/de_government/$DIR/$DIR2/xml" -bs crawldata/de_government/$DIR/$DIR2/de_government -ifp -pdm "aupdih" &> logs/de_government/de_government_14_pairdetect
echo "Now aligning... the time is `date`"
java -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -align -lang "en;de" -i "crawldata/de_government/$DIR/$DIR2/xml" -bs corpora/de_government/de_government_14 &> logs/de_government/de_government_14_align
echo "Website 14 is finished! Now deleting some large binary files... the time is `date`"
if [ -d crawldata/de_government/$DIR/$DIR2/xml ]; then find crawldata/de_government/$DIR/$DIR2/xml -type f -name "*.html" | xargs rm; ls -d crawldata/de_government/$DIR/$DIR2/xml/* | grep -P "/*.pdf$" | xargs rm; fi
echo "Now for the tmxmerge part..."
python pythonscripts/tmxlist.py "de_government"
java -jar ilsp-fc-2.2.4-SNAPSHOT-jar-with-dependencies.jar -tmxmerge -lang "en;de" -i "corpora/de_government/de_government_tmx" -oxslt -pdm "aupdih" -segtypes "1:1" -bs corpora/de_government/de_government -mtuvl 2 -mpa "0.16" -minlr "0.6" -maxlr "1.6" -ksn &> logs/de_government/de_government_tmxmerge
echo "Webcrawl finished! Use websiterank.py to see how your corpus looks. The corpus is in /corpora, the xmls are all in /crawldata (consider archiving them!), and the logs are in /logs."
