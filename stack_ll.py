############## STACK IMPLEMENTATION USING LINKED LIST ##############

# Creating a node
class Node:
	def __init__(self, data = None):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self, head = None):
		self.head = head

	# Inserting element in the beginning
	def insert_begin(self, new_element):
		if self.head:
			new_element.next = self.head
			self.head = new_element

		else:
			self.head = new_element

	def delete_first(self):
		if self.head:
			deleted_item = self.head
			self.head = sel############## STACK IMPLEMENTATION USING LINKED LIST ##############

# Creating a node
class Node:
	def __init__(self, data = None):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self, head = None):
		self.head = head

	# Inserting element in the beginning
	def insert_begin(self, new_element):
		if self.head:
			new_element.next = self.head
			self.head = new_element

		else:
			self.head = new_element

	def delete_first(self):
		if self.head:
			deleted_item = self.head
			self.head = self.head.next
			return deleted_item

		else:
			return None

class Stack:
	def __init__(self, top = None):
		self.ll = LinkedList(top)

	def push(self, new_element):
		self.ll.insert_begin(new_element)

	def pop(self):
		return self.ll.delete_first()


### CHECK ###
st = Stack()
st.push(Node(4))
st.push(Node(3))
st.push(Node(2))
st.push(Node(1))

# Should print 1
print(st.pop().data)
# Should print 2
print(st.pop().data)
# Should print 3
print(st.pop().data)
# Should print 4
print(st.pop().data)
# Should print None
print(st.pop())

f.head.next
			return deleted_item

		else:
			return None

class Stack:
	def __init__(self, top = None):
		self.ll = LinkedList(top)

	def push(self, new_element):
		self.ll.insert_begin(new_element)

	def pop(self):
		return self.ll.delete_first()


### CHECK ###
st = Stack()
st.push(Node(4))
st.push(Node(3))
st.push(Node(2))
st.push(Node(1))

# Should print 1
print(st.pop().data)
# Should print 2
print(st.pop().data)
# Should print 3
print(st.pop().data)
# Should print 4
print(st.pop().data)
# Should print None
print(st.pop())

