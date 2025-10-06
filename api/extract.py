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

"""
Email extraction previously used a very loose pattern ("\S+@\S+") which
caused false positives (e.g., tokens with trailing punctuation). We now use a
centralized, stricter regex that matches typical email addresses and respects
word boundaries.

Pattern:
- Local part: [A-Za-z0-9._%+-]+
- Domain: [A-Za-z0-9.-]+ with at least one dot
- TLD: [A-Za-z]{2,}
"""

# Centralized, stricter email pattern
EMAIL_RE = re.compile(r"\b[a-zA-Z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")

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
        mails = EMAIL_RE.findall(text)
        if(len(mails)!=0):
            alert(mails,from_name,mails=True)
        try:
            return mails
        except:
            return []

    class just:
        def mail(text):
            mails = EMAIL_RE.findall(text)
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