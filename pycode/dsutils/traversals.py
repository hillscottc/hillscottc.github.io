"""
Breadth-First and Depth-First graph traversal.

BFT and DFT are identical, _except_
> DFS store unvisited nodes in a stack, while
> BFS store unvisited nodes in a queue.

From http://code.activestate.com/recipes/576723-dfs-and-bfs-graph-traversal/
"""


def dft(graph, start, visited=None):
    visited = [] if not visited else visited
    q = [start]
    while q:
        v = q.pop(0)
        if v not in visited:
            visited = visited + [v]
            q = graph[v] + q  # unvisited to TOP (stack)
    return visited


def bft(graph, start, visited=None):
    visited = [] if not visited else visited
    q = [start]
    while q:
        v = q.pop(0)
        if v not in visited:
            visited = visited + [v]
            q = q + graph[v]  # unvisited to BOTTOM (queue)
    return visited


if __name__ == "__main__":
    import sample_data as samp
    print dft(samp.ADJL_1, 'A')
    print bft(samp.ADJL_2, 'A')
