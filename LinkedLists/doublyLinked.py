class DoublyLinked:

    class Node:
        def __init__(self, data, next = None, prev = None):
            self.data = data
            self.next = next
            self.prev = prev

        def get_data(self):
            return self.data

        def get_next(self):
            return self.next

        def get_previous(self):
            return self.prev


    def __init__(self, data = None):
        self.data = data
        self.front = None
        self.back = None

    def get_front(self):
        return self.front

    def get_back(self):
        return self.back

    def push_front(self, data):
        node = self.Node(data)

        if self.front is None:
            self.front = node
            self.back = node
        else:
            node.next = self.front
            self.front.prev = node
            self.front = node

    def push_back(self,data):
        node = self.Node(data)

        if self.back is None:
            self.back = node
            self.front = node
        else:
            node.prev = self.back
            self.back.next = node
            self.back = node

    def pop_front(self):
        if self.is_empty():
            raise IndexError('pop_front() used on empty list')
        else:
            data = self.front.data
            self.front = self.front.next
            if self.front:
                self.front.prev = None
            else:
                self.back = None
            return data

    def pop_back(self):
        if self.is_empty():
            raise IndexError('pop_back() used on empty list')
        
        else:
            data = self.back.data
            self.back = self.back.prev

            if self.back:
                self.back.next = None
            else:
                self.front = None

            return data

    def is_empty(self):
        return self.front is None and self.back is None

    def insert_after(self, data, node):
        if node is None:
            self.push_front(data)
            return

        if node.next is None:
            self.push_back(data)
            return

        new_node = self.Node(data)
        new_node.prev = node

        if node.next:
            node.next.prev = new_node
            new_node.next = node.next

        node.next = new_node


    def search(self, data):
        if self.is_empty():
            return None

        current = self.front

        while current:
            if current.data == data:
                return current
            
            current = current.next

        return None

    def __len__(self):
        count = 0
        current = self.front
        
        while current:
            count += 1
            current = current.next
        return count

    def is_palindrome_rec(self, front, back):
        if front is None or back is None:
            return True

        if front.data == back.data:
            return self.is_palindrome_rec(front.next, back.prev)

        else:
            return False

    def is_palindrome(self):
        return self.is_palindrome_rec(self.front, self.back)
    
    def __str__(self):
        if self.is_empty():
            return ''
        if self.__len__() == 1:
            return str(self.front.data)
        copy = self.front
        list = []
        while(copy is not self.back.prev):
            list.append(copy.next.data)
            copy = copy.next
        return str(list)