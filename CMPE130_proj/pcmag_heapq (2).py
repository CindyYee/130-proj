import requests
import os
import time
import heapq    
import itertools
import csv
from datetime import datetime,date

from bs4 import BeautifulSoup


class Article(object):
    def __init__(self, title=None, date=None, url=None):
        self.title=title;
        self.date=date;
        self.url=url;
    def __lt__(self,other):
        return (self.date < other.date);
    def __repr__(self):
        return ("Title: " + self.title + "\nDate: " + self.date.strftime("%m/%d/%y") + "\nURL: " + self.url);
#        return ("Title: " + self.title + "\nDate: " + str(self.date) + "\nURL: " + self.url);

		
pq = []                         # list of entries arranged in a heap
entry_finder = {}               # mapping of tasks to entries
REMOVED = '<removed-task>'      # placeholder for a removed task
counter = itertools.count()     # unique sequence count

def add_task(task):
    'Add a new task or update the priority of an existing task'
    if task in entry_finder:
        remove_task(task)
    count = next(counter);
#    entry = [priority, count, task]
    entry = [count, task]
    entry_finder[task] = entry
    heapq.heappush(pq, entry)

def remove_task(task):
    'Mark an existing task as REMOVED.  Raise KeyError if not found.'
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED

def pop_task():
    'Remove and return the lowest priority task. Raise KeyError if empty.'
    while pq:
#        priority, count, task = heapq.heappop(pq)
        count, task = heapq.heappop(pq)
        if task is not REMOVED:
            del entry_finder[task]
            return task
    raise KeyError('pop from an empty priority queue')
    


headers = {
    'User-Agent': 'test',
    'From': "donghwe90@gmail.com"
}


def spider(max_pages):
    page = 1
    while page <= max_pages:
        url = "https://www.laptopmag.com/latest/" + str(page)
        source_code = requests.get(url, headers=headers)
        time.sleep(1);
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        news_boxes = soup.find_all('div', {'class': 'newsBox'})
        news_box = news_boxes[0]
        time.sleep(1);
        for news_box in news_boxes:
            title = news_box.div.a.h2.text
            date = news_box.div.time.text
            
#            date = date[:date.rindex(" ")+5]
            dt=datetime.strptime(date,"%B %d, %Y ");
#            dt = dt[:dt.rindex(" ")+5] #unconverted data remains:
            url = "https://www.laptopmag.com/" + news_box.div.a.get('href')
            # print("Title: " + title + "\n"
                  # "Date: " + date + "\n"
                  # "URL: " + url + "\n")
            add_task(Article(title,dt,url));
            time.sleep(1);

        page += 1

spider(1);

j=0;
for jL in pq:
	print(pq[j]);
	print(); #empty line
	j=j+1;
