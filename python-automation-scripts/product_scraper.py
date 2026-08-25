import requests
from bs4 import BeautifulSoup
url = "https://books.toscrape.com/"
pro=requests.get(url)
soup=BeautifulSoup(pro.text,"html.parser")
print(soup.prettify())
print(soup.title.text)
products=soup.find_all("article",class_='product_pod')
for product in products :
    book=product.find("h3").find("a")
    print(book['title'])
    
    link=product.find("a")
    print(link["href"])
    price=product.find("p",class_="price_color")
    print(price.text)
    rating=product.find("p")
    print(rating['class'][1])
    
    print("="*80)