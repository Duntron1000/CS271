#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 13:20:20 2023

@author: liambruhin
"""
import numpy as np
import math

mylist = np.random.randint(0, 100, 10)
mylist.sort()

def binarySearch(nums, goal):
    print("number searching for: ", goal)
    print("Sorted List: ", nums)
    print("indexes of^: ",np.arange(0,100,10))
    mid = len(nums) // 2
    for i in range(math.ceil(math.log(len(nums), 2))):        
        if goal == nums[mid]:
            return mid
        elif goal > mid:
            mid += mid // 2
        elif goal < mid:
            mid = (mid + len(nums)) // 2
            
index = binarySearch(mylist, np.random.choice(mylist))

print("index of the found number: ", index)
print(mylist[index])

