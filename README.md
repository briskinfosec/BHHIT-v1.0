# BHHIT v1.0
<br>
<img width="200" src="https://github.com/briskinfosec/BHHIT-v1.0/blob/master/images/screenshot.png" /><br>

## Brisk Host Header Injection Tool
An open-source Python-3x based automated Host-Header-Injection attack detector. Generally the main component of the tool is `hhi_check.py` file. Executing this by passing some arguments will display the results. This is a small automation tool, usually works in two ways, 

1. This tool will crawl all the links of the target website by setting it's scope domain automatically then, it will only fetch the redirected urls (301, 302) status codes and after that it's going to perform the test. Spidering and crawling will be done by python-scrapy. The crawler file `hhi_crawl.py` is under core/spiders/. You can tweak many crawling functionalities if you are familiar with the scrapy-framework and python scripting.

***Note:*** This crawling process may take a while and the duration time is depends upon scope of the target web site (How huge the website is).

2. You can also use the wordlist to perform like the brute-force kind of test. No crawler is indulged in this method. that means the keywords and phrases will be read from your specified wordlist file after that, it's going to perform the permutation for each and every single request of targeted url then, it will perform the further activity.

***Note:*** This tool results may provide some false positives. 

## Documentation
* https://github.com/briskinfosec/BHHIT-v1.0/wiki

## Updates
If you want new features, create an issue report and label it as enhancement Or start a pull request on our repositories.

## Credits:
* ArulSelvar Thomas: [Founder and Director of BriskInfosec Technology and Consulting Pvt Ltd](https://in.linkedin.com/in/briskinfosec)
* Karthik : Security Engineer

## :octocat: How to contribute
All contributions are welcome, from code to documentation, to design suggestions, to bug reports.
Please use GitHub to its fullest. submit pull requests, contribute tutorials or other wiki content, whatever 
you have to offer, we can use it!

## Support us !
BHHIT is developed with an intended to create cyber security awareness in IT industry. If you want to support us 
in a any possible way,please do it. Here is our official Email address:contact@briskinfosec.com or visit our website [Briskinfosec](http://www.briksinfosec.com) for more details.

## Useful links:
 1. [Brisk Infosec] (www.briskinfosec.com/)
 2. [NCDRC] (http://www.ncdrc.res.in/)
 3. [BINT LABS] (http://briskinfosec.com/bint%20testing)
 
## Disclaimer:

***Note: BHHIT is intended to be used for legal security purposes only, and you should only use it to protect web applications and sites you own or have permission to test. Any other use is not the responsibility of the developer(s). Be sure that you understand and are complying with the BHHIT tool licenses and laws in your area.***
