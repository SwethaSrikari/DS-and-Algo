#############################			 BINARY SEARCH TREE 		###################################

# Creating a NODE
class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

# No duplicates
def insert_bst(root,element):
	if root is None:
		root = element

	if element.data < root.data:
		if root.left is None:
			root.left = element
		else:
			insert_bst(root.left,element)

	if element.data > root.data:
		if root.right is None:
			root.right = element
		else:
			insert_bst(root.right,element)

def  inorder(root):
	if root:
		inorder(root.left)
		print(root.data)
		inorder(root.right)

def preorder(root):
	if root:
		print(root.data)
		preorder(root.left)
		preorder(root.right)

# Returns the remaining tree from that value
def search(root,value):
	if root:
		if root.data == value:
			preorder(root)
		if value < root.data:
			search(root.left,value)
		if value > root.data:
			search(root.right,value)
		else:
			return
	else:
		return 

def minValRightTree(root):
	while root.left:
		root = root.left
	return root

def deletion(root,value):
	if root is None:
		return root
	
	if value < root.data:
		print('l',root.data)
		root.left = deletion(root.left,value)
	elif value > root.data:
		print('r',root.data)
		root.right = deletion(root.right,value)

	else:
		if root.right is None:
			temp = root.left
			root = None
			print(temp,'rn')
			return temp

		elif root.left is None:
			temp = root.right
			root = None
			print(temp,'ln')
			return temp

		
		temp = minValRightTree(root.right)
		print(temp.data,'2c')

		root.data = temp.data



		root.right = deletion(root.right,temp.data)

	return root
	
	


	
	
	

root = Node(4)
# insert_bst(root,Node())
insert_bst(root,Node(2))
insert_bst(root,Node(7))
insert_bst(root,Node(1))
insert_bst(root,Node(3))

# print("Inorder")
# inorder(root)
print("Preorder")
preorder(root)
# print("Search 2")
# search(root,2)
print("Delete 4")
deletion(root,4)
preorder(root)



