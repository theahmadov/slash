########################
#   Social Media Scan  #
########################

from profiles.autoimport import *
from profiles.notapi import notapi

def socmint(username):
    db = get_db()
    len_db = len(db)
    for i in range(0,len_db):
        if(db[f"{i}"]["type"]=="notapi"):
            try:
                cofi = notapi(username,db[f"{i}"])
                if(cofi!=None):
                    gathered.profiles.append(cofi)
            except Exception as e:
                #print(e)
                pass
            #print(gathered.profiles)
    


class profiles:
    def run(username):
        print(f"{symbol.log} Starting {color.bold}Social Media{color.reset} OSINT for {color.bold}{color.orange}{username}{color.reset}...")
        socmint(username)
        print(f"{symbol.log} {color.bold}Social Media OSINT{color.reset} finished. {color.bold}{color.red}{len(gathered.profiles)}{color.reset} results found...")
        
        # print(gathered.names)
        # print(gathered.locations)
        # print(gathered.educations)
        # print(gathered.bios)
        # print(gathered.linked_urls)
        # print(gathered.profiles)
        
        # print(gathered.phone_numbers)
        # print(gathered.mails)