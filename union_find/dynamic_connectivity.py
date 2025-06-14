from abc import ABC, abstractmethod


class UF(ABC):
    def __init__(self, N):
        self.total_nodes = N

    @abstractmethod
    def union(self, p, q):
        pass

    def connected(self, p, q):
        pass




class QuickFind(UF):
    def __init__(self, N):
        super().__init__(N)
        self.nodes = [0] * N
        for i in range(N):
            self.nodes[i] = i
        
     
    def  root(self,p):
        while p!= self.nodes[p]:
            p = self.nodes[p]
        return p
        
           
    def union(self, p, q):
        int i = self.root(p)
        j = self.root(q)
        self.nodes[i] = j
    
    
    def connected(self, p, q):
        return self.root(p) == self.root(q)
    
    


if __name__ == "__main__":
    pass
      
      