from SetLinkedList import*
    
class HashSet:
    
    def __init__(self, n_buckets):
        self.num_buckets = n_buckets
        self.buckets = []
        self.length = 0
        
        for i in range(self.num_buckets):
            self.buckets.append(linked_list())
        
    def __contains__(self, obj):
        bucket = hash(obj) % self.num_buckets
        return obj in self.buckets[bucket]
        
    
    def add(self,obj):
        bucket = hash(obj) % self.num_buckets
        if not obj in self:
            self.buckets[bucket].add_first(obj)
            self.length += 1
    
    def remove(self, obj):
        if obj in self:
            bucket = hash(obj) % self.num_buckets
            self.buckets[bucket].remove(obj)
            self.length -=1
        else:
            raise KeyError("Item {} not in set!".format(key))
        
    
    def __len__(self):
        return self.length
    
    def keys(self):
        keys = []
        for i in range(self.num_buckets):
            cursor = self.buckets[i].head
            while cursor:
                keys.append(cursor.key)
                cursor = cursor.next
        return keys
    
    def __str__(self):
        s = ""
        for i in range(self.num_buckets):
            s += self.buckets[i].__str__() 
            s += "\n"
        
        return s
        
    
    
  





















    