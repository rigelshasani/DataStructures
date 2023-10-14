class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


head =  Node(4)
nodeB = Node(2)
nodeC = Node(3)
nodeD = Node(10)
nodeE = Node(15)

head.next  = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE

#traverse the list going through all the elements until we find where the next is null

def countNodes(head):
    count = 1
    while(head.next != None):
        current = head.next.data
        head = head.next
        count += 1
    print(count)
countNodes(head)
    