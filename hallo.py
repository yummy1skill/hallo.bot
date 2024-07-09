# Made with ❤ by yummy
import argparse
import random
import requests
from requests.structures import CaseInsensitiveDict
import time
import datetime
from colorama import init, Fore, Style
init(autoreset=True)


 # Tentukan waktu mulai saat bot dijalankan

def balence (token):
    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'en-US,en;q=0.9,id;q=0.8',
        'Content-Type': 'application/json',
        'Origin': 'https://bot.crossfi.org',
        'Referer': 'https://bot.crossfi.org/',
        'priority': 'u=1, i',
        'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'Sec-Ch-Ua-mobile': '?1',
        'Sec-Ch-Ua-platform': '"Android"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36',
}
    
      
def get_new_token(query_id):
    import json
    # Header untuk permintaan HTTP
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9,id;q=0.8",
        "content-type": "application/json",
        "origin": "https://bot.crossfi.org",
        "priority": "u=1, i",
        "referer": "https://bot.crossfi.org/"
    }

    # Data yang akan dikirim dalam permintaan POST
    data = json.dumps({"query": query_id})



