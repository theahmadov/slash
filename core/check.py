def ismail(username):
    try:
        lst = username.split("@")
        try:
            domain = lst[1].split(".")
            if(len(domain)==2):
                return True
            else:
                return False
        except:
            return False
    except:
        return False