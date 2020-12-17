class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.previous=None
class DLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def append(self,data):
        new=node(data)
        if(self.tail==None):
            self.tail=self.head=new
            self.tail.prev=None
            self.tail.next=None
        else:
            self.tail.next=new
            new.prev=self.tail
            self.tail=new
            self.tail.next=None
    def disp(self):
        cur=self.head
        while cur:
            print(cur.data)
            cur=cur.next
    def addatbegin(self,data):
        cur=self.head
        new=node(data)
        new.next=cur
        cur.prev=new
        self.head=new

d=DLinkedList()
n=int(input("size:"))
for i in range(n):
    k=int(input())
    d.append(k)
p=int(input("ele:"))
d.addatbegin(p)
d.disp()
