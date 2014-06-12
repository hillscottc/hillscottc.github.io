"""
+---- A
|   / |
|  B--D--C
|   \ | /
+---- E
"""

GRAPH = {
    'A': ['B', 'D'],
    'B': ['A', 'D', 'E'],
    'C': ['D', 'E'],
    'D': ['A', 'B', 'C', 'E'],
    'E': ['B', 'D', 'C']
}


def dfs_iter(graph, start, visited=None):
    """Iterative depth-first search of graph."""
    visited = [] if not visited else visited

    q = [start]
    while q:
        v = q.pop(0)
        if v not in visited:
            visited = visited + [v]
            q = graph[v] + q
    return visited


def bfs_iter(graph, start, visited=None):
    """Iterative breadth-first search of graph."""
    visited = [] if not visited else visited

    q = [start]
    while q:
        v = q.pop(0)
        if not v in visited:
            visited = visited + [v]
            q = q + graph[v]
    return visited


# https://www.python.org/doc/essays/graphs/
def find_shortest_path(graph, start, end, path=None):
    path = [] if not path else path
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest

if __name__ == "__main__":
    print dfs_iter(GRAPH, 'A')
    print bfs_iter(GRAPH, 'A')
    print find_shortest_path(GRAPH, 'A', 'C')
