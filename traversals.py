GRAPH_PIC = """
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
    'E': ['B', 'D', 'C']}


def dfs_recurs(graph, start, visited=None):
    """Recursive depth-first search of graph."""
    visited = [] if not visited else visited

    visited = visited + [start]
    for node in graph[start]:
        if not node in visited:
            visited = dfs_recurs(graph, node, visited)
    return visited


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


if __name__ == "__main__":
    dfs_recurs(GRAPH, 'A')
    dfs_iter(GRAPH, 'A')
    bfs_iter(GRAPH, 'A')
