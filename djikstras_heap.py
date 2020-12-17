import sys
#min_heap_djikstras
class min_heap():
    def __init__(self,n):
        self.tree=[]
        self.default=[sys.maxsize,0]
        for i in range(n):
            self.tree.append(self.default)
        self.current_node=0
        self.epos=0
        self.n=n
        self.index={}
    
    def create_heap(self,arr):
        for i in arr:
            self.insert(i)        

    def insert(self,element):
        if(self.isempty()):
            self.tree[0]=element
            self.current_node=0
            self.index[tuple(element)]=0
        else:
            #element_inserted
            self.epos=0
            if(self.isleftpos(self.current_node)):
                self.tree[2*self.current_node+1]=element
                self.index[tuple(element)]=2*self.current_node+1
                self.epos=2*self.current_node+1
            elif(self.isrightpos(self.current_node)):
                self.tree[2*self.current_node+2]=element
                self.epos=2*self.current_node+2
                self.index[tuple(element)]=2*self.current_node+2
            else:
                self.current_node=self.current_node+1
                self.tree[2*self.current_node+1]=element
                self.index[tuple(element)]=2*self.current_node+1
                self.epos=2*self.current_node+1
            #element_check_position
            epos=self.epos
            ppos=int((epos-1)/2)
            while(ppos>=0 and self.tree[ppos][0]>self.tree[epos][0]):
                temp=self.tree[ppos]
                
                self.index[tuple(self.tree[ppos])]=epos
                self.index[tuple(self.tree[epos])]=ppos
                
                self.tree[ppos]=self.tree[epos]
                self.tree[epos]=temp
                epos=ppos
                ppos=int((epos-1)/2)
                
    def display(self):
        print(self.tree)
        print(self.current_node)
        print(self.index)
    
        
    def pop_element(self,element):
        ind=self.index[tuple(element)]
        element=self.pop_mi(ind)
        return element
                         
    def pop_mi(self,i):
        if(self.isempty()):
            return 
        else:
            top=self.tree[i]
            if(i==2*self.current_node+2):
                self.tree[i]=self.default
                
            elif(i==2*self.current_node+1):
                if(self.tree[2*self.current_node+2]==self.default):
                    self.tree[i]=self.default
                    if(self.current_node>0):
                        self.current_node=self.current_node-1
                else:
                    self.tree[i]=self.tree[2*self.current_node+2]
                    self.index[tuple(self.tree[2*self.current_node+2])]=i
                    self.tree[2*self.current_node+2]=self.default        
            else:
                if(self.tree[2*self.current_node+2]!=self.default):
                    self.tree[i]=self.tree[2*self.current_node+2]
                    self.index[tuple(self.tree[2*self.current_node+2])]=i
                    self.tree[2*self.current_node+2]=self.default
                else:
                    self.tree[i]=self.tree[2*self.current_node+1]
                    self.index[tuple(self.tree[2*self.current_node+1])]=i
                    self.tree[2*self.current_node+1]=self.default
                    if(self.current_node>0):
                        self.current_node=self.current_node-1

                flag=True
                ppos=i
                lc=1
                rc=2
                while((ppos<self.n) and (self.tree[ppos][0]>self.tree[lc][0] or self.tree[ppos][0]>self.tree[rc][0])):
                    if(self.tree[lc][0]<self.tree[rc][0]):
                        self.index[tuple(self.tree[ppos])]=lc
                        self.index[tuple(self.tree[lc])]=ppos
                        temp=self.tree[ppos]
                        self.tree[ppos]=self.tree[lc]
                        self.tree[lc]=temp
                        ppos=2*ppos+1
                    else:
                        self.index[tuple(self.tree[ppos])]=rc
                        self.index[tuple(self.tree[rc])]=ppos
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
                            self.index[tuple(self.tree[ppos])]=lc
                            self.index[tuple(self.tree[lc])]=ppos
                            temp=self.tree[ppos]
                            self.tree[ppos]=self.tree[lc]
                            self.tree[lc]=temp
                        break
                    elif(lc>=self.n and rc>=self.n):
                        break
                    else:
                        pass
        del self.index[tuple(top)]
        return top
    
    def pop(self):
        if(self.isempty()):
            return 
        else:
            top=self.pop_mi(0)
            return top
            
    
    def isleftpos(self,node):
        if(self.tree[2*node+1][0]==self.default[0]):
            return True
        else:
            return False
        
    def isrightpos(self,node):
        if(self.tree[2*node+2][0]==self.default[0]):
            return True
        else:
            return False
            
    def isempty(self):
        if(self.tree[0][0]==self.default[0]):
            return True
        else:
            return False
        
    def has_element(self):
        if(self.isempty()):
            return False
        else:
            return True
