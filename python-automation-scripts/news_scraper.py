import requests
from bs4 import BeautifulSoup
url = "https://news.ycombinator.com/"
news=requests.get(url)
print(news.status_code)
soup=BeautifulSoup(news.text,"html.parser")
print(soup.prettify())
print(soup.title.text)
News=soup.find_all("span",class_='titleline')
for headline in News:
    New=headline.find("a")
    print(f"HEADLINE : {New.get_text()}")
    print("-"*60)
    print(f"LINK : {New["href"]}")
    print("*"*60)