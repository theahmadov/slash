import typer
from os import system
import time

from smi import smi
from fmi import fmi 

from lib import (
    banner,
    color,
    symbol,
    clear
)
from lib.check import *
import threading
import argparse 

from api.pastebin import search as pastesearch
from api.github import search as githubsearch
from api.extract import extract as extract 



def gethelp():
    print(f"""{symbol.help_found}:
    -u : set username (--u username)
    -m : set mail address (--m mailaddress)

    Username {color.redbg}OSINT{color.reset} include {color.bold}paste{color.reset} search, 
    {color.bold}social media{color.reset} dedective, {color.bold}forum{color.reset} search.

    Example :
    {color.graybg}{color.red}{color.bold}${color.reset}{color.graybg} python slash.py --u thesaderror{color.reset}
    {color.graybg}{color.red}{color.bold}${color.reset}{color.graybg} python slash.py --m target@gmail.com{color.reset}""")

def _username(username):
    print(f"{symbol.log} {symbol.slash} starting...")
    print(f"{symbol.log} Username [{color.green}{color.bold}{username}{color.reset}] succesfully setted.")
    threading.Thread(target=smi.run,args=(username,)).start()
    threading.Thread(target=fmi.run,args=(username,)).start()
    time.sleep(5)
    threading.Thread(target=pastesearch,args=(username,)).start()
    threading.Thread(target=githubsearch,args=(username,)).start()

def _mail(mail_adress):
    print(f"{symbol.log} {symbol.slash} starting...")
    print(f"{symbol.log} Mail adress [{color.green}{color.bold}{mail_adress}{color.reset}] succesfully setted.")
    threading.Thread(target=pastesearch,args=(mail_adress,)).start()
    threading.Thread(target=githubsearch,args=(mail_adress,)).start()


    
def _start(value : str):

    if(value=="/" or value=="h"):
        gethelp()
    elif(len(extract.just.mail(value))!=0):
        _mail(value)
    elif(len(extract.just.phone(value))!=0):
        pass
    else:
        _username(value)

if __name__ == "__main__":
    clear()
    print(banner.slash)
    #_start()
    typer.run(_start)

# By Thesaderror...