import numpy as np
import matplotlib.pyplot as plt

class TrieNode:
    def __init__(self, c=""):
        self.c = c
        self.children = {}
        self.end = False

    def set_inorder(self, val = [0]):
        children = list(self.children.values())
        mid = len(children)//2
        for i in range(mid):
            children[i].set_inorder(val)
        self.x = val[0]
        val[0] += 1
        for i in range(mid, len(children)):
            children[i].set_inorder(val)
    
    def plot(self, y = 0):
        x1, y1 = self.x, y
        sz = 40
        c = 'k'
        if self.end:
            sz = 100
            c = 'r'
        plt.scatter(x1, y1, sz, c)
        plt.text(x1+0.3, y1+0.1, self.c)
        for c in self.children:
            x2, y2 = self.children[c].x, y-1
            plt.plot([x1, x2], [y1, y2])
            self.children[c].plot(y-1)
            
    def gather_words(self, words, prefix):
        """
        List of words and prefix of the string we've built so far
        """
        if self.end:
            words.append(prefix)
            # Recusicely branch out to children
            for key, value in self.children.items():
                self.children[key].gather_words(words, prefix + key)
        
        

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add_word(self, s):
        node = self.root
        for i in range(len(s)):
            c = s[i]
            if c in node.children:
                node = node.children[c]
            else:
                # Not there, make a new node
                new_node = TreiNode(c)
                node.children = new_node
                node = new_node
        node.end = True            

    def __contains__(self, s):
        node = self.root
        
        contains = True
        i = 0
        while i < len(s) and contains:
            c = s[i]
            if c in node.children:
                node = node.children[c]
                i += 1
            else:
                contains = False
        if contains and not node.end:
            contains = False
        return contains
    
    def get_words(self, s):
        
        """
        Collect all words that have s as a prefix
        """
        words = []
        
        node = self.root
        contains = True
        i = 0
        while i < len(s) and contains:
            c = s[i]
            if c in node.children:
                node = node.children[c]
                i += 1
            else:
                contains = False
        if contains:
            node.gather_words(words, s)
        return words
        

    def plot(self):
        self.root.set_inorder()
        self.root.plot()
        plt.axis("off")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        