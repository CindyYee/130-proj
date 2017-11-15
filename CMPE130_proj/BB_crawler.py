# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 23:05:09 2017

@author: Cindy Yee
References:
    https://www.analyticsvidhya.com/blog/2015/10/beginner-guide-web-scraping-beautiful-soup-python/
    https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe
    https://www.crummy.com/software/BeautifulSoup/bs4/doc/
"""

import urllib2; #used to query a website
from bs4 import BeautifulSoup #used to parse the data returned from the website

#url link
BB_pg1="https://www.bestbuy.com/site/searchpage.jsp?cp=1&searchType=search&_dyncharset=UTF-8&ks=960&sc=Global&list=y&usc=All%20Categories&type=page&id=pcat17071&iht=n&seeAll=&browsedCategory=pcmcat138500050001&st=categoryid%24pcmcat138500050001&qp=&sp=-displaydate%20skuidsaas";

#Query the website and return the html to the variable 'page1'
page1 = urllib2.urlopen(BB_pg1);

# parse the html using beautiful soup and store in variable `pg1Soup`
pg1Soup = BeautifulSoup(page1);

#print pg1Soup.prettify(); #this prints everything from the html "Inspect"

  
#data-name='HP ...'    is an attribute
#soup.find() only outputs 1, unlike find_all
pg1_items=pg1Soup.find_all("div", {"class" : "list-item"});
itemnum=0;
for div in pg1_items:
    itemnum=itemnum+1;#Check how many items was extracted
   # print div;   #print everything from the #<div class="list-item"   .....</div>

print itemnum; #YES! itemnum=24 after the for loop, which corresponds to the BB listing 1-24
                #Have not checked whether all of them have the right data, but 1st 3 div does

