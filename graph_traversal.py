class Graph:
	def __init__(self):
		"""
		Create a dictionary to store graph using adjacency lists
		"""
		self.graph = dict()

	def add_nodes_edges(self, n, e):
		"""
		Add nodes and edges to the graph
		: param n: node (integer or name or character)
		: param e: list of nodes connected to n (list of integers or names or characters) 
		"""
		self.graph[n] = e
		return self.graph

	def BFS_traversal(self, graph, start):
		"""
		Breadth first search of a graph
		: param graph: Graph
		: param start: starting node (to start search from that node)
		Returns all nodes from the starting node using breadth first search
		"""
		queue = []
		visited = {k: False for k in self.graph.keys()}

		# Stores the nodes in the order of traversal
		# and the first node in the queue is visited first
		queue.append(start)
		print('queue', queue)

		while queue:
			start = queue.pop(0)
			print(start, end = " ")
			
			for e in graph[start]:
				if not visited[e]:
					queue.append(e)
					visited[e] = True
			print('queue', queue)

	def DFS_traversal(self, graph, start):
		"""
		Depth first search of a graph
		: param graph: Graph
		: param start: starting node (to start search from that node)
		Returns all nodes from the starting node using depth first search
		"""
		stack = []
		visited = {k: False for k in self.graph.keys()}

		# Stores the nodes in the order of traversal
		# and the last node in the stack is visited first
		stack.append(start)
		print('stack', stack)

		while stack:
			start = stack.pop()
			print(start, end = " ")
			
			# Since the last node is visited first in a stack,
			# store the neighbors in a reverse order so that the 
			# first neighbor is stored last but visited first along with
			# its neighbors
			for e in graph[start][::-1]:
				if not visited[e]:
					stack.append(e)
					visited[e] = True
			print('stack', stack)

	def BFS_find(self, graph, start, key):
		"""
		BFS to find a key in the graph
		: param graph: Graph
		: param start: starting node (to start search from that node)
		: param key: the node to be found

		Returns all the nodes searched before finding the node
		"""
		queue = []
		visited = {k: False for k in self.graph.keys()}

		# Stores the nodes in the order of traversal
		# and the first node in the queue is visited first
		queue.append(start)

		while queue and start != key:
			start = queue.pop(0)
			print(start, end = " ")
			
			for e in graph[start]:
				if not visited[e]:
					queue.append(e)
					visited[e] = True

	def DFS_find(self, graph, start, key):
		"""
		Depth first search to find an element in the graph
		: param graph: Graph
		: param start: starting node (to start search from that node)
		: param key: the node to find
		Returns all the nodes searched before finding the node
		"""
		stack = []
		visited = {k: False for k in self.graph.keys()}

		# Stores the nodes in the order of traversal
		# and the last node in the stack is visited first
		stack.append(start)

		while stack and start != key:
			start = stack.pop()
			print(start, end = " ")
			
			# Since the last node is visited first in a stack,
			# store the neighbors in a reverse order so that the 
			# first neighbor is stored last but visited first along with
			# its neighbors
			for e in graph[start][::-1]:
				if not visited[e]:
					stack.append(e)
					visited[e] = True



# Example 1
g = Graph()
g.add_nodes_edges('a', ['b', 'e', 'f'])
g.add_nodes_edges('b', ['c', 'd'])
g.add_nodes_edges('e', ['d', 'g'])
g.add_nodes_edges('f', [])
g.add_nodes_edges('c', [])
g.add_nodes_edges('d', [])
g.add_nodes_edges('g', [])
print('DEPTH FIRST SEARCH')
print(g.DFS_traversal(g.graph, 'a'))
print('\n')
print('BREADTH FIRST SEARCH')
print(g.BFS_traversal(g.graph, 'a'))
print('\n')
print('FIND USING BREADTH FIRST SEARCH')
g.BFS_find(g.graph, 'a', 'f')
print('\n')
print('FIND USING DEPTH FIRST SEARCH')
g.DFS_find(g.graph, 'a', 'f')
print('\n')


# Example 2
g = Graph()
g.add_nodes_edges(1, [2, 3 ,4])
g.add_nodes_edges(2, [7, 5])
g.add_nodes_edges(3, [5])
g.add_nodes_edges(4, [])
g.add_nodes_edges(5, [6])
g.add_nodes_edges(6, [])
g.add_nodes_edges(7, [])
print('DEPTH FIRST SEARCH')
print(g.DFS_traversal(g.graph, 1))
print('\n')
print('BREADTH FIRST SEARCH')
print(g.BFS_traversal(g.graph, 1))
print('\n')

# Example 3
g = Graph()
g.add_nodes_edges(1, [2, 3 ,4])
g.add_nodes_edges(2, [7, 5])
g.add_nodes_edges(3, [5])
g.add_nodes_edges(4, [])
g.add_nodes_edges(5, [6])
g.add_nodes_edges(6, [])
g.add_nodes_edges(7, [])
print('DEPTH FIRST SEARCH')
print(g.DFS_traversal(g.graph, 1))
print('\n')
print('BREADTH FIRST SEARCH')
print(g.BFS_traversal(g.graph, 1))
print('\n')