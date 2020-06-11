#!/usr/bin/python3
# script for display the redirects...

import sys
import requests
import time

# permutate the words from wordlist and append to URL ...     
def permutate_subdir(path):
    try:
        with open(path,'r') as file:      
            for line in file:       
                for word in line.split():
                    url = sys.argv[1]+'/'+word
                    time.sleep(1)
                    for x in chase_redirects(url):
                        print(x)
    except FileNotFoundError:
        print('[!] Unable to detect the wordlist.')           

# main loop to display the redirects ...
def chase_redirects(url):
    print('\n* * * * * *')
    while True:
        try:
            yield url
            r = requests.head(url, timeout=4)
            if 300 < r.status_code < 400:
                url = r.headers['location'] 
                print('status code -> '+ str(r.status_code) + '\n--------------------------------------\n')
            else:
                break
        except requests.ConnectTimeout:
            print('[!]Connection timed out')
            break
        except requests.ConnectionError:
            print('[!]Connection error occured...')
            break

if len(sys.argv) > 1:
    permutate_subdir(sys.argv[2])
else:
    sys.exit(0)
