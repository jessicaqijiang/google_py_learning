# cat a list 
student-01-c02e2caebdce@linux-instance:~$ cd data
student-01-c02e2caebdce@linux-instance:~/data$ cat list.txt

001 jane /data/jane_profile_07272018.doc
002 kwood /data/kwood_profile_04022017.doc
003 pchow /data/pchow_profile_05152019.doc
004 janez /data/janez_profile_11042019.doc
005 jane /data/jane_pic_07282018.jpg
006 kwood /data/kwood_pic_04032017.jpg
007 pchow /data/pchow_pic_05162019.jpg
008 jane /data/jane_contact_07292018.csv
009 kwood /data/kwood_contact_04042017.csv
010 pchow /data/pchow_contact_05172019.csv

student-01-c02e2caebdce@linux-instance:~/data$ ls
jane_contact_07292018.csv  jane_profile_07272018.doc  janez_profile_11042019.doc  kwood_pic_04032017.jpg  kwood_profile_04022017.doc  list.txt  pchow_pic_05162019.jpg


#!/bin/bash
#create empry rile oldFiles.txt
> oldFiles.txt
files=`grep 'jane' ../data/list.txt | cut -d ' ' -f 3`
#echo "$files" >> oldFiles.txt
for file in $files; do
  if [ -e $HOME$file ]; then
    echo $HOME$file >> oldFiles.txt;
  fi
  done
  
#Change file name
#!/usr/bin/env python3

import sys
import subprocess

#open file and read lines
file = open (sys.argv[1], "r")
for line in file.readlines():
  old_name = line.strip()
  new_name = old_name.replace("jane", "jdoe")
      #MV rename the files
  subprocess.run(["mv", old_name, new_name])
file.close()



