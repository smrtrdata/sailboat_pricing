from bs4 import BeautifulSoup
import requests
import textwrap
import pandas

l=[]
base_url="https://www.yachtworld.com/boats-for-sale/make-c&c/?page="
for page in range(1,10,1):
    print(base_url+str(page))
    r=requests.get(base_url+str(page))
    c=r.content
    soup=BeautifulSoup(c,"html.parser")
    all=soup.select('a[data-reporting-click-listing-type="standard listing"]')
    for item in all:
        d={}
        d["Sailboat"]=textwrap.shorten(item.find(class_="listing-card-title").text,width=50)
        if item.find("div",{"class":"price"}).text.replace("\n","").replace("*","").replace(" ","") == 'Call$(".currNote").hide()':
            d["Price"]=("0")
        else:
            d["Price"]=item.find(class_="price").text.replace("\n","").replace("*","").replace(" ","")
        d["Location"]=textwrap.shorten(item.find(class_="listing-card-location").text,width=50)
        d["Broker"]=textwrap.shorten(item.find(class_="listing-card-broker").text,width=50)
        length = item.find(class_="listing-card-length-year").text.split('/')[0]
        year = item.find(class_="listing-card-length-year").text.split('/')[1]
        d["length"]=textwrap.shorten(length,width=50)
        d["year"]=textwrap.shorten(year,width=50)

        d["url"]=textwrap.shorten(item['href'],width=1000)

        
        l.append(d)

df=pandas.DataFrame(l)
df.to_csv("multiple_brands.csv")
