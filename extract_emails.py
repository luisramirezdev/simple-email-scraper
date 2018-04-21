#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import urllib
from urllib.request import urlopen
from urllib.request import urlretrieve
from urllib.parse import quote


# Get emails function
def run_emails():
    filepath = 'domains.txt'
    with open(filepath) as fp:
        for line in fp:
            try:
                print (line)
                page_1 = urlopen("http://%s" % line).read().decode('ISO-8859-1')

                match = re.findall(r'[\w\.-]+@[\w\.-]+', page_1)
                with open("emails.txt", "a") as f:
                    for s in match:
                        f.write(str(s) +"\n")

            except urllib.error.HTTPError as e:
                if e.code in (..., 403, ...):
                    continue
            except urllib.error.URLError as e:
                print("Skip -> URL Error")
    Continue()


# Main function
def main():
    print ("==============")
    print ("What option do you want?")
    print ("")
    print ("1.- I have txt with domains to extract")
    print ("0.- Exit")
    print ("")
    print ("==============")
    input_main = input("Select an option: ")

    if (input_main == '1'):
        run_emails()
    if (input_main == '0'):
        print('\n'
              'Thanks for using this Script! If you enjoyed this script, start the repo http://github.com/luisramirez-m/simple-email-scraper')
        quit()
    else:
        pass

# Function to continue
def Continue():
    keep_going = input('Do you want to keep going? Enter yes or no. \n'
                       '').lower()
    # evaluates user's response.
    if keep_going == 'yes':
        main()
    elif keep_going == 'no':
        print('\n'
              'Thanks for using this Script! If you enjoyed this script, start the repo http://github.com/luisramirez-m/simple-email-scraper')
        quit()
    else:
        print('\n'
              'Input not recognized. Try again.')


# Runs the main function, which runs everything else.
if __name__ == "__main__":
    main()

main()