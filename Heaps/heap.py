class MinHeap:
    #When a MinHeap is instantiated, it is passed a python list that may be empty. 
    #You may assume that any values in the list are comparable using 
    #comparison operators such as <, <=, >=, >, == and !=. 
    #This initializer will initialize a heap using this array.
    def __init__(self, arr = []):
        self.size = 0
        self.arr = [] 
        #changes size
        for i in arr:
            self.insert(i)

    def insert(self, element):
        #add element at the end
        self.arr = self.arr + [element]
        #change size
        self.size += 1
        self.heapifyUp()

    def heapifyUp(self):
        index = self.size-1
        #while the index HAS a parent AND the parent is bigger than me
        while(self.hasParent(index) and (self.parent(index) > self.arr[index])):
            #swap them
            self.swap(self.getParentIndex(index), index)
            #update index
            index = self.getParentIndex(index)


    #helper functions
    def getLeftChildIndex(self, parentIndex):
        return 2 * parentIndex + 1
    def getRightChildIndex(self, parentIndex):
        return 2 * parentIndex + 2
    def getParentIndex(self, childIndex):
        return (childIndex-1) // 2
    
    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index) < self.size
    def hasRightChild(self, index):
        return self.getRightChildIndex(index) < self.size
    def hasParent(self, index):
        return self.getParentIndex(index) >= 0
    
    def leftChild(self, index):
        return self.arr[self.getLeftChildIndex(index)]
    def rightChild(self, index):
        return self.arr[self.getRightChildIndex(index)]
    def parent(self, index):
        return self.arr[self.getParentIndex(index)]
    
    def swap(self, i1, i2):
        temp = self.arr[i1]
        self.arr[i1] = self.arr[i2]
        self.arr[i2] = temp

    def get_min(self):
        if(self.is_empty() != True):
            return self.arr[0]
        return None
    
    def is_empty(self):
            if self.size == 0:
                return True
            return False

    def __len__(self):
        return self.size
    
    def peek(self):
        if self.is_empty() != True:
            return self.arr[0]

    def popper(self):
        if self.is_empty() != True: 
            # temp = []
            # #loop through the array till the last element, and exclude it
            # for i in range(0, self.size-1):
            #     temp = temp + [self.arr[i]]
            # #assign this temporary array to our array
            # self.arr = temp
            # #decrease size manually
            self.size -= 1
            
    
    def extract_min(self):
        if(self.is_empty() != True):
            item = self.arr[0]
            self.arr[0] = self.arr[self.size-1]
            self.popper()
            self.heapifyDown()
            return item
    

    def heapifyDown(self):
        index = 0
        #while the index has a left child
        while(self.hasLeftChild(index)):
            #assign a variable to that left child
            smallerChildIndex = self.getLeftChildIndex(index)
            #check if it has a right child and if its smaller than the left child
            if self.hasRightChild(index) and self.rightChild(index) < self.leftChild(index):
                #assign the variable to the smallest of the children
                smallerChildIndex = self.getRightChildIndex(index)
            #if the element is smaller than the smallest child, break
            if self.arr[index] < self.arr[smallerChildIndex]:
                break
            #if not that means we need to swap
            else:
                self.swap(index, smallerChildIndex)
            #update the index and keep checking
            index = smallerChildIndex
        

heap1 = MinHeap([5, 3, 2, 1])
print(heap1.arr)
    

