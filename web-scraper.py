import requests
from bs4 import BeautifulSoup

#have user input the article they want parsed
article = input("Paste AP News article link: ")

# get the raw html file
r = requests.get(article)
html_doc = r.text

parsed = BeautifulSoup(html_doc, 'html.parser')
print(parsed.title.text)
