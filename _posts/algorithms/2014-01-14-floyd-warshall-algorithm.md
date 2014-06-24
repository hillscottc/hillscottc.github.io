---
layout: post
markdown: redcarpet
category: algorithms
tagline: for All-Pairs Shortest Path
tags: [floyd, graph, shortest-path]
---
{% include JB/setup %}

[From a TopCoders Tutorial](http://community.topcoder.com/tc?module=Static&d1=tutorials&d2=graphsDataStrucs3)


Floyd-Warshall is a very powerful technique when the graph is represented by an adjacency matrix. It runs in `O(n^3)` time, where `n` is the number of vertices in the graph. However, in comparison to Dijkstra, which only gives us the shortest path from one source to the targets, Floyd-Warshall gives us the shortest paths from all source to all target nodes. There are other uses for Floyd-Warshall as well; it can be used to find connectivity in a graph (known as the Transitive Closure of a graph). 

First, however we will discuss the Floyd Warshall All-Pairs Shortest Path algorithm, which is the most similar to Dijkstra. After running the algorithm on the adjacency matrix the element at `adj[i][j]` represents the length of the shortest path from node `i` to node `j`. 

Pseudo-code for the algorithm :

    for (k = 1 to n)
       for (i = 1 to n)
           for (j = 1 to n)
               adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j]);

In Python, it would be:

        vertices = g.keys()

        d = g
        for v2 in vertices:
            d = {v1: {v3: min(d[v1][v3], d[v1][v2] + d[v2][v3])
                     for v3 in vertices}
                 for v1 in vertices}
        return d

As you can see, this is extremely simple to remember and type. If the graph is small (less than 100 nodes) then this technique can be used to great effect for a quick submission. 

    def costs_of_shortest_paths(g):
        """
        Cost of shortest path between every pair of vertices in a weighted graph.

        >>> inf = float('inf')
        >>> g = {0: {0: 0,   1: 1,   2: 4},
        ...      1: {0: inf, 1: 0,   2: 2},
        ...      2: {0: inf, 1: inf, 2: 0}}
        >>> fw(g) # doctest: +NORMALIZE_WHITESPACE
        {0: {0: 0,   1: 1,   2: 3},
         1: {0: inf, 1: 0,   2: 2},
         2: {0: inf, 1: inf, 2: 0}}
        """
        vertices = g.keys()

        d = g
        for v2 in vertices:
            d = {v1: {v3: min(d[v1][v3], d[v1][v2] + d[v2][v3])
                     for v3 in vertices}
                 for v1 in vertices}
        return d


An excellent problem to test this out on is the Division 2 1000 from SRM 184, TeamBuilder.

- Problems
  - Teambuilder

- Other resources
  - Floyd Warshall [data sets](https://www.cs.usfca.edu/~galles/visualization/Floyd.html)


