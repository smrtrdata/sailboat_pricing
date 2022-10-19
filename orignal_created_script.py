from bs4 import BeautifulSoup
import requests
import textwrap
import pandas

def get_created_date(url) : 
        content = requests.get(url=url).text
        date = content.split('"date":{"created":"')[1]
        date = date.split('","')[0]
        date = date.split("T")[0]
        return date
l=[]
base_url="https://www.yachtworld.com/boats-for-sale/?makeModel=hunter&page="
for page in range(2,10,1):
    print(base_url+str(page))
    r=requests.get(base_url+str(page))
    c=r.content
    soup=BeautifulSoup(c,"html.parser")
    all=soup.select('a[data-reporting-click-listing-type="standard listing"]')
    for item in all:
        d={}
        d["Sailboat"]=textwrap.shorten(item.find(class_="listing-card-title").text,width=50)
        if item.find("div",{"class":"price"}).text.replace("\n","").replace("*","").replace(" ","") == 'Call$(".currNote").hide()':
            d["Price"]=("Call for current price")
        else:
            d["Price"]=item.find(class_="price").text.replace("\n","").replace("*","").replace(" ","")
        d["Location"]=textwrap.shorten(item.find(class_="listing-card-location").text,width=50)
        d["Broker"]=textwrap.shorten(item.find(class_="listing-card-broker").text,width=50)
        length = item.find(class_="listing-card-length-year").text.split('/')[0]
        year = item.find(class_="listing-card-length-year").text.split('/')[1]
        d["length"]=textwrap.shorten(length,width=50)
        d["year"]=textwrap.shorten(year,width=50)

        d["url"]=textwrap.shorten(item['href'],width=1000)

        date = get_created_date(d['url'])
        d["created_date"] = date
                
        l.append(d)

df=pandas.DataFrame(l)
df.to_csv("West Coast Sailboats for Sale From Yacht Finder.csv")
