#finding median maintainence
from min_heap import min_heap
from max_heap import max_heap

class two_heap():
    def __init__(self,n):
        self.min_heap=min_heap(n)
        self.max_heap=max_heap(n)
        self.min_count=0
        self.max_count=0
        self.ele_count=0
    def balance(self):
        if(self.min_count-self.max_count>1):
            self.max_heap.insert(self.min_heap.pop())
            self.min_count-=1
            self.max_count+=1
        elif(self.max_count-self.min_count>1):
            self.min_heap.insert(self.max_heap.pop())
            self.min_count+=1
            self.max_count-=1
        else:
            pass
        
    def insert(self,element):
        if(element<=self.max_heap.tree[0]):
            self.max_heap.insert(element)
            self.max_count+=1
        else:
            self.min_heap.insert(element)
            self.min_count+=1
        self.balance()
        self.ele_count+=1
        
    def median(self):
        if(self.ele_count%2==0):
            med=int(self.ele_count/2)
        else:
            med=int((self.ele_count+1)/2)
        if(med==self.max_count):
            return self.max_heap.tree[0]
        else:
            return self.min_heap.tree[0]

f = open("C:/Users/Christopher Gomes/median.txt","r")
mm=two_heap(10000)
s=0
for x in f:
    mm.insert(int(x))
    s=s+mm.median()
    
print(s)  

