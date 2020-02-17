import requests
from bs4 import BeautifulSoup as soup
import csv

myurl = "http://books.toscrape.com/"

r = requests.get(myurl).text

my_soup = soup(r,'lxml')

csv_file = open("C:\\Users\\tyres\\Desktop\Python Projects\\webscrape1.csv",'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Book Title',"Price","Availabilty"])



for article in my_soup.find_all("article"):
    product = article.find("h3").text
    print(product)

    product_p = article.find("div",class_="product_price")
    product_price = product_p.find("p",class_="price_color").text
    product_stock = product_p.find("p",class_="instock availability").text.strip()
    print(product_price)
    print(product_stock)
    print()

    csv_writer.writerow([product,product_price,product_stock])

csv_file.close()

