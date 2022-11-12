import requests
from bs4 import BeautifulSoup

URL = 'https://www.etuovi.com'
ID = "mui-52368"

print("jee")
r = requests.get(URL)
sivu = BeautifulSoup(r.text,"html.parser")

linkit = sivu.find_all("input")
for a in linkit:
    print(a)
    print()

#print(sivu)


#print(r.text)