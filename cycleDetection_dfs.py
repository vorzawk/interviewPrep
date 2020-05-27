class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.numVertices = len(self.graph)
        self.status = ['undiscovered'] * self.numVertices
        self.parent = {}
        self.cyclePresent = False

    def dfs_visit(self):
        for v in self.graph:
            if self.status[v] == 'undiscovered':
                self.parent[v] = None
                self.dfs(v)

    def dfs(self,v):
        self.status[v] = 'discovered'
        for u in self.graph[v]:
            if self.status[u] == 'discovered' and self.parent[v] != u:
                self.cyclePresent = True
            if self.status[u] == 'undiscovered':
                self.parent[u] = v
                self.dfs(u)
        self.status[v] = 'processed'

if __name__ == '__main__':
#    graph = {0:[1,3], 1:[0,2,4], 2:[1,3], 3:[0,5,2], 4:[1], 5:[3], 6:[7], 7:[6]}
#    graph = {0:[1,3], 1:[0,2,4], 2:[1], 3:[0,5], 4:[1], 5:[3], 6:[7], 7:[6]}
#    graph = {0:[1], 1:[0]}
#    graph = {0:[1,2], 1:[3], 2:[3], 3:[]}
    graph = {0:[1,2], 1:[3], 2:[1], 3:[2]}

    myGraph = Graph(graph)
    myGraph.dfs_visit()
    if myGraph.cyclePresent:
        print('Cycle exists')
    else:
        print('No cycle')
    print(myGraph.status)
    print(myGraph.parent)

