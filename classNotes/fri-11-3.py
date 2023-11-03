import numpy as np
import matplotlib.pyplot as plt

class TreeNode(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 0
        self.inorder_pos = 0

    # change to keep the tree balancee - tree rotations 
    # Case1 : height(node.left) = height(node.right) + 2
    #   - Case1a: height(node.left.left) > height(node.left.right) 
    #       - height(node.left.left) = h + 1
    #       - clockwise rotation about node makes both left and right height of h + 1
    #
    #   - Case1b: height(node.left.left) < height(node.left.right)
    #       - more annoying because a rotation about node will not balance this
    #       - both of the childred of node.left.right have a hight of <= h
    #       - counter clockwise rotation about node.left makes height(node.left.left) > height (node.left.righ)
    #       - turns into case1a

    def add(self, key):
        ret = self
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

        # rebalance 

        #return


    def height(self):
        if self == None:
            return -1
        return 1 + max(self.left.height(), self.right.height())
    
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

    def height(self, node):
        return node.height()

def make_tree():
    T = BinaryTree()
    for val in [10, 7, 16, 3, 9, 11, 20, 14, 17, 13, 12, 6, 5, 17, 15, 4, 8]:
        T.add(val)
    return T

T = make_tree()
T.draw()
print(height(T.root))


