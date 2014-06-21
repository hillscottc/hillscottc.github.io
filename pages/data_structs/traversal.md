---
layout: page
markdown: redcarpet
title: Graph Traversal ... BFS, DFS, Djikstra
group: data_structs
---
{% include JB/setup %}

While traversing methods, how the keys are printed sometimes make a difference:

- *INORDER* prints the root key BETWEEN subtrees.
- *preorder* prints keys before, and *postorder* prints keys after subtrees.


Dijkstra (Heap method)

Dijkstra using a Heap is one of the most powerful techniques to add to your TopCoder arsenal. It essentially allows you to write a Breadth First search, and instead of using a Queue you use a Priority Queue/Heap with  has a sorting func on nodes such that lowest cost nodes are on top.

This allows us to find the best path through a graph in:

> O(m * log(n)) time where n is the number of vertices and m is the number of edges in the graph.

The Heap's nice properties:

- inserting an element or removing the top element takes O(log n) time, where n is the num elems in the heap. 
- Getting the top value is an O(1) operation


Dijkstra pseudocode:

    void dijkstra(node start) {
        priorityQueue s;
        s.add(start);
        while (s.empty() == false) {
            top = s.top();
            s.pop();
            mark top as visited;
            check for termination condition (have we reached the target node?)
            add all of top's unvisited neighbors to the stack.
        }
    }



## Floyd-Warshall, All-Pairs Shortest Path

[From a TopCoders Tutorial](http://community.topcoder.com/tc?module=Static&d1=tutorials&d2=graphsDataStrucs3)



Floyd-Warshall is a very powerful technique when the graph is represented by an adjacency matrix. It runs in O(n^3) time, where n is the number of vertices in the graph. However, in comparison to Dijkstra, which only gives us the shortest path from one source to the targets, Floyd-Warshall gives us the shortest paths from all source to all target nodes. There are other uses for Floyd-Warshall as well; it can be used to find connectivity in a graph (known as the Transitive Closure of a graph). 

First, however we will discuss the Floyd Warshall All-Pairs Shortest Path algorithm, which is the most similar to Dijkstra. After running the algorithm on the adjacency matrix the element at `adj[i][j]` represents the length of the shortest path from node i to node j. 

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






