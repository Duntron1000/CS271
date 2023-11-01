#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 12:20:00 2023

@author: liambruhin
"""

import numpy as np
np.random.seed(0)
arr = sorted(np.random.randint(0, 100, 70))



def binary_search(nums, target, low = 0, high = -1):
    if high == -1:
        high = len(arr) - 1
        
    
    # find the middle index
    mid = (low + high) // 2
    
    
    # find the value at the middle index
    testnum = nums[mid]
    
        
    #base case
    returner = -1
    if target == testnum:
        returner = mid
    elif low >= high:
        returner = -1
    elif target > testnum:
        returner = binary_search(nums, target, mid + 1, high)
    elif target < testnum:
        returner = binary_search(nums, target, low, mid - 1)
    return returner
    
    
    
    

def check_for_every_number(array, high):
    for i in range(high):
        temp = binary_search(array, i)
        if temp != -1:
            print(i, temp, arr[temp])
        else:
            print(i,temp)
    

