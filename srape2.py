import requests
from bs4 import BeautifulSoup

html_text = requests.get("https://michael-lyon.github.io/e-commerce-front-end/").text
soup = BeautifulSoup(html_text ,"lxml")
# print(soup)
div1 = soup.find_all("div", class_ = "pro-container")
for i in div1:
    h5 = i.h5
    img =i.img
print(h5)
print(img) 