import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
import logging

flipkart_url="https://www.flipkart.com/search?q="+"iphone11"
# print(flipkart_url)

# bina click karai kholna hai

urlclient=uReq(flipkart_url)

# print(urlclient)
flip_kartpage=urlclient.read()
# print(flip_kartpage)
flipkart_html=bs(flip_kartpage,'html.parser')
# print(flipkart_html)
bigbox=flipkart_html.findAll("div",{"class":"_1AtVbE col-12-12"})
a=len(bigbox)
print(a)
productlink="https://www.flipkart.com"+bigbox[2].div.div.div.a['href']
for i in bigbox:
    print(productlink)

product_req=requests.get(productlink)
product_html=bs(product_req.text,'html.parser')
reviwbox=product_html.findAll("div",{"class":"_16PBlm"})
print(len(reviwbox))
# name
for i in reviwbox:
    print(i.div.div.findAll('p',{"class":"_2sc7ZR _2V5EHH"})[0].text)

# rating
for i in reviwbox:
    print(i.div.div.div.div.text)

# comment heading
for i in reviwbox:
    print(i.div.div.div.p.text)

# actual comment
for i in reviwbox:
    print(i.div.div.findAll('div',{"class":''})[0].div.text)