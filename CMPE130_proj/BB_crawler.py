import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

bb_page1 = 'https://www.bestbuy.com/site/searchpage.jsp?cp=1&searchType=search&_dyncharset=UTF-8&ks=960&sc=Global&list=y&usc=All%20Categories&type=page&id=pcat17071&iht=n&seeAll=&browsedCategory=pcmcat138500050001&st=categoryid%24pcmcat138500050001&qp=&sp=-displaydate%20skuidsaas'
bb_page2 = 'https://www.bestbuy.com/site/searchpage.jsp?cp=2&searchType=search&_dyncharset=UTF-8&ks=960&sc=Global&list=y&usc=All%20Categories&type=page&id=pcat17071&iht=n&seeAll=&browsedCategory=pcmcat138500050001&st=categoryid%24pcmcat138500050001&qp=&sp=-displaydate%20skuidsaas'
bb_page3 = 'https://www.bestbuy.com/site/searchpage.jsp?cp=3&searchType=search&_dyncharset=UTF-8&ks=960&sc=Global&list=y&usc=All%20Categories&type=page&id=pcat17071&iht=n&seeAll=&browsedCategory=pcmcat138500050001&st=categoryid%24pcmcat138500050001&qp=&sp=-displaydate%20skuidsaas'
bb_page4 = 'https://www.bestbuy.com/site/searchpage.jsp?cp=4&searchType=search&_dyncharset=UTF-8&ks=960&sc=Global&list=y&usc=All%20Categories&type=page&id=pcat17071&iht=n&seeAll=&browsedCategory=pcmcat138500050001&st=categoryid%24pcmcat138500050001&qp=&sp=-displaydate%20skuidsaas'
bb_page5 = 'https://www.bestbuy.com/site/searchpage.jsp?cp=5&searchType=search&_dyncharset=UTF-8&ks=960&sc=Global&list=y&usc=All%20Categories&type=page&id=pcat17071&iht=n&seeAll=&browsedCategory=pcmcat138500050001&st=categoryid%24pcmcat138500050001&qp=&sp=-displaydate%20skuidsaas'

#opening up connection, grabbing the page using urllib
uClient1 = uReq(bb_page1)
uClient2 = uReq(bb_page2)
uClient3 = uReq(bb_page3)
uClient4 = uReq(bb_page4)
uClient5 = uReq(bb_page5)
page_html1 = uClient1.read()
page_html2 = uClient2.read()
page_html3 = uClient3.read()
page_html4 = uClient4.read()
page_html5 = uClient5.read()
uClient1.close()
uClient2.close()
uClient3.close()
uClient4.close()
uClient5.close()
#html parsing
page_soup1 = soup(page_html1, "html.parser")
page_soup2 = soup(page_html2, "html.parser")
page_soup3 = soup(page_html3, "html.parser")
page_soup4 = soup(page_html4, "html.parser")
page_soup5 = soup(page_html5, "html.parser")

#grabs each product
items1 = page_soup1.findAll("div", {"class":"list-item"})
items2 = page_soup2.findAll("div", {"class":"list-item"})
items3 = page_soup3.findAll("div", {"class":"list-item"})
items4 = page_soup4.findAll("div", {"class":"list-item"})
items5 = page_soup5.findAll("div", {"class":"list-item"})

'''
filename = "bestbuy2.csv"
f = open(filename, "w")
headers = " brand, product_name\n"
f.write(headers)
f.write("")
'''

for item in items1:
    product = item["data-title"]
    price = item["data-price"]

    print("Product:" + product)
    print("Price: $" + price)
    #f.write(product + "," + price + "\n\n")

for item in items2:
    product = item["data-title"]
    price = item["data-price"]

    print("Product:" + product)
    print("Price: $" + price)
   # f.write(product + "," + price + "\n\n")

for item in items3:
    product = item["data-title"]
    price = item["data-price"]

    print("Product:" + product)
    print("Price: $" + price)
    #f.write(product + "," + price + "\n\n")

for item in items4:
    product = item["data-title"]
    price = item["data-price"]

    print("Product:" + product)
    print("Price: $" + price)
   # f.write(product + "," + price + "\n\n")

for item in items5:
    product = item["data-title"]
    price = item["data-price"]

    print("Product:" + product)
    print("Price: $" + price)
'''
    f.write(product + "," + price + "\n\n")

f.close()
'''
