import requests
import os
import time
import heapq    
import itertools
import csv

from bs4 import BeautifulSoup


class Article(object):
    def __init__(self, title=None, url=None, date=None):
        self.title=title;
        self.url=url;
        self.date=date;
    def __lt__(self,other):
        return (self.date < other.date);
    def __repr__(self):
        return ("Title: " + self.title + "\nDate: " + self.date + "\nURL: " + self.url + "\n");
#    def __str__(self):
#        return ("Title: " + self.title + "\nDate: " + self.date + "\nURL: " + self.url + "\n");
def printArticle(Article):
      print (Article.title, Article.url, Article.date);    
pq = []                         # list of entries arranged in a heap
entry_finder = {}               # mapping of tasks to entries
REMOVED = '<removed-task>'      # placeholder for a removed task
counter = itertools.count()     # unique sequence count

def add_task(task, priority=0):
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
        time.sleep(5);
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        news_boxes = soup.find_all('div', {'class': 'newsBox'})
        news_box = news_boxes[0]
        time.sleep(5);
        for news_box in news_boxes:
            title = news_box.div.a.h2.text
            date = news_box.div.time.text
            url = "https://www.laptopmag.com/" + news_box.div.a.get('href')
            print("Title: " + title + "\n"
                  "Date: " + date + "\n"
                  "URL: " + url + "\n")
            add_task(Article(title,date,url));
            time.sleep(1);

        page += 1

spider(1);

j=0;
for jL in pq:
    print(pq[j]);
    j=j+1;
