#implementatino of kruskal's algorithm
class union_find():
    def __init__(self,n):
        self.n=n
        self.parent_of=[-1]*(n+1)
        self.child_of={}
        for i in range(n+1):
            self.child_of[i]=[i]
            
    def union(self,x,y):
        x,size_x=self.find(x)
        y,size_y=self.find(y)
                
        if(size_y>size_x):
            x,y=y,x
            
        for i in self.child_of[y]:
            self.parent_of[i]=x
            self.parent_of[x]=self.parent_of[x]-1
        self.child_of[x]=self.child_of[x]+self.child_of[y]
        del self.child_of[y]

    def find(self,i):
        if(self.parent_of[i]<0):
            return i,abs(self.parent_of[i])
        else:
            return self.parent_of[i],abs(self.parent_of[self.parent_of[i]])
        
    def display(self):
        print(self.child_of)
        print(self.parent_of)
        
        
f = open("C:/Users/Christopher Gomes/kruskal.txt","r")
flag=True
heap=[]

for x in f:
    if(flag==True):
        n=int(x)
        flag=False
    else:
        ele=list(map(int,x.split()))
        heap.append(ele)
        
heap.sort(key = lambda x: x[2])



i=0
k=4
clusters=n
unif=union_find(n)

while(clusters>k-1):
    ele=heap[i]
    x=ele[0]
    y=ele[1]
    if(unif.find(x)==unif.find(y)):
        pass
    else:
        unif.union(x,y)
        clusters=clusters-1
    i=i+1
    
print(heap[i-1])
#106