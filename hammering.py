#implementing clustering on hammering code
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
        
f = open("C:/Users/Christopher Gomes/clus.txt","r")
flag=True

n=0
bits=0

file_check={}
file_read=[]

for x in f:
    if(flag==True):
        flag=False
        try:
            n,bits=x.split()
            n=int(n)
            bits=int(bits)
        except:
            print(x)
            break
    else:
        x=list(x.split())
        x=''.join(x)
        x=int(x)
        file_read.append(x)
        file_check[x]=1
        
