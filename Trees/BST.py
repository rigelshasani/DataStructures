from Queue import Queue

class BST:
    class Node:
        # Node's init function
        def __init__(self,data=None,left=None,right=None):
            self.data = data
            self.left = left
            self.right = right

    #BST's init function
    def __init__(self):
        self.root = None

    def insert(self, data):
        #if the tree is empty
        if self.root is None:
            self.root = BST.Node(data)
        else:
            curr = self.root
            inserted = False

            while not inserted:
                #if the data we want to insert is smaller than the data at current
                if data < curr.data:
                    #if it has a left child
                    if curr.left is not None:
                        #traverse to it
                        curr = curr.left
                    else:
                        curr.left = BST.Node(data)
                        inserted = True
                else:
                    if curr.right is not None:
                        curr = curr.right
                    else:
                        curr.right = BST.Node(data)
                        inserted = True
    
    def search(self, data):
        curr = self.root
        while curr is not None:
            if data < curr.data:
                curr = curr.left
            elif data > curr.data:
                curr = curr.right
            else:
                return curr
        return None
            
    
    def inorder_print(self):
        pass

    def pre_order_print(self):
        pass

    def breadth_first_print(self):
        the_nodes = Queue()

        if self.root is not None:
            the_nodes.enqueue(self.root)

        while not the_nodes.is_empty():
            curr = the_nodes.dequeue()

            if curr.left:
                the_nodes.enqueue(curr.left)
            if curr.right:
                the_nodes.enqueue(curr.right)
            print(curr.data, end=" ")


tree1 = BST()
tree1.insert(35)
tree1.insert(30)
tree1.insert(40)
tree1.insert(5)
tree1.insert(15)
tree1.insert(10)
tree1.insert(25)
tree1.insert(20)
tree1.breadth_first_print()
print("")