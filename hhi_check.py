#!/usr/bin/python3
# Python 3.x based Host-header-attack Checker.
# Dependencies --> 1.Python 3x Standard libraries, 2.Scrapy framework ...
# This is the main file of the tool.
# Crawler file is under spiders directory of project folder. 

import subprocess
import time
import sys, re
import requests
import argparse
from colors import blue, green, red, yellow, reset

# Just a fancy duck banner ;)
banner = f"""{blue}
BINT LABS | Brisk Host Header Injection Tool v1.0{reset}{green}
                :::::::::   :::    :::  :::    :::  :::::::::::  ::::::::::: 
                :+:    :+:  :+:    :+:  :+:    :+:      :+:          :+:     
                +:+    +:+  +:+    +:+  +:+    +:+      +:+          +:+     
                +#++:++#+   +#++:++#++  +#++:++#++      +#+          +#+     
                +#+    +#+  +#+    +#+  +#+    +#+      +#+          +#+     
                #+#    #+#  #+#    #+#  #+#    #+#      #+#          #+#     
                #########   ###    ###  ###    ###  ###########      ###{reset}   
                                {blue}Powered by BRISKINFOSEC(www.briskinfosec.com){reset}
                                """

# Defined statements for parsing the user arguments correctly...
parser = argparse.ArgumentParser(description='Host Header Attack Detector',
epilog='Providing the URL (-u) option only will crawl the links automatically related to given url and domain.')
rparser = parser.add_argument_group('required argument')
rparser.add_argument("-u","--url", type=str, help='specify the URL with it\'s correct scheme', required=True)
parser.add_argument("-w","--wordlist", type=str, help='integrate the wordlist with given URL and perform the request')
args = parser.parse_args()

# Fetch the url using regex from redirects.py, feed and invoke the calls.
def PermutateWithWordlist(url, wordlist):
    print(f'\n{green}[+] Performing the wordlist permutations with the given URL...{reset}\n')
    print('[!] Please wait until the result is being retrived...\n')
    output = subprocess.check_output([sys.executable, 'redirects.py', url, wordlist])
    pattern = re.compile(r'[^n]+/[.a-zA-Z0-9/\][%?=:&+-]+\\nstatus code -> 301')
    matches = pattern.findall(str(output))
    urls = []
    for i in matches:
        i = i.replace(r'\nstatus code -> 301','')
        urls.append(i)
    if not urls:
         print(f'{yellow}[!] No redirections occured to perform the attack.\n{blue}\n[+] Exiting!...{reset}\n')
    else:
        for url in urls:
            time.sleep(1)
            for x in PerformThetest(url):
                print(x)
  
# Fetch the 301 & 302 urls using regex from spider, feed and invoke the calls.
def ProcessWithSpider(url):
    print(f'\n{green}[+] Invoking the scrapy crawler...{reset}\n\n[!] Please wait until the crawling process gets over...\n')
    print('[!] Please maintain the patience for at least 30 secs. Crawling delay depends upon the scope of target domain...\n')
    url = url
    domain = url.split('//')[1].split('/')[0]
    output = subprocess.check_output(['scrapy','crawl','start','-a',f'url={url}','-a', f'domain={domain}'],\
         universal_newlines=True, stderr=subprocess.DEVNULL) 
    pattern = re.compile(r"(.*(301|302))")
    matches = pattern.findall(str(output))  
    urls = []
    for i in matches:
        for j in i:
            if len(j) > 3:
                j = j.replace('-> 302', '')
                urls.append(j)
    # Conditionals blocks for passing the url as arguments to function call
    if not urls:
         print(f'{yellow}[!] No redirections occured to perform the attack.\n{blue}\n[+] Exiting!...{reset}\n')
    else:
        for url in urls:
            time.sleep(1)
            for x in PerformThetest(url):
                print(x)
  
# perform the Host_header_attack test
def PerformThetest(url):
    while True:
        print('---------------------------------------------------------------')
        yield url
        print('---------------------------------------------------------------')
        # Modify and send the Host-header            
        print('[*] Trying with modified host header... ')
        req = requests.head(url, timeout=4, headers={ 
                'Host':'bing.com',
                'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0' 
        })
        try:
            if 'bing.com' in req.headers['location']:                       
                print(f'{red}[!] Prone to Host header attack.             ->   (Vulnerable){reset}')
                print('---------------------------------------------------------------')
                break
            else:
                print(f'{green}[*] Not vulnerable to the Host header attack...{reset}')
        except KeyError:
            print(f'{yellow}:(  Bad Request, Unable to fetch the location header.{reset}')
        
        # Add X-Forwarded-Host Header
        print('[*] Trying with X-Forwarded-Host header... ')
        req_x = requests.head(url, timeout=4, headers={     
            'X-Forwarded-Host':'bing.com',
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'
        })
        try:
            if 'bing.com' in req_x.headers['location']:
                print(f'{red}[!] Prone to Host header attack.             ->   (Vulnerable){reset}') 
            else:
                print(f'{green}[*] Not vulnerable to the Host header attack...{reset}\n---------------------------------------------------------------')
                break
        except KeyError:
            print(f'{yellow}:(  Bad Request, Unable to fetch the location header.{reset}\n---------------------------------------------------------------')  
        break   

if __name__ == "__main__":
    # Conditional logics for execution... 
    if args.url and args.wordlist:
        start = time.time()
        print(banner)
        PermutateWithWordlist(args.url, args.wordlist)
        end = time.time()
        print(f'{green}[+] Finished automated host-header-attack scripts in {yellow}'+ str(round(end - start))+f'{green} secs.\n{reset}')
    
    elif args.url:
        start = time.time()
        print(banner)
        ProcessWithSpider(args.url)
        end = time.time()
        print(f'{green}[+] Finished automated host-header-attack scripts in {yellow}'+ str(round(end - start))+f'{green} secs.\n{reset}')

    


  
    
