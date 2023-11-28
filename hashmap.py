#build the initial map
#use a linked list approach to chain the elements which are hashed at the same index
#implement the necessary functions

#    Main Author(s): Rigels Hasani
#    Main Reviewer(s):

# If you are doing chaining for collision resolution, 
# copy your code from a1 into a1_partb.py and uncomment the next line
from LinkedLists.LL import LinkedList

class HashTable:

	# You cannot change the function prototypes below.  Other than that
	# how you implement the class is your choice as long as it is a hash table

	def __init__(self, cap=32):
		self.list = [None] * cap
		self.cap = cap
		self.total = 0
	#create a function to calc LF if LF goes over 0.7, call rebalancing function
	#create function for rebalancing
	def insert(self,key, value):

		if(self.search(key) is not None):
			return False
		idx = abs(hash(key) % self.cap)
		if(self.list[idx] is None):
			self.list[idx] = LinkedList()
		self.list[idx].push_front([key, value])
		self.total= self.total + 1
		return True
	
	def search(self, key):
		idx = abs(hash(key) % self.cap)
		if(self.list[idx] == None):
			return None
		copy = self.list[idx].front
		# self.list[idx] is the Linked list. 
		#While traversing the list
		while(copy.next is not self.list[idx].back):
			if copy.next.data[0] == key:
				return copy.next.data[1] #return the value
			copy = copy.next
		return None

	def modify(self, key, value):
		if(self.search(key) is None):
			return False
		idx = hash(key) % self.cap
		copy = self.list[idx].front.next
		# self.list[idx] is the Linked list. 
		#While traversing the list
		while(copy is not self.list[idx].back):
			if copy.data[0] == key:
				#change the value
				copy.data[1] = value
				return True
			copy = copy.next
		return False

	def remove(self, key): 
		idx = hash(key) % self.cap
		copy = self.list[idx].front.next
		# self.list[idx] is the Linked list. 
		#While traversing the list
		while(copy is not self.list[idx].back):
			if copy.data[0] == key:
				copy.next.prev = copy.prev
				copy.prev.next = copy.next
			copy = copy.next
		return None
	
	# rm = self.front.next
# rm.next.prev = rm.prev
# rm.prev.next = rm.next


	def capacity(self):
		return self.cap

	def __len__(self):
		return self.total

	def display(self):
		for i in range(self.cap):
			if(self.list[i] is not None):
				print("Index " + str(i) + " has " + str(self.list[i]))

h1 = HashTable(10)
h1.insert("apple", 10)
h1.insert("banana", 20)
# h1.insert("orange", 99)
# h1.insert("pineapple", 88)
# h1.insert("mango", 23)
h1.display()
result = h1.search("blob")
print(result)
print("----------------")
#result = h1.search(1)
#print(result)
#h1.modify(1, 1000)
# h1.display()
# h1.remove(1)
# print("----------------")
# h1.display()


#1. get the list from the LL.
#2. take care of collisions