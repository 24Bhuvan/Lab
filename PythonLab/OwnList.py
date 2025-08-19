import ctypes
# operations:
# creating list
# len function 
# printing
# append
# fetching using index
# pop 
# clear
# finding
# inserting
# deleting
# removing

class MyList:
    def __init__(self):
        self.size=1
        self.n=0
        self.A= self.makearray(self.size)

    def makearray(self,capacity):
        #creates a ctype array with size capacity (static,referential)
        return (capacity*ctypes.py_object)()

    def __len__(self):
        #For using len function
        return self.n

    def append(self,item):
        if self.n==self.size:
            #Resize
            self.resize(self.size*2)
        self.A[self.n]=item
        self.n+=1

    def resize(self,new_capactiy):
        #for dynamic array
        B=self.makearray(new_capactiy)
        self.size=new_capactiy
        for i in range(self.n):
            B[i]=self.A[i]
        self.A=B 

    def __str__(self):
        #for printing the list
        result=""
        for i in range(self.n):
            result = result+str(self.A[i])+","
        return "["+result[:-1]+"]"

    def __getitem__(self,index):
        #for indexing
        if self.n>index>=0:
            return self.A[index]
        else :
            return 'IndexError-Index out of range'

    def pop(self):
        if self.n==0:
            return 'Empty List'
        print(self.A[self.n-1])
        self.n=self.n-1

    def clear(self):
        self.n=0
        self.size=1

    def index(self,item):
            for i in range (self.n):
                if self.A[i] == item:
                    return i
            return 'ValueError'

    def insert(self,pos,item):
        if self.size==self.n :
            self.resize(self.size*2)
        for i in range(self.n,pos,-1):
            self.A[i]=self.A[i-1]
        self.A[pos]=item
        self.n+=1

    def __delitem__(self,pos):
        for i in range(pos,self.n-1):
            self.A[i]=self.A[i+1]
        self.n=self.n-1

    def remove(self,item):
        pos=self.index(item)
        if type(pos)==int:
            self.__delitem__(pos)
        else:
            return pos
if __name__=="__main__":
    pass