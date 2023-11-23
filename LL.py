class LinkedList:
    
    class Node:
        #initialize the node, it has 3 attributes, 2 are defaulted
        def __init__(self, data, next = None, prev = None):
            self.data = data
            self.next = next
            self.prev = prev
    #initialize the linked list, it has a front and a back
    def __init__(self):
        self.front = self.Node(None)
        self.back  = self.Node(None, None, self.front)
        self.front.next = self.back
    
    def push_front(self, data):
        #makes a new node using the data, and inserts it to the front of the linked list?
        nn = LinkedList.Node(data, self.front.next, self.front)
        self.front.next.prev = nn
        self.front.next = nn
    
    def pop_front(self):
        #if the LL is not empty
        if self.front.next is not self.back:
            rm = self.front.next
            self.front.next = self.front.next.next
            self.front.next.next.prev = self.front
            del rm
    def __str__(self):
        copy = self.front
        list = []
        while(copy is not self.back.prev):
            list.append(copy.next.data)
            copy = copy.next
        return str(list)

# ll1 = LinkedList()
# ll1.push_front(10)
# ll1.push_front(20)
# print(ll1)

# rm = self.front.next
# rm.next.prev = rm.prev
# rm.prev.next = rm.next
# self.front.next.next.prev = self.front.next.prev
# self.front.next.prev.next = self.front.next.next

