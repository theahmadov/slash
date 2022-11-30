import re 
from core import (
    banner,
    color,
    symbol,
    clear,
    highlight,
    info_highlight,
    error_highlight,
    css
)

def alert(values,from_name,phones=False,mails=False):
    print()
    if(phones):
        out = f"{color.reset}[{color.redbg}{from_name}/Phone{color.reset}]:"
        for number in values:
            out+=f"\n     {color.reset}[{color.whitebg}{from_name}{color.reset}] {color.bold}Phone Number{color.reset} : [{color.red}{color.underline}{number}{color.reset}]"
        print(out)
    elif(mails):
        out = f"{color.reset}[{color.redbg}{from_name}/Mail{color.reset}]:"
        for adress in values:
            out+=f"\n     {color.reset}[{color.whitebg}{from_name}{color.reset}] {color.bold}Mail Adress{color.reset} : [{color.red}{color.underline}{adress}{color.reset}]"
        print(out)

    print()

class extract:
    def phone(from_name,text):
        #print(text)
        txt=re.compile(r'(\(?\d{2,3}\)?\D{0,3}\d{6,10}|\d{10})')
        nums=txt.findall(text)
        if(len(nums)!=0):
            alert(nums,from_name,phones=True)
        try:
            return nums
        except:
            return []

    def mail(from_name,text):
        mails = re.findall('\S+@\S+', text) 
        if(len(mails)!=0):
            alert(mails,from_name,mails=True)
        try:
            return mails
        except:
            return []

    class just:
        def mail(text):
            mails = re.findall('\S+@\S+', text) 
            try:
                return mails
            except:
                return []


        def phone(text):
            #print(text)
            txt=re.compile(r'(\(?\d{2,3}\)?\D{0,3}\d{6,10}|\d{10})')
            nums=txt.findall(text)
            try:
                return nums
            except:
                return []