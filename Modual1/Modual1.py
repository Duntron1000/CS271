#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 11:27:50 2023

@author: liambruhin
"""

# Arithmetic Expressions
import math
def print_bus_vans(bus_capacity, van_capacity, num_people):
    """
    Compute the bus and van capacity
    Parameters
    ----------
    bus_capacity: int
     Number of people a bus can hold
    van_capacity: int
     Number of people a van can hold
    num_people: int
     Number of people on the trip
    """
    ## TODO: Change these two variables to reflect the actual
    ## number needed
    num_busses = math.floor(num_people / bus_capacity)
    num_people = num_people%bus_capacity
    num_vans = math.ceil(num_people / van_capacity)
    
    print("{} Buses, {} Vans".format(num_busses, num_vans), end='.')