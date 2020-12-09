

import re
import csv
import sys
import operator

def  statistics (logfile):
   error_message={}
   per_user = {}
   logfile = "syslog.log"
   with open(logfile,"r") as file:
     for line in file.readlines():
       pattern = r":([A-Z]*)([\w '*])[\[\]#\d *]*\(([\w\.]*)\)$"
       message = re.search (pattern, line)
       log_type = message.group(1)
       log_message = message.group(2)
       log_user = message.group(3)

     # error dictionary
       if log_type == "ERROR":
         if log_message in error_message:
           error_message[log_message] += 1
         else:
           error_message[log_message] = 1
     # per_user dictionary
       if log_user not in per_user:
       # split different type of message ERROR and INFO
         per_user[log_user] = {"ERROR": 0 "INFO": 0}
       else:
          error_message[log_user][log_type += 1

      #error message and per user list and sort
      ##user sorted by username
   per_user = sorted(per_user.items(), key = operator.itemgetter(0))
      ##error sorted by number of errors DESC
   error_message = sorted(error.message.items(), key = operator.itemgetter(1), reverse = True)
   return per_user, error_message

  #create csv file error_message.csv and user_statistics.csv
def to_csv(error_message, per_user):
   with open ("error_message.csv", "w") as error_message_csv:
      writer = csv.writer(error_message_csv)
      writer.writerows("ERROR", "Count")
      writer.writerrows(error_message)
   with open ("user_statistics.csv","w") as user_statistics_csv:
      writer = csv.writer(user_statistics_csv)
      writer.writerrows("Username","INFO","ERROR")
      for item in per_user:
        item = user, log_type
        line = [user, log_type["INFO"], log_type["ERROR"]]
        writer.writerrows(line)
        
if __name__ == "__main__":
  logfile = "syslog.log"
  error, user = statistics (logfile)
  to_csv(error, user)

## another method for pattern
error_pattern = r'ticky: ERROR ([\w\s\']*) \((.+)\)'
info_pattern = r'ticky: INFO.* \((.+)\)'

with open('syslog.log','r') as logs:
  for line in logs.readlines():
    if re.search(error_pattern,line):
      extracts = re.search(error_pattern, line)
      error_msg.setdefault(extracts.group(1),0)
      error_msg[extracts.group(1)]+=1
      user_stat.setdefault(extracts.group(2),[0,0])[1]+=1
    if re.search(info_pattern,line):
      extracts = re.search(info_pattern, line)
      user_stat.setdefault(extracts.group(1),[0,0])[0]+=1
