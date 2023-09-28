from bs4 import BeautifulSoup

with open("index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

tag = doc.find_all("p")
# tag = doc.title
# tag.string ="helo"
