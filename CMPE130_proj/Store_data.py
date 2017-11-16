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

CompanyA=[];

#after paring, everything will be treated like strings
CompanyA.append(Laptop("Dell intel", "DELL123", float("399.99"), "6-12-2017"));
CompanyA.append(Laptop("HP amd", "HP123", float("499.99"), "7-4-2017"));
CompanyA.append(Laptop("Lenovo sss", "LVNVNV123", float("299.99"), "7-4-2014"));
print "name:", CompanyA[0].name, "model:", CompanyA[0].model;
print "price:",CompanyA[0].price, "release date:", CompanyA[0].release_date;

#compare price
if CompanyA[0].price<CompanyA[1].price:
    print "1st cost less than 2nd"
if CompanyA[1].price<CompanyA[2].price:
    print "2nd cost less than 3rd"
else:
    print "2nd cost more than 3rd"    
