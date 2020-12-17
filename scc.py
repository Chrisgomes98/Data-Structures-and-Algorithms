import pandas as pd
import sys 
sys.setrecursionlimit(5*10**3) 
class SCC:
    def __init__(self):
        '''self.n = int(input())
        self.nE = int(input())'''
        df= pd.read_csv("scc.csv")
        V1=list(df['v1'])
        V2=list(df['v2'])
        #self.e = []
        #self.rev = []
        i = 0
        self.n = 875714
        self.a = []
        self.arev = []
        self.finishStack = []
        for i in range(self.n+1):
            self.a.append([])
            self.arev.append([])
        self.visited = [0]*(self.n+1)
        for i in range(len(V1)):
            #u,v = map(int,x.split())
            u = V1[i]
            v = V2[i]
            self.a[u].append(v)
            self.arev[v].append(u)
            #self.e.append([u,v])
            #self.rev.append([v,u])
        #print(self.e)
        #print(self.rev)
        '''print(self.a)
        print(self.arev)'''
        for i in range(self.n,0,-1):
            '''print(self.visited)
            print(self.finishStack)'''
            if self.visited[i]==1:
                continue
            else:
                self.DFS(self.a,i)
        '''print(self.visited)
        print(self.finishStack)'''
        self.visited = [0]*(self.n+1)
        '''print(self.visited)'''
        self.Scc = []
        N = self.n
        while(N>0):
            i = self.finishStack.pop()
            if self.visited[i]==0:
                self.Scc.append([i])
                self.DFS2(self.arev,i)
            N = N - 1

    def DFS(self,G,i):
        '''print("DFS of",G,i)'''
        #print(self.visited)
        #print(self.finishStack)
        self.visited[i] = 1
        for v in self.a[i]:
            '''print("v=",v)'''
            if self.visited[v]==0:
                self.DFS(G,v)
        '''print("visited=",self.visited)'''
        self.finishStack.append(i)
        '''print("finishStack=",self.finishStack)
        print("DFS ended of",G,i)'''
        
    def DFS2(self,G,i):
        #print("DFS of",G,i)
        #print(self.visited)
        #print(self.finishStack)
        self.visited[i] = 1
        for v in self.arev[i]:
            #print("v=",v)
            if self.visited[v]==0:
                self.Scc[-1].append(v)
                self.DFS2(G,v)
        #rint("visited=",self.visited)
        #rint("Scc=",self.Scc)
        #rint("DFS ended of",G,i)
scc = SCC()