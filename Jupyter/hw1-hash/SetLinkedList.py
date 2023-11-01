class node:
    def __init__(self, key):
        self.key = key
        self.next = None
        
class linked_list:
    def __init__(self):
        self.head = None
        
    def add_first(self, obj):
        new_node = node(obj)
        new_node.next = self.head
        self.head = new_node
    
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
        
    def __str__(self):
        """
        Like java's toString()
        """
        if self.head == None:
            return "[]"
        
        node = self.head
        s = ""
        while node:
            s += str(node.key) + " ==> "
            node = node.next
        return s