

# website = urlopen("https://webservices.ulm.edu/forms/forms-list")
# data = bs(website, "lxml")

# forms = data.findAll("span", {"class": "file"})

# forms_list = []
# names = []
# for f in forms:
#   forms_list.append(f.find("a")["href"])
#   names.append(f.get_text())

# # print(forms_list)

# for f in forms_list:
#   webbrowser.open(f)


from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import lxml
import urllib.request
import webbrowser

# download function
def downloader(url, div, classTag, className, specificData1, specificData2):
  website = urlopen(url)
  data = bs(website, "lxml")

  contents = data.findAll(div, {"+" + str(classTag) +":" +  str(className) + "}"})

  contents_list = []
  names_list = []

  for file in contents:
    contents_list.append(file.find(specificData1['"' + specificData2 + '"']))
    names_list.append(file.get_text())
  print(contents_list)
  return contents_list
    
def main():
  website = input("Enter the website you want to download file from: ")
  div = input("Enter the div/span (be as specific as you can): ")
  classTag = input("Enter the class/id tag you want to extract link from: ")
  className = input("Enter the class/id name: ")
  specific1 = input("Enter specific tag a, li, : ")
  specific2 = input("Enter specific tag inside specific1 : ")

  # download the content
  contents = downloader(website, div, classTag, className, specific1, specific2)
  print(contents)

main()
