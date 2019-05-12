#!/usr/bin/python

# Python implementation of the google queries from (Goohak) 1N3@CrowdShield


import requests
import sys
import argparse
import webbrowser
from time import sleep



queries = [
        "https://www.google.de/search?q=site:{0}+username+OR+password+OR+login+OR+root+OR+admin",
        "https://www.google.de/search?q=site:{0}+inurl:readme+OR+inurl:license+OR+inurl:install+OR+inurl:setup+OR+inurl:config",
        "https://www.google.de/search?q=site:{0}+inurl:shell+OR+inurl:backdoor+OR+inurl:wso+OR+inurl:cmd+OR+shadow+OR+passwd+OR+boot.ini+OR+inurl:backdoor",
        "https://www.google.de/search?q=site:{0}+inurl:wp-+OR+inurl:plugin+OR+inurl:upload+OR+inurl:download",
        "https://www.google.de/search?q=site:{0}+inurl:redir+OR+inurl:url+OR+inurl:redirect+OR+inurl:return+OR+inurl:src=http+OR+inurl:r=http",
        "https://www.google.de/search?q=site:{0}+ext:cgi+OR+ext:php+OR+ext:asp+OR+ext:aspx+OR+ext:jsp+OR+ext:jspx+OR+ext:swf+OR+ext:fla+OR+ext:xml",
        "https://www.google.de/search?q=site:{0}+ext:doc+OR+ext:docx+OR+ext:csv+OR+ext:pdf+OR+ext:txt+OR+ext:log+OR+ext:bak",
        "https://www.google.de/search?q=site:{0}+ext:action+OR+struts",
        "https://www.google.de/search?q=site:pastebin.com+{0}",
        "https://www.google.de/search?q=site:linkedin.com+employees+{0}"
        ]





def main():
    parser = argparse.ArgumentParser(description='Google OSINT for domains')
    parser.add_argument('-d', '--domain', help='Enter domain to search' ,type=str)
    args = parser.parse_args()
    if not len(sys.argv) > 1:
        print("You have to pass an argument. Insert -h for more information.")
        sys.exit(0)
    # Check vor valid domain
    try:
        print("Trying to reach the domain (http)")
        r1 = requests.get("http://"+args.domain)
        if r1.status_code != 200:
            print("Trying to reach the domain (https)")
            r2 = requests.get("https://"+args.domain)
            if r2.status_code != 200:
                 if input("Are you sure the given domain is correct?").lower().startswith("n"):
                     print("closing programm...")
                     sys.exit(1)
        print(args.domain+" seems valid!")
        for querie in queries:
                sleep(3)
                webbrowser.open(querie.format(args.domain))
    
    except Exception as error:
        print(error)
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('\nInterrupted by human...')
        sys.exit(0)


