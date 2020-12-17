#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the prims function below.
#prims algo
#prims algo
class min_heap_prims():
    def __init__(self,n):
        self.tree=[]
        for i in range(n):
            self.tree.append([99999,'s','d'])
        self.current_node=0
        self.epos=0
        self.n=n
        
    def insert(self,element):
        if(self.isempty()):
            self.tree[0]=element
            self.current_node=0
        else:
            #element_inserted
            self.epos=0
            if(self.isleftpos(self.current_node)):
                self.tree[2*self.current_node+1]=element
                self.epos=2*self.current_node+1
            elif(self.isrightpos(self.current_node)):
                self.tree[2*self.current_node+2]=element
                self.epos=2*self.current_node+2
            else:
                self.current_node=self.current_node+1
                self.tree[2*self.current_node+1]=element
                self.epos=2*self.current_node+1
            #element_check_position
            epos=self.epos
            ppos=int((epos-1)/2)
            while(ppos>=0 and self.tree[ppos][0]>self.tree[epos][0]):
                temp=self.tree[ppos]
                self.tree[ppos]=self.tree[epos]
                self.tree[epos]=temp
                epos=ppos
                ppos=int((epos-1)/2)
                
    def display(self):
        print(self.tree)
                         
    def pop(self):
        if(self.isempty()):
            return 
        else:
            top=self.tree[0]
            if(self.tree[2*self.current_node+2]!=[99999,'s','d']):
                self.tree[0]=self.tree[2*self.current_node+2]
                self.tree[2*self.current_node+2]=[99999,'s','d']
            else:
                self.tree[0]=self.tree[2*self.current_node+1]
                self.tree[2*self.current_node+1]=[99999,'s','d']
                self.current_node=self.current_node-1
                
            flag=True
            ppos=0
            lc=1
            rc=2
            while((ppos<self.n) and (self.tree[ppos][0]>self.tree[lc][0] or self.tree[ppos][0]>self.tree[rc][0])):
                if(self.tree[lc][0]<self.tree[rc][0]):
                    temp=self.tree[ppos]
                    self.tree[ppos]=self.tree[lc]
                    self.tree[lc]=temp
                    ppos=2*ppos+1
                else:
                    temp=self.tree[ppos]
                    self.tree[ppos]=self.tree[rc]
                    self.tree[rc]=temp
                    ppos=2*ppos+2

                lc=2*ppos+1
                rc=2*ppos+2

                if(lc>=self.n):
                    break
                elif(rc>=self.n):
                    if(self.tree[ppos][0]>self.tree[lc][0]):
                        temp=self.tree[ppos]
                        self.tree[ppos]=self.tree[lc]
                        self.tree[lc]=temp
                    break
                elif(lc>=self.n and rc>=self.n):
                    break
                else:
                    pass
                
            return top
            
    
    def isleftpos(self,node):
        if(self.tree[2*node+1][0]==99999):
            return True
        else:
            return False
        
    def isrightpos(self,node):
        if(self.tree[2*node+2][0]==99999):
            return True
        else:
            return False
            
    def isempty(self):
        if(self.tree[0][0]==99999):
            return True
        else:
            return False
        
    def has_element(self):
        if(self.isempty()):
            return False
        else:
            return True


print("THIS IS THE IMPLEMENTATION OF PRIM'S ALGORITHM")

n,m=input().split()
n=int(n)
m=int(m)
heap=min_heap_prims(2*m)
graph={}
visited={}

for i in range(m):
    ele=list(map(int,input().split()))
    x=ele[0]
    y=ele[1]
    cost=ele[2]
    try:
        graph[x].append([cost,y])
    except:
        graph[x]=[[cost,y]]
    try:
        graph[y].append([cost,x])
    except:
        graph[y]=[[cost,x]]

#print(graph)


for i in graph[1]:
    heap.insert(i)

visited[1]=1
visited_count=1

total=0

#heap.display()

    
while(visited_count!=n):
    ele=heap.pop()
    if(ele==None):
        break
    else:
        vertex=ele[1]
        cost=ele[0]
        try:
            visited[vertex]==1
        except:
            visited[vertex]=1
            total=total+cost
            visited_count+=1
            for i in graph[vertex]:
                heap.insert(i)
        


print(total)
