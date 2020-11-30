
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

