#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 12:04:34 2023

@author: liambruhin
"""

import numpy as np
import math

mylist = np.random.randint(0, 100, 10)
print("Random list : ", mylist)
mylist.sort()

def binarySearch(nums, goal):
    print("Number Im searching for: ", goal)
    print("Sorted list: ", mylist)
    print("indexes of^: ",np.arange(0,100,10))
    lost = 0
    for i in range(math.ceil(math.log(len(nums), 2))):
        mid = len(nums) // 2
        if nums[mid] == goal:
            return mid + lost
        elif goal > nums[mid]:
            lost += mid
            nums = nums[mid:]
        elif goal < nums[mid]:
            nums = nums[0:mid]

index = binarySearch(mylist, np.random.choice(mylist))
print("Index of the found number: ",  index)
print(mylist[index])
    
    