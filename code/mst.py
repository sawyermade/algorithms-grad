class Graph:
	def __init__(self):
		self.adjDict = {}
		self.edgeList = []
		self.vList = []
		self.E = 0
		self.V = 0

	def addEdge(self, u, v, w):
		if u not in self.adjDict.keys():
			self.adjDict.update({u : [(v, w)]})
			self.V += 1
		else:
			if (v, w) not in self.adjDict[u]:
				self.adjDict[u].append((v, w))


		if v not in self.adjDict.keys():
			self.adjDict.update({v : [(u, w)]})
			self.V += 1
		else:
			if (u, w) not in self.adjDict[v]:
				self.adjDict[v].append((u, w))

		if [u, v, w] not in self.edgeList and [v, u, w] not in self.edgeList: 
			self.edgeList.append([u, v, w])
			self.E += 1

		if u not in self.vList:
			self.vList.append(u)
		if v not in self.vList:
			self.vList.append(v)

	def print(self):
		vList = self.vList
		vList.sort()

		for v in vList:
			print('{}: '.format(v), end='')
			adjList = self.adjDict[v]
			for adj in adjList:
				print('{} '.format(adj[0]), end='')
			print()


def createGraph():
	g = Graph()

	g.addEdge('a', 'b', 10)
	g.addEdge('a', 'c', 12)
	g.addEdge('b', 'c', 9)
	g.addEdge('b', 'd', 8)
	g.addEdge('c', 'e', 3)
	g.addEdge('c', 'f', 1)
	g.addEdge('d', 'e', 7)
	g.addEdge('d', 'f', 9)
	g.addEdge('d', 'g', 8)
	g.addEdge('d', 'h', 5)
	g.addEdge('e', 'f', 3)
	g.addEdge('f', 'h', 6)
	g.addEdge('g', 'h', 9)
	g.addEdge('g', 'i', 2)
	g.addEdge('h', 'i', 11)

	return g

def kruskal(g):
	pass

def prims(g):
	pass

if __name__ == '__main__':
	g = createGraph()

	g.print()