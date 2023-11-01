#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 11:31:21 2023

@author: liambruhin
"""

class Node:
    def __init__(self, obj):
        """
        Parameters
        ----------
        obj: object
            Some object we want to store in this container
        """
        self.obj = obj
        self.next = None # Like "null" in C++
        
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_first(self, obj):
        new_node = Node(obj)
        new_node.next = self.head
        self.head = new_node
    
    def add_last(self, obj):
        new_node = Node(obj)
        if not self.head:
            # If the head is None (nothing is in the list yet)
            self.head = new_node
        else:
            # Loop through until I get to the end
            cursor = self.head
            while cursor.next:
                # while cursor's next is not None
                cursor = cursor.next
            cursor.next = new_node
        
    def contains(self, obj):
        cursor = self.head
        found = False
        while not found and cursor: # If cursor is None, this is false
            if cursor.obj == obj:
                found = True
            cursor = cursor.next
        return found
    
    def print_elements(self):
        cursor = self.head
        while cursor: # If cursor is None, this is false
            print(cursor.obj, end="-->")
            cursor = cursor.next
            
        
mylist = LinkedList()
mylist.add_last("Camila")
mylist.add_last("Journi")
mylist.add_last("Tre")
mylist.add_last("Levi")

mylist.print_elements()
print("\n")
print(mylist.contains("Levi"))
print(mylist.contains("Pedro"))