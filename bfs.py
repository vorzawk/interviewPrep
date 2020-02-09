from collections import deque
def bfs(graph, s):
    """ Find the shortest path from a given source vertex using bfs for unweighted graphs """
    dist = {s: 0}
    parent = {s: None}
    queue = deque([s])
    while queue:
        cur = queue.popleft()
        # Process the node here if necessary
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







