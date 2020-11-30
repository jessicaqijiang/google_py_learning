#emails_test
#!/usr/bin/env python3
import unittest
from emails import find_email

#Create Email test class
class EmailTest(unittest.TestCase):
   def test_basid(self):
      testcase = [None, "Bree","Campbell"]
      expected = "breee@abc.edu"
      self.assertEqual(find_email(testcase),expected)

   def test_one_name(self):
      testcase= [None, "John"]
      expected = "Missing parameters"
      self.assertEqual(find_email(testcase),expected)

   def test_two_anme(self):
      testcase = [None,"Roy","Copper"]
      expected = "No email address found"
      self.asserEqual(find_email(testcase),expected)


if __name__ == '__main__':
   unittest.main()

#emails
#!/usr/bin/env python3

import sys
import csv

def populate_dictionary(filename):
  """Populate a dictionary with name/email pairs for easy lookup."""
  email_dict = {}
  with open(filename) as csvfile:
    lines = csv.reader(csvfile, delimiter = ',')
    for row in lines:
      name = str(row[0].lower())
      email_dict[name] = row[1]
  return email_dict

def find_email(argv):
  """ Return an email address based on the username given."""
  # Create the username based on the command line input.
  try:
    fullname = str(argv[1] + " " + argv[2])
  # Preprocess the data
    email_dict = populate_dictionary('/home/student-00-1d025e960b5c/data/user_emails.csv')
  # Find and print the email
    if email_dict.get(fullname.lower()):
       return email_dict.get(fullname.lower())
    else:
       return "No email address found"
  except IndexError:
    return "Missing parameters"

def main():
  print(find_email(sys.argv))

if __name__ == "__main__":
  main()

