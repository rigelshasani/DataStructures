#build the initial map
#use a linked list approach to chain the elements which are hashed at the same index
#implement the necessary functions

#    Main Author(s): Rigels Hasani
#    Main Reviewer(s):

# If you are doing chaining for collision resolution, 
# copy your code from a1 into a1_partb.py and uncomment the next line
from LL import LinkedList

class HashTable:

	# You cannot change the function prototypes below.  Other than that
	# how you implement the class is your choice as long as it is a hash table

	def __init__(self, cap=32):
		self.list = [None] * cap
		self.cap = cap
	def insert(self,key, value):
		idx = hash(key) % self.cap
		if(self.list[idx] is None):
			self.list[idx] = LinkedList()
		self.list[idx].push_front([key, value])

	def modify(self, key, value):
		pass

	def remove(self, key):
		pass

	def search(self, key):
		pass

	def capacity(self):
		pass

	def __len__(self):
		pass

	def display(self):
		for i in range(self.cap):
			if(self.list[i] is not None):
				print("Index " + str(i) + " has " + str(self.list[i]))

h1 = HashTable(10)
h1.insert(5, 10)
h1.insert(15, 20)
h1.insert(1, 99)
h1.insert(11, 88)
h1.insert(4, 23)
h1.insert(7, 48)
h1.insert(15, 24)
h1.display()

#1. get the list from the LL.
#2. take care of collisions