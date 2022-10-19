import requests 
from bs4 import BeautifulSoup 
 
response = requests.get("https://zenrows.com") 
soup = BeautifulSoup(response.content, "html.parser") 
 

 
datePublished = soup.find('meta', itemprop='datePublished') 
print(datePublished['content']) # 2014-01-09