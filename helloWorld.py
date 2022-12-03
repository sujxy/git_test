
class Node :
    def __init__(self,data):
        self.data = data
        self.next = None

class queue :
    def __init__(self):
        self.head = None
        self.tail = None 

    def __iter__(self):
        node = self.head 
        while node :
            yield node
            node = node.next 

    def __str__(self) :
        values =[str(x.data) for x in self]  
        return "<-".join(values)

    def enq(self,val) :
        newNode = Node(val)        
        if self.head == None :
            self.head = newNode
            self.tail = newNode 

        else :
            self.tail.next = newNode
            self.tail = newNode

    def deq(self):
        if self.head == None :
            print("queue is empty")
            return
        else :
            val = self.head 
            self.head = self.head.next 
            return val 

q1 = queue()
q1.enq(9)                
q1.enq(4)                
q1.enq(1)                
q1.enq(8)  
q1.deq()   
print(q1)           