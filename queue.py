
#############################				QUEUE 				################################



############## QUEUE IMPLEMENTATION USING LINKED LIST ##############

# Creating a Node
class Node:
	def __init__(self, data = None):
		self.data = data
		self.next = None


# Creating a Linked list
class LinkedList:
	def __init__(self, head = None):
		self.head = head

	# Inserting element at the end
	def insert_end(self, new_element):
		if self.head:
			current = self.head
			while current.next:
				current = current.next
			current.next = new_element

		else:
			self.head = new_element

	# Deleting first element
	def delete_first(self):
		if self.head:
			deleted_item = self.head
			self.head = self.head.next
			return deleted_item

		else:
			return None
			print("Empty list")

# Creating a queue
class Queue:
	def __init__(self, head = None):
		self.ll = LinkedList(head)

	# Inserting element in a queue
	def enqueue(self, new_element):
		self.ll.insert_end(new_element)

	# Deleting the first entered element
	def dequeue(self):
		return self.ll.delete_first()

### CHECK ###
q = Queue()

q.enqueue(Node(4))
q.enqueue(Node(3))
q.enqueue(Node(2))
q.enqueue(Node(1))

print("Queue implementation using Linked list")

# Should print 4
print(q.dequeue().data)
# Should print 3
print(q.dequeue().data)
# Should print 2
print(q.dequeue().data)
# Should print 1
print(q.dequeue().data)




############# STACK IMPLEMENTATION USING LISTS ##############

queue = []

# Performs enqueue action 
queue.append(4)
queue.append(3)
queue.append(2)
queue.append(1)

# Performs dequeue action
print("Stack implementation using list")

# Should print 4
print(queue.pop(0))
# Should print 3
print(queue.pop(0))
# Should print 2
print(queue.pop(0))
# Should print 1
print(queue.pop(0))
