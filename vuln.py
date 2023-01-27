import requests, argparse, sys
from colorama import *

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', help='url', required=True)
parser.add_argument('-p', '--payloads', help='payloads list', required=True)
args = parser.parse_args()

def fuzz(url, payloads):
    for payload in open(payloads, 'r').readlines():
        new_url = url.replace('{fuzz}', payload)
        request = requests.get(new_url)
        if request.elapsed.total_seconds() > 7:
            print(Style.BRIGHT + Fore.RED + 'Timeout detected with ', new_url)
        else:
            print(Style.BRIGHT + Fore.CYAN + 'Not working with this payload ', payload)

def verif(url):
    url_test = url.replace('{fuzz', '')
    req = requests.get(url_test)
    if req.elapsed.total_seconds() > 5:
        sys.exit(Style.BRIGHT + Fore.RED + 'Please make sure you have a stable internet connection')
    else:
        fuzz(args.url, args.payloads)
if not '{fuzz}' in args.url:
    sys.exit(Style.BRIGHT + Fore.RED + 'Missing {fuzz} parameter')
else:
    verif(args.url)