# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 23:33:48 2019

@author: ganze
"""

def print_full_name_mg(first, last):
    print(last + ", " + first)
    
first_name_1 = "민건"
last_name_1 = "김" 
first_name_2 = "하영"
last_name_2 = "신" 

print_full_name_mg(first_name_1, last_name_1)
print_full_name_mg(first_name_2, last_name_2)


def print_full_name(first_name, last_name):
    print("%s, %s" % (last_name, first_name))
    
print_full_name("민건", "김")

#########################################################

def calculate_change(payment, cost):
    wallet = [50000, 10000, 5000, 1000]
    bill = []
    for i in range(4):
        bill[i] = int((payment - cost) / wallet[i])
    print("%d원 지폐: %d장" % (str(wallet[0]), str(bill[0])))
    print("%d원 지폐: %d장" % (str(wallet[1]), str(bill[1])))
    print("%d원 지폐: %d장" % (str(wallet[2]), str(bill[2])))
    print("%d원 지폐: %d장" % (str(wallet[3]), str(bill[3])))
          
calculate_change(100000, 33000)    
#################################################################
def calculate_change(payment, cost):
    change = payment - cost
    fifty_thousand = int((change) / 50000)
    fifty_change = change % 50000
    ten_thousand = int((fifty_change) / 10000)
    ten_change = fifty_change % 10000
    five_thousand = int((ten_change) / 5000)
    five_change = ten_change % 5000
    one_thousand = int((five_change) / 1000)
    one_change = five_change % 1000
    print("%d원 지폐: %d장" % (50000, fifty_thousand))
    print("%d원 지폐: %d장" % (10000, ten_thousand))
    print("%d원 지폐: %d장" % (5000, five_thousand))
    print("%d원 지폐: %d장" % (1000, one_thousand))

calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)