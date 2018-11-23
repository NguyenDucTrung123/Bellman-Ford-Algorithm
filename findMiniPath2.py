import numpy as np
from collections import defaultdict




#a class to represent a vertex in a graph as a node. 
class Node(object):
	def __init__(self, vertex_name, dist = float('inf'), trace = None):
		self.vertex_name = vertex_name
		self.dist = dist
		self.trace = trace
		pass
"""

class Vertex(object):
	#docstring for Vertex
	def __init__(self, vertex_name):
		super(Vertex, self).__init__()
		self.vertex = vertex_name
		self.next = None
"""	
v = 0
e = 0
s = 0
f = 0	
#a class to represent a graph. A graph
#is the list of the adjacency lists. 
# Size of the array will be the no. of the 
# vertices "V" 
class Graph(object):
	"""docstring for Graph"""
	V = [] # list of nodes.
	E = [] # list of edges. Each edge is a list containing 2 nodes and 1 integer.
	minipath = []# list of Nodes
	numVer = 0 # No. of Vertices
	numEdge = 0 # N. of Edges

	def __init__(self, vertices=[], edges=[], minipath = [], numVer = 0, numEdge = 0):
		super(Graph, self).__init__()
		self.V = vertices
		self.E = edges
		self.minipath= minipath
		# No. of Vertices
		self.numVer = numVer
		# No. of edges
		self.numEdge = numEdge


    # Function to add an edge in the graph
    # src and dest are nodes that are ends of the added edge
    # weight is cost to go from src to dest. 
	def addEdge(self,src,dest,weight):
		self.E.append([src,dest,weight])

	# Function to find a mini path that links between node src and node dest.
	def BellmanFord(self, src, dest):
		for v in self.V: 
			v.dist = float("inf")
		self.V[src-1].dist = 0
		for a in self.V:
			for [u ,v ,w] in self.E:
				if self.V[v-1].dist > self.V[u-1].dist + w:
					self.V[v-1].dist = self.V[u-1].dist + w
					self.V[v-1].trace = u  
		if self.V[dest-1] == float('inf'):
			return
			pass
		self.minipath.append(dest)
		while src not in self.minipath: 
			self.minipath.append(self.V[self.minipath[-1]-1].trace)

G = Graph()
print("\nRead input from file")
#with open('MINPATH.INP','r') as fp:
fp = open( 'minpath_in.txt', 'r' )
line = fp.readline()
coords = line.split(" ")
G.numVer = int(coords[0])
G.numEdge = int(coords[1])
s = int(coords[2])
f = int(coords[3])
line = fp.readline()
while line:
    coords = line.split(" ")
    G.addEdge(int(coords[0]), int(coords[1]), int(coords[2]))
    line = fp.readline()
    pass
fp.close()

for i in range(1,G.numVer+1):
	G.V.append(Node(i))
G.BellmanFord(s,f)

print("\nWrite ouput into file")
#with open('MINPATH.OUT','w') as fp:
fp = open( 'minpath_out.txt', 'w' )
if s not in G.minipath:
    fp.write("\nThere are no paths from %d to %d" % (G.V[s-1].vertex_name, G.V[f-1].vertex_name))
else:
    fp.write("Distance from %d to %d is: %d\n" % (G.V[s-1].vertex_name, G.V[f-1].vertex_name, G.V[f-1].dist))
    fp.write('%d'% G.V[f-1].vertex_name)
    for v in G.minipath:
        if G.V[v-1].trace != None:
            fp.write(" <-- %d" % G.V[v-1].trace)
fp.close()
		