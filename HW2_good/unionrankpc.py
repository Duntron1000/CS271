class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}
        self._operations = 0
        self._calls = 0
    
    def root(self, i):
        if self.parent[i] != i:
            self._operations += 1
            self.parent[i] = self.root(self.parent[i]) # Path compression
        return self.parent[i]

        
    def union(self, i, j):
        self._calls += 1
        root_i = self.root(i)
        root_j = self.root(j)
        if root_i != root_j:
            if self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
                self._operations += 1
               
            elif self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
                self._operations += 1
                
            elif self.rank[root_i] == self.rank[root_j]:
                self.parent[root_j] = root_i
                self._operations += 1
                self.rank[root_i] += 1
            
       
    def find(self, i, j):
        self._calls += 1
        return self.root(i) == self.root(j)
    
    def makeset(self, obj):
        self.rank[obj] = 0
        self.parent[obj] = obj
        