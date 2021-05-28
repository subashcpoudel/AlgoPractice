from typing import ByteString

#Node Class
class Node(object):
    def __init__(self, val):
        self.val=val
        self.next=None

    def get_data(self):
        return self.val

    def set_data(self, data):
        self.val=data

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next=next

#List Class
class LinkedList(object):
    def __init__(self, head=None):
        self.head=head
        self.count=0

    def get_count(self):
        return self.count

    def insert(self, data):
        new_node=Node(data)
        new_node.set_next(self.head)
        self.head=new_node
        self.count+=1
    
    def find(self,val):
        item=self.head
        pos=0
        while(item!=None):
            if item.get_data() == val:
                return pos
            else:
                pos+=1
                item=item.get_next()
        return None

    def deleteAt(self,at):
        #If Delete at is larger than List count deletes last node
        item=self.head
        cur=Node()
        pos=0
        while(at!=pos):
            cur=item
            item=item.get_next()
            pos+=1
        cur.set_next=item.get_next
        self.count-=1
    
    def dump(self):
        item=self.head
        pos=0
        while(item!=None):
            print("Node pos & value:",pos,item.val)
            pos+=1
            item=item.get_next()

#Initialize Lists and Start Program
def initprog(a,b):
    a=LinkedList()
    b=LinkedList()
    progstart(a,b)
    
#Actual Start Program
def progstart(a,b):
    x=input("\n Select Linked list: a or b? or c to destroy both ")
    if(x=="a"):
        compstart(a,b)
    elif(x=="b"):
        compstart(b,a)
    elif(x=="c"):
        initprog(a,b)
    else:
        progstart(a,b)

#Actual Computations for Program
def compstart(list,another):
    x=input("\n Select Insert-1, Find-2, DeleteAt-3, Dump-4,Start-5 ")
    if(x=="1"):
        data=input("\n Data to insert ")
        list.insert(data)
        print("\n Data inserted New count = ",list.get_count())
    elif(x=="2"):
        data=input("Find what? ")
        print("\n Found at",list.find(data))
    elif(x=="3"):
        data=input("Delete At? ")
        Print("\n Data Deleted New Count = ",list.get_count())
    elif(x=="4"):
        list.dump()
    elif(x=="5"):
        progstart(list,another)
    compstart(list, another)

#Code Initial Functions     
a=LinkedList()
b=LinkedList()
progstart(a,b)