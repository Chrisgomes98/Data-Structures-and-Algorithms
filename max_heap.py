class max_heap():
    def __init__(self,n):
        self.tree=[-99999]*n
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
            while(ppos>=0 and self.tree[ppos]<self.tree[epos]):
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
            if(self.tree[2*self.current_node+2]!=-99999):
                self.tree[0]=self.tree[2*self.current_node+2]
                self.tree[2*self.current_node+2]=-99999
            else:
                self.tree[0]=self.tree[2*self.current_node+1]
                self.tree[2*self.current_node+1]=-99999
                if(self.current_node>0):
                    self.current_node=self.current_node-1
                
            flag=True
            ppos=0
            lc=1
            rc=2
            while((ppos<self.n) and (self.tree[ppos]<self.tree[lc] or self.tree[ppos]<self.tree[rc])):
                if(self.tree[lc]>self.tree[rc]):
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
            return top
            
    
    def isleftpos(self,node):
        if(self.tree[2*node+1]==-99999):
            return True
        else:
            return False
        
    def isrightpos(self,node):
        if(self.tree[2*node+2]==-99999):
            return True
        else:
            return False
            
    def isempty(self):
        if(self.tree[0]==-99999):
            return True
        else:
            return False
    