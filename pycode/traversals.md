---
layout: default
title: traversals.py
---
[gist:traversals](https://gist.github.com/hillscottc/5872513c69398e003fd4)

    """
    They are identical, except:
    DFS uses a stack, and BFS uses a queue
    to store unvisited nodes.
    """

    def dfs(graph, start, visited=None):
        visited = [] if not visited else visited
        q = [start]
        while q:
            v = q.pop(0)
            if v not in visited:
                visited = visited + [v]
                q = graph[v] + q          # unvisited to TOP (stack)
        return visited

    def bfs(graph, start, visited=None):
        visited = [] if not visited else visited
        q = [start]
        while q:
            v = q.pop(0)
            if v not in visited:
                visited = visited + [v]
                q = q + graph[v]         # unvisited to BOTTOM (queue)
        return visited

    if __name__ == "__main__":
        '''
           +---- A
           |   /   \
           |  B--D--C
           |   \ | /
           +---- E
        '''
        graph = {'A': ['B', 'C'], 'B': ['D', 'E'],
                 'C': ['D', 'E'], 'D': ['E'], 'E': ['A']}

        print dfs(graph, 'A')
        print bfs(graph, 'A')

    