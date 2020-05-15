############## Implementation of Linked Lists ###############
import ipdb


# Creating a node
class Node:
	def __init__(self,data = None):
		self.data = data
		self.next = None


# Creating a linked List
class LinkedList:
	def __init__(self, head = None):
		self.head = head

	# Traversing a list or Printing each value in the Linked List
	def traverse(self):
		if self.head:
			current = self.head
			while current:
				print(current.data)
				current = current.next

		else:
			print("List empty. Add items to print")

	# Inserting element in the beginning of the list
	def insert_begin(self,value):
		if self.head:
			value.next = self.head
			self.head = value

		else:
			self.head = value


	# Inserting element at the end of the list
	def insert_end(self,value):
		if self.head:
			current = self.head
			while current.next:
				current = current.next
			current.next = value

		else:
			self.head = value

	# Inserting element at specified position
	def insert_position(self,value,position):
		if position == 1:
			self.insert_begin(value)

		if self.head:
			if position == 2:
				value.next = self.head.next
				self.head.next = value

			if position > 2:
				current = self.head
				for i in range(position - 2):
					current = current.next
				value.next = current.next
				current.next = value


	# Deleting first element of the list
	def delete_first(self):
		if self.head:
			self.head = self.head.next

		else:
			print("List is empty. Fill it first")


	# Deleting last element of the list
	def delete_last(self):
		if self.head:
			current = self.head
			while current.next:
				temp = current
				current = current.next
			temp.next = None

		else:
			print("List is already empty. Can not delete more")


	# Deleting a value the first time it appears in the list
	def del_val_once(self,value):
		if self.head:
			if self.head.data == value:
				self.head = self.head.next

			else:
				current = self.head
				while current.data != value and current.next != None:
					temp = current
					current = current.next
				temp.next = temp.next.next

		else:
			print("Empty list")


	# Deleting a value whenever it appears in the list
	def del_val(self,value):
		if self.head:
			if self.head.data == value:
				self.head = self.head.next

			current = self.head
			temp = current
			while current.next:
				if current.data == value:
					temp.next = temp.next.next
					current = current.next
				else:
					temp = current
					current = current.next
			if current.data == value:
					temp.next = temp.next.next
					current = current.next

		else:
			print("Empty list")


	# Deleting alternate elements in the list
	def del_alternate(self):
		if self.head:
			current = self.head
			
			while current:
				if current.next:
					temp = current
					current = current.next.next
					temp.next = current					
				else:
					break

		else:
			print("Empty list")

	# Place alternate values in a seperate list
	def two_lists(self):
		if self.head:
			l2 = LinkedList()
			current = self.head
			
			while current:
				if current.next:
					temp = current
					l2.insert_end(Node(temp.next.data))
					current = current.next.next
					temp.next = current					
				else:
					break

			l2.traverse()
		else:
			print("Empty list")


	# Reverse a Linked list by creating another list
	def reverse_newlist(self):
		if self.head:
			rl = LinkedList()
			current = self.head
			while current.next:
				rl.insert_begin(Node(current.data))
				current = current.next
			rl.insert_begin(Node(current.data))
			rl.traverse()
		else:
			print("Empty list")


	# Reverse a Linked list
	def reverse(self):
		prev = None
		current = self.head
		while current:
			temp = current.next
			current.next = prev
			prev = current
			current = temp
			self.head = prev








### CHECK ###
element1 = Node(1)
ll = LinkedList(element1)

# Should print 1
print("head",ll.head.data)

element2 = Node(2)
ll.head.next = element2

# Should print 2
print("next",ll.head.next.data)

# ll.traverse()

ll.insert_begin(Node(3))
# Should print 312
# ll.traverse()

ll.insert_end(Node(4))
# Should print 3124
# ll.traverse()

ll.insert_position(Node(5),1)
# # Should print 53124
# # ll.traverse()

ll.insert_position(Node(4),2)
# # Should print 543124
# # ll.traverse()

ll.insert_position(Node(2),4)
ll.insert_position(Node(3),7)
#Should print 54321234
# ll.traverse()
 
# ll.delete_first()
# # # Should print 4321234
# # # ll.traverse()

# ll.delete_last()
# # # Should print 432123
# # # ll.traverse()

# ll.del_val_once(4)
# # # Should print 42123
# # # ll.traverse()

# ll.del_val(3)
# # # # Should print 212
# # ll.traverse()

# ll.del_alternate()
# Should print 22
# ll.traverse()

# ll.two_lists()
# ll.traverse()

ll.reverse()
# Should print 54321
ll.traverse()