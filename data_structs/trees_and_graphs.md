---
layout: default
title: Trees and Graphs
---

- A tree is an undirected graph that is connected and acyclic.
- Search is a factor of height.

- A tree cannot have a loop.

- Many kinds by tweaking the balance, height, or adding props like color, etc.

- Dijkstras Algorithm for shortest path is used for many solutions.
  <script src="https://gist.github.com/hillscottc/7d2e17c59d96e26ec855.js"></script>

- Binary Search Trees
    - Each node has a comparable key and no more than two child nodes.
    - The left sub-tree contains only nodes with keys less than the parent node.
    - The right sub-tree contains only nodes with keys greater than the parent node.
    - Operations: SEARCH, MIN/MAX, PREDECESSOR/SUCCESSOR, INSERT/DELETE


### Graphs

[TopCoder Graphs](http://help.topcoder.com/data-science/competing-in-algorithm-challenges/algorithm-tutorials/introduction-to-graphs-and-their-data-structures-section-1/)

Graphs are a fundamental data structure in the world of programming. 

Knowing the correct data structures to use with graph problems is critical. A problem that appears intractable may prove to be a few lines with the proper data structure.

While a tree only allows a node to have children, and there cannot be any loops in the tree, with a more general graph we can represent many different situations.

A very common example used is flight paths between cities. If there is a flight between city A and city B there is an edge between the cities. The *cost* of the edge can be the length of time that it takes for the flight, or perhaps the amount of fuel used.

```python
structure node
   [list of nodes] neighbors
   [data]
end

cost(X, Y) := if (X.neighbors contains Y) return X.neighbors[Y];
         else "Not possible"
```

### Recognizing a graph problem:

Some common keywords associated with graph problems are: vertices, nodes, edges, connections, connectivity, paths, cycles and direction.

An example of a description of a simple problem that exhibits some of these characteristics is:

"Bob has become lost in his neighborhood. He needs to get from his current position back to his home. Bob's neighborhood is a 2 dimensional grid, that starts at (0, 0) and (width - 1, height - 1). There are empty spaces upon which bob can walk with no difficulty, and houses, which Bob cannot pass through. Bob may only move horizontally or vertically by one square at a time.""

Bob's initial position will be represented by a 'B' and the house location will be represented by an 'H'. Empty squares on the grid are represented by '.' and houses are represented by 'X'. Find the minimum number of steps it takes Bob to get back home, but if it is not possible for Bob to return home, return -1.

An example of a neighborhood of width 7 and height 5:

    ...X..B
    .X.X.XX
    .H.....
    ...X...
    .....X."

Once you have recognized that the problem is a graph problem it is time to start building up your representation of the graph in memory.


### Convert a directed graph to an adjacency matrix

Convert a directed graph to an adjacency matrix.

Note: The distance from a node to itself is 0 and distance from a node to
an unconnected node is defined to be infinite.


    def adj(g):
        """
        >>> g = {1: {2: 3, 3: 8, 5: -4},
        ...      2: {4: 1, 5: 7},
        ...      3: {2: 4},
        ...      4: {1: 2, 3: -5},
        ...      5: {4: 6}}
        >>> adj(g) # doctest: +NORMALIZE_WHITESPACE
        {1: {1: 0, 2: 3, 3: 8, 4: inf, 5: -4},
         2: {1: inf, 2: 0, 3: inf, 4: 1, 5: 7},
         3: {1: inf, 2: 4, 3: 0, 4: inf, 5: inf},
         4: {1: 2, 2: inf, 3: -5, 4: 0, 5: inf},
         5: {1: inf, 2: inf, 3: inf, 4: 6, 5: 0}}
        """
        vertices = g.keys()
        return {v1: {v2: 0 if v1 == v2 else g[v1].get(v2, float('inf'))
                     for v2 in vertices}
                for v1 in vertices}


### Singly linked lists

An example of one of the simplest types of graphs is a singly linked list! Now we can start to see the power of the graph data structure, as it can represent very complicated relationships, but also something as simple as a list.
A singly linked list has one "head" node, and each node has a link to the next node. So the structure looks like this:

    structure node
       [node] link;
       [data]
    end

node head;

A simple example would be:

    node B, C;
    head.next = B;
    B.next = C;
    C.next = null;

This would be represented graphically as `head -> B -> C -> null`.

The *cost function* would look as follows:

    cost(X, Y) := if (X.link = Y) return 1;
               else if (X = Y) return 0;
               else "Not possible"

This cost function represents the fact that we can only move directly to the link node from our current node. 
Get used to seeing cost functions because anytime that you encounter a graph problem you will be dealing with them in some form or another.

