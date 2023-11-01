import numpy as np
import matplotlib.pyplot as plt

class TreeNode(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.inorder_pos = 0
    
    def add(self, key):
        if key < self.key:
            if self.left:
                self.left.add(key)
            else:
                self.left = TreeNode(key)
        elif key > self.key:
            if self.right:
                self.right.add(key)
            else:
                self.right = TreeNode(key)
    
    def inorder(self, num, key_list):
        """
        Parameters
        ----------
        num: list
            List of a single element which keeps 
            track of the number I'm at
        """
        if self.left:
            self.left.inorder(num, key_list)
        self.inorder_pos = num[0]
        key_list.append(self.key)
        num[0] += 1
        if self.right:
            self.right.inorder(num, key_list)
    
    def draw(self, y):
        x = self.inorder_pos
        plt.scatter([x], [y], 50, 'k')
        plt.text(x+0.2, y, "{}".format(self.key))
        y_next = y-1
        if self.left:
            x_next = self.left.inorder_pos
            plt.plot([x, x_next], [y, y_next])
            self.left.draw(y_next)
        if self.right:
            x_next = self.right.inorder_pos
            plt.plot([x, x_next], [y, y_next])
            self.right.draw(y_next)

    def remove(self, node):
        if node > self.key and self.right:
            self.right = self.right.remove(node)
            return self
        elif node < self.key and self.left:
            self.left = self.left.remove(node)
            return self
        else:
            if self.left and self.right:
                # get the highest number in the left sub tree
                cursor = self.left
                while cursor.right:
                    cursor = cursor.right
                # replace the node we want to remove with that 
                self.key = cursor.key
                # remove the one we replaced with 
                self.left = self.left.remove(cursor.key)
                return self
            else:
                if self.left:
                    return self.left
                else: 
                    return self.right


        
        
class BinaryTree(object):
    def __init__(self):
        self.root = None
    
    def inorder(self):
        key_list = []
        if self.root:
            self.root.inorder([0], key_list)
        return key_list
    
    def draw(self):
        self.inorder()
        if self.root:
            self.root.draw(0)
    
    def add(self, key):
        if self.root:
            self.root.add(key)
        else:
            self.root = TreeNode(key)
    
    def remove(self, node):
        if self.root:
            self.root.remove(node)

def make_tree():
    T = BinaryTree()
    for val in [10, 7, 16, 3, 9, 11, 20, 14, 17, 13, 12, 6, 5, 17, 15, 4, 8]:
        T.add(val)
    return T

T = make_tree()
T.draw()

# |%%--%%| <SE4TZ2NKnr|ip52YOSxMb>
T.remove(10)
T.remove(16)
T.remove(7)
T.draw()

