class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.numVertices = len(self.graph)
        self.status = ['undiscovered'] * self.numVertices
        self.cyclePresent = False
        self.topologicalOrder = []

    def dfs_visit(self):
        for v in self.graph:
            if self.status[v] == 'undiscovered':
                self.dfs(v)
        self.topologicalOrder.reverse()

    def dfs(self,v):
        self.status[v] = 'discovered'
        for u in self.graph[v]:
            if self.status[u] == 'discovered':
                self.cyclePresent = True
            if self.status[u] == 'undiscovered':
                self.dfs(u)
        self.status[v] = 'processed'
        self.topologicalOrder.append(v)

if __name__ == '__main__':
    graph = {0:[1], 1:[0,2], 2:[1]}
#    graph = {0:[1], 1:[]}
#    graph = {0:[1,2], 1:[3], 2:[3], 3:[]}
#    graph = {0:[1,2], 1:[3], 2:[1], 3:[2]}

    myGraph = Graph(graph)
    myGraph.dfs_visit()
    if myGraph.cyclePresent:
        print('Cycle exists. Topological sort is only possible for DAGs')
    else:
        print('No cycle. Topological order : {}'.format(myGraph.topologicalOrder))

