from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import lxml
import urllib.request
import webbrowser

website = urlopen("https://webservices.ulm.edu/forms/forms-list")
data = bs(website, "lxml")

forms = data.findAll("span", {"class": "file"})

forms_list = []
names = []
for f in forms:
  forms_list.append(f.find("a")["href"])
  names.append(f.get_text())

# print(forms_list)

for f in forms_list:
  webbrowser.open(f)
