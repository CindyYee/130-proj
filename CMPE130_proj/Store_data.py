# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 17:46:20 2017

@author: KuroX
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 20:51:09 2017
@author: Cindy Yee
"""
class Laptop(object):
    def __init__(self, name=None, model=None, price=None, release_date=None):
        self.name=name;
        self.model=model;
        self.price=price;
        self.release_date=release_date;
    def __cmp__(self, other):               #used so we can sort into heaps
        return cmp(self.price, other.price)

CompanyA=[];

#after paring, everything will be treated like strings
CompanyA.append(Laptop("Dell intel", "DELL123", float("399.99"), "6-12-2017"));
CompanyA.append(Laptop("HP amd", "HP123", float("499.99"), "7-4-2017"));
CompanyA.append(Laptop("Lenovo sss", "LVNVNV123", float("299.99"), "7-4-2014"));

print "\nOriginal:"
i=0;
for iL in CompanyA:
    print "name:", CompanyA[i].name, "model:", CompanyA[i].model;
    print "\tprice:",CompanyA[i].price, "release date:", CompanyA[i].release_date;
    i=i+1;

##compare price
#if CompanyA[0].price<CompanyA[1].price:
#    print "1st cost less than 2nd"
#if CompanyA[1].price<CompanyA[2].price:
#    print "2nd cost less than 3rd"
#else:
#    print "2nd cost more than 3rd"    
    
print "\nHeapified "
    
import heapq

heapq.heapify(CompanyA);
j=0;
for jL in CompanyA:
   print "name:", CompanyA[j].name, "model:", CompanyA[j].model;
   print "\tprice:",CompanyA[j].price, "release date:", CompanyA[j].release_date;
   j=j+1; 