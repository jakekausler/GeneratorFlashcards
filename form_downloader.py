import requests
from bs4 import BeautifulSoup as BS

PAGE = "https://en.wiktionary.org/wiki/%CF%87%CE%B1%CE%AF%CF%81%CF%89"

r = requests.get(PAGE)
soup = BS(r.text, features="html.parser")
navframes = soup.find_all(find_conjugations)