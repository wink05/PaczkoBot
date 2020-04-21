# Here script will know what to import to work
import os
import time
import requests
import argparse
import fbchat
import linecache
from bs4 import BeautifulSoup
from fbchat import Client
from fbchat.models import *

parser = argparse.ArgumentParser()

# -l FBLOGIN -p FBPASS -t TRACKINGNUM -gid SECONDS -n NAZWAPAKI
parser.add_argument("-l", dest = "login", default = "", help="Facebook Login")
parser.add_argument("-p", dest = "password", default = "", help="Facebook Password")
parser.add_argument("-t", dest = "tracking", default = "", help="Tracking Number")
parser.add_argument("-gid", dest = "groupid", default="", help="Group ID")
parser.add_argument("-r", dest = "refreshtime", default="60", help="Refresh time in seconds")
parser.add_argument("-n", dest = "packname", default="", help="Nazwa Paczki")

args = parser.parse_args()

client = Client(args.login, args.password) 
def important():
    os.system("title PaczkoBot v1.0")
    print("PaczkoBot v1.0")
    print("Stworzony przez Michała Winka")
    print("Przechodze do logowania...")
    print("====================================")

def siteprepare():
    print("Pobieranie strony...")
    r = requests.get("https://furgonetka.pl/zlokalizuj/" + args.tracking, allow_redirects=True)
    open('index.html', 'wb').write(r.content)
    print("Strona pobrana!")
    print("====================================")

def clsandsend():
    current_time = time.strftime("%d.%m.%Y, %H:%M:%S")
    cleantext = BeautifulSoup(linecache.getline('index.html', 386), "lxml").text
    odkiedy = BeautifulSoup(linecache.getline('index.html', 387), "lxml").text
    client.send(Message(text="Nazwa paczki: " + args.packname + "\nStatus przesyłki: " + cleantext + "od:" + odkiedy + "Sprawdzono: " + current_time), thread_id=args.groupid, thread_type=ThreadType.GROUP)
    print("\nNazwa paczki: " + args.packname + "\nStatus przesyłki: " + cleantext + "od:" + odkiedy + "Sprawdzono: " + current_time)
    os.remove('index.html')
    print("====================================")

while True:
    important()
    siteprepare()
    clsandsend()
    time.sleep(int(args.refreshtime))