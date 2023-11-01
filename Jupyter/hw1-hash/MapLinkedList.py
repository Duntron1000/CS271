class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        
class Linked_List:
    def __init__(self):
        self.head = None
        self.len = 0
        
    def add_first(self, obj, value):
        new_node = Node(obj, value)
        new_node.next = self.head
        self.head = new_node
        self.len += 1
  
    def __getitem__(self, key):
        if not key in self:
            raise KeyError("Cannot get an item that is not icluded in the list")
        cursor = self.head
        found = False
        while not found and cursor:
            if cursor.key == key:
                return cursor.value
            
            cursor = cursor.next
               
    def __setitem__(self, key, value):
        if not key in self:
            raise KeyError("Cannot set an item that is not icluded in the list")
        cursor = self.head
        found = False
        while not found and cursor:
            if cursor.key == key:
                cursor.value = value
                return
            cursor = cursor.next

    
    def __contains__(self, obj):
        cursor = self.head
        found = False
        while not found and cursor: # If cursor is None, this is false
            if cursor.key == obj:
                found = True
            cursor = cursor.next
        return found
    
    def remove(self, obj):
        removed = False
        if not obj in self:
            raise KeyError("Cannot remove an object that is not included in the list")
        cursor = self.head
        
        #speacial case if obj is the first element
        if cursor.key == obj:
            self.head = cursor.next
            
        while not removed and cursor.next:
            if cursor.next.key == obj:
                cursor.next = cursor.next.next
                removed = True
            else:
                cursor = cursor.next
    def __len__(self):
        return self.len
        
    def __str__(self):
        """
        Like java's toString()
        """
        if self.head == None:
            return "[]"
        
        node = self.head
        s = ""
        while node:
            s += str(node.key) + ": " +  str(node.value)  + " ==> "
            node = node.next
        return s