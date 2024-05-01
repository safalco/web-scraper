import requests
from bs4 import BeautifulSoup

# get the raw html file
r = requests.get('https://apnews.com/article/catholic-church-shift-orthodoxy-tradition-7638fa2013a593f8cb07483ffc8ed487')
html_doc = r.text

parsed = BeautifulSoup(html_doc, 'html.parser')
print(parsed.title.string)
