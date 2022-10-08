from bs4 import BeautifulSoup
import requests
import textwrap
import pandas

l=[]
base_url="https://www.yachtworld.com/boats-for-sale/?makeModel=hunter&page="
for page in range(2,3,1):
    print(base_url+str(page))
    r=requests.get(base_url+str(page))
    c=r.content
    soup=BeautifulSoup(c,"html.parser")
    all=soup.find_all("div",{"class":"listing-card-information"})
    for item in all:
        d={}
        d["Sailboat"]=textwrap.shorten(item.find("div",{"class":"listing-card-title "}).text,width=50)
        if item.find("div",{"class":"price"}).text.replace("\n","").replace("*","").replace(" ","") == 'Call$(".currNote").hide()':
            d["Price"]=("Call for current price")
        else:
            d["Price"]=item.find("div",{"class":"price"}).text.replace("\n","").replace("*","").replace(" ","")
        d["Location"]=textwrap.shorten(item.find("div",{"class":"location"}).text,width=50)
        d["Broker"]=textwrap.shorten(item.find("div",{"class":"broker"}).text,width=50)
        l.append(d)

df=pandas.DataFrame(l)
df.to_csv("West Coast Sailboats for Sale From Yacht Finder.csv")
