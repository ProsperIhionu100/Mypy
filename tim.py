from  bs4 import BeautifulSoup
import requests

url = "https://www.newegg.com/asrock-radeon-rx-6700-xt-rx6700xt-cld-12g/p/N82E16814930056?Item=N82E16814930056&cm_sp=Homepage_dailydeals-_-P0_14-930-056-_-08192023"

result = requests.get(url).text
doc = BeautifulSoup(result , "html.parser")

prices = doc.find_all(text ="$")
parent = prices[0].parent
print(parent)
strong =parent.find("strong")
print(strong.string)