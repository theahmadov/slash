from bs4 import BeautifulSoup

def span(source,classname):
    soup = BeautifulSoup(source, "html.parser")
    found = soup.find("span", {"class": classname})
    return found.text

def ahead(source,classname):
    soup = BeautifulSoup(source, "html.parser")
    found = soup.find("a", {"class": classname})
    return found.text

def div(source,classname):
    soup = BeautifulSoup(source, "html.parser")
    found = soup.find("div", {"class": classname})
    return found.text

def phead(source,classname):
    soup = BeautifulSoup(source, "html.parser")
    found = soup.find("p", {"class": classname})
    return found.text

def h1(source,classname):
    soup = BeautifulSoup(source, "html.parser")
    try:
        found = soup.find("h1", {"class": classname}).text
    except:
        found = soup.find("h1", class_ = classname).text

    return found

def section(source,classname):
    soup = BeautifulSoup(source, "html.parser")
    try:
        found = soup.find("section", {"class": classname}).text
    except:
        found = soup.find("section", class_ = classname).text

    return found

# import requests

# print(phead(requests.get("").text, "profile__head-display-name"))