from collections import deque
def bfs(graph, s):
    """ Find the shortest path from a given source vertex to all other vertices in an unweighted graph """
    dist = {s: 0}
    parent = {s: None}
    queue = deque([s])
    while queue:
        cur = queue.popleft()
        for v in graph[cur]:
            if v not in dist:
                queue.append(v)
                dist[v] = dist[cur] + 1
                parent[v] = cur
    return dist, parent

def shortestPath(graph, s, t):
    dist, parent = bfs(graph, s)
    if t in dist:
        print("shortest path of size : {}".format(dist[t]))
        v = t
        path = [t]
        while v != s:
            path.append(parent[v])
            v = parent[v]
        path.reverse()
        for u in path[:-1]:
            print("{} -> ".format(u), end='')
        print(path[-1])

if __name__ == '__main__':
#    graph = {0:[1,3], 1:[0,2], 2:[1], 3:[0,4], 4:[3]}
#    graph = {0:[1,2], 1:[0,2], 2:[0,1]}
    graph = {0:[1], 1:[2], 2:[0]}
    s = 0; t = 2
    shortestPath(graph, s, t)






