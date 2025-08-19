class Node:
    #Creating linked list Nodes
    def __init__(self,value):
        self.data = value
        self.next= None
        
class LinkedList:
    def __init__(self):
        self.head= None
        #length of the list of current object is called next
        self.n=0

    def len(self):
        return self.n
    
    def insert_head(self,value):
        #create new node
        new_node=Node(value)
        #creating connection
        new_node.next=self.head 
        #Reassigning head to point new node
        self.head=new_node
        #Increment n 
        self.n+=1

    def append(self,value):
        new_node=Node(value)

        cur=self.head

        while cur.next!=None:
            cur=cur.next
        
        cur.next=new_node

    def __str__(self):
        cur = self.head
        result=""
        while cur!=None:
            result=result+str(cur.data)+"->"
            cur=cur.next
        return result[:-2]
    
if __name__=="__main__":
    l=LinkedList()
    l.insert_head(3)
    l.insert_head(2)
    l.insert_head(1)
    l.append(4)
    print(l)