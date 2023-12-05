from Queue import Queue

class BST:
    class Node:
        def __init__(self, data=None, left = None, right = None):
            self.data  = data
            self.left  = left
            self.right = right
    def __init__(self):
        self.root = None

    #this function calls the r_search function, passing in the data, and the root as arguments
    #this is going to get the recursive search going
    def recursive_search(self, data):
        return self.r_search(data, self.root)    
    
    def r_search(self, data, subtree):
        #if there is no root, there can be no search
        if subtree is None:
            return None
        #if there is a root, we need to decide which subtree to search
        if data > subtree.data:
            subtree = subtree.right
            return self.r_search(data, subtree)
        elif data < subtree.data:
            subtree = subtree.left
            return self.r_search(data, subtree)
        else:
            return subtree
        
    def recursive_insert(self, data):
        self.root = self.ins(data, self.root)
    
    def ins(self, data, subtree):
        if subtree is None:
            subtree = BST.Node(data)
            return subtree
        #if the argument is smaller subtree's data, then we move left
        elif data < subtree.data:
            subtree.left = self.ins(data, subtree.left)
            return subtree
        else:
            subtree.right = self.ins(data, subtree.right)
            return subtree
        
    #inorder tree traversal: printing all values from smallest to biggest, recursively
    #we will visit each node ONCE, and will pass only the root as argument
    #base case is an empty tree, where we do nothing and exit
    #if tree isnt empty, we print all values smaller than the current node(left subtree), then the current node,
    #then the values bigger(right subtree)

    def print_inorder(self, subtree):
        if subtree is not None:
            self.print_inorder(subtree.left)
            print(subtree.data, end = " ")
            self.print_inorder(subtree.right)
        
    def print(self):
        self.print_inorder(self.root)
        print("")

    #preorder is the exact same, but line 55 is replaced with  54


    def print_between(self, subtree, min, max):
        if subtree is not None:
            self.print_inorder(subtree.left)
            if(subtree.data > 5 or subtree.data < 25):
                print(subtree.data, end = " ")
            self.print_inorder(subtree.right)
        
    def print(self):
        self.print_between(self.root)
        print("")
