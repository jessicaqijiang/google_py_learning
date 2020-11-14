
#!/usr/bin/env python3

#Import libraries
import csv
import re


def contains_domain(address, domain):
  """Returns True if the email address contains the given domain,in the domain position, false if not."""
  domain_pattern =r'[\w\.-]+@'+domain+'$'
  if re.match(domain_pattern, address):
     return True
  return False

def replace_domain(address, old_domain, new_domain):
  """Replaces the old domain with the new domain in the received address."""
  old_domain_pattern = r" " + old_domain + "$"
  address = re.sub(old_domain_pattern, new_domain, address)
  return address

def main():
  """Processes the list of emails, replacing any instances of the old domain with the new domain."""
  old_domain, new_domain = "abc.edu", "xyz.edu"
  csv_file ="/home/student-00-47d6a3159870/data/user_emails.csv"
  report_file = "/home/student-00-47d6a3159870/data/" + "/update_user_emails.csv"
  #Create List
  user_email_list = []
  old_domain_email_list = []
  new_domain_email_list = []
  #Open csv file read user emails and fill into list
  with open(csv_file, "r") as file:
     user_data_list = list(csv.reader(file))
     user_email_list = [data[1].strip() for data in user_dat_list[1:]]

     for email_address in user_email_list:
       if contains_domain(email_address, old_domain):
        old_domain_email_list.append(email_address)
        new_domain_email = replace_domain(email_address,old_domain, new_domain)
        new_domain_email_list.append(new_domain_email)

     email_pattern = " " + "Email Address"
     email_index = user_data_list[0].index(email_pattern)

     for user in user_data_list[1:]:
        for old_domain, new_domain in zip(old_domain_email_list, new_domain_emial_list):
           if user[email_index] == " " + old_domain:
             user[email_index] = " " +new_domain
  file.close()
  #Write list as output file
  with open(report_file, "w+") as output_file:
      writer = csv.writer(output_file)
      writer.writerows(user_data_list)
  output_file.close()

main()

