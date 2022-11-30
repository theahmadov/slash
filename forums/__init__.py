from forums.auto import *

class gathered:
    username = ""
    profiles = []

def forums_check(dct):
    username = gathered.username
    name=dct["name"]
    url=dct["url"].format(username)
    check_code = dct["check_code"]
    check = dct["check"]
    htext = highlight(url,username)
    
    if(check_code=="1"):
        
        req = urlopen(url,timeout=4)
        try:
            source = req.read().decode("utf-8")
        except:
            source = req.read().decode("latin-1")

        if(check.format(username) in source):
            print(f"{symbol.forum_found} {color.blue}{color.bold}forum/{color.green}{color.bold}{name}{color.reset} : {htext}{color.reset}")
            gathered.profiles({name:url})

    elif(check_code=="2"):
        req = urlopen(url,timeout=4)
        st = req.getcode()
        try:
            source = req.read().decode("utf-8")
        except:
            source = req.read().decode("latin-1")

        if(st!=check):
            print(f"{symbol.forum_found} {color.blue}{color.bold}forum/{color.green}{color.bold}{name}{color.reset} : {htext}{color.reset}")
            gathered.profiles({name:url})
            print({name:url})

    elif(check_code=="3"):
        req = urlopen(url,timeout=40)
        #print(req)
        try:
            source = req.read().decode("utf-8")
        except:
            source = req.read().decode("latin-1")
        #print(highlight(text=source, selected=check))
        if(not check in source):
            print(f"{symbol.forum_found} {color.blue}{color.bold}forum/{color.green}{color.bold}{name}{color.reset} : {htext}{color.reset}")
            gathered.profiles({name:url})
    

def focmint(username):
    db = get_db()["forums"]
    ldb = len(db)

    for i in range(0,ldb):
        try:
            forums_check(db[i])
        except Exception as e:
            pass#;print(e)

class forums:
    def run(username):
        print(f"{symbol.log} Searching {color.bold}{color.orange}{username}{color.reset} on {color.bold}Forums{color.reset}...")
        gathered.username = username
        focmint(username)
        print(f"{symbol.log} {color.bold}Forum Search{color.reset} finished. {color.bold}{color.red}{len(gathered.profiles)}{color.reset} results found...")