from MapLinkedList import *
import numpy as np

class HashMap:
    def __init__(self,num_buckets, load_factor):
        self.load_factor = load_factor
        self.num_buckets = num_buckets
        self.buckets = np.empty(self.num_buckets, dtype=Linked_List)
        self.len = 0
        for i in range(self.num_buckets):
            self.buckets[i] = Linked_List()
            
    def __contains__(self, key):
        bucket = hash(key) % self.num_buckets
        return key in self.buckets[bucket]
    
    def rebalance(self):
        newBuckets = np.empty(self.num_buckets * 2, dtype=Linked_List)
        keys = self.keys()
        values = []
        for key in keys:
            values.append(self[key])
        for i in range(self.num_buckets * 2):
            newBuckets[i] = Linked_List()

        self.num_buckets *= 2
        self.buckets = newBuckets
        
        for i, key in enumerate(keys):
            self[key] = values[i]
    
    def __setitem__(self, key, value):
        bucket = hash(key) % self.num_buckets
        if not key in self:
            self.buckets[bucket].add_first(key, value)
            self.len += 1
        else:
            self.buckets[bucket][key] = value
            
        if self.len > (self.load_factor * self.num_buckets):
            self.rebalance()
            
    def __getitem__(self, key):
        bucket = hash(key) % self.num_buckets
        return self.buckets[bucket][key]
    
    def __delitem__(self, key):
        bucket = hash(key) % self.num_buckets
        self.buckets[bucket].remove(key)
        self.len -= 1
                 
    def __str__(self):
        s = ""
        for i in range(len(self.buckets) - 1):
            s += self.buckets[i].__str__() 
            s += "\n"
        return s
    
    def __len__(self):
        return self.len
    
    def keys(self):
        keys = []
        for i in range(self.num_buckets):
            cursor = self.buckets[i].head
            while cursor:
                keys.append(cursor.key)
                cursor = cursor.next
        return keys
    
              
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        