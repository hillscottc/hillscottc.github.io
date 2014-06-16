---
layout: default
title: traversals.py
---
[gist:traversals](https://gist.github.com/hillscottc/5872513c69398e003fd4)


    """
    BFS and DFS are IDENTICAL but for one line...
    putting unvisited nodes to TOP or BOTTOM of list.
    """

    def dfs(graph, start, visited=None):
        visited = [] if not visited else visited
        q = [start]
        while q:
            v = q.pop(0)
            if v not in visited:
                visited = visited + [v]
                q = graph[v] + q          ## Unvisited to TOP of list!
        return visited

    def bfs(graph, start, visited=None):
        visited = [] if not visited else visited
        q = [start]
        while q:
            v = q.pop(0)
            if v not in visited:
                visited = visited + [v]
                q = q + graph[v]         ## Unvisited to BOTTOM of list!
        return visited

