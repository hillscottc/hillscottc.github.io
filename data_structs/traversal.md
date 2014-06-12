---
layout: default
title: Graph Traversal ... BFS, DFS, Djikstra
---



While traversing methods, how the keys are printed sometimes make a difference:

- *INORDER* prints the root key BETWEEN subtrees.
- *preorder* prints keys before, and *postorder* prints keys after subtrees.

Algorithms follow this pattern, roughly:

- If an edge goes to an undiscovered vertex x, mark x discovered and add it to work queue
- Skip edges that go to a processed vertex.
- Skip edges that go to a discovered vertex. They've already been added to queue.

Each undirected edge will be considered exactly twice, once when each of its endpoints is explored.


## DEPTH-FIRST

Wander paths with a **stack**  

Where we want to find any solution to the problem (not necessarily the shortest path), or to visit all of the nodes in the graph. 

A classic problem is the The flood-fill operation for a graphic painting application. The concept is to fill a bounded region with a single color. This concept maps extremely well to a Depth First search. The basic concept is to visit a node, then push all of the nodes to be visited onto the stack.


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


## BREADTH-FIRST

Radiate from start with a **queue**

It has the extremely useful property -- if all of the edges in a graph are unweighted (or the same weight) then the first time a node is visited is the shortest path to that node from the source node.

The depth first search is well geared towards problems where we want to find any solution to the problem (not necessarily the shortest path), or to visit all of the nodes in the graph. 


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


## Finding the best path through a graph

Dijkstra (Heap method)

Dijkstra using a Heap is one of the most powerful techniques to add to your TopCoder arsenal. It essentially allows you to write a Breadth First search, and instead of using a Queue you use a Priority Queue/Heap with  has a sorting func on nodes such that lowest cost nodes are on top.

This allows us to find the best path through a graph in:

> O(m * log(n)) time where n is the number of vertices and m is the number of edges in the graph.

The Heap's nice properties:

- inserting an element or removing the top element takes O(log n) time, where n is the num elems in the heap. 
- Getting the top value is an O(1) operation


** Dijkstra pseudocode:**

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


** Dijkstra's Algorithm** (from Interactive Python):  

    class Graph:
      def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

      def add_node(self, value):
        self.nodes.add(value)

      def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance


    def dijsktra(graph, initial):
      visited = {initial: 0}
      path = {}

      nodes = set(graph.nodes)

      while nodes: 
        min_node = None
        for node in nodes:
          if node in visited:
            if min_node is None:
              min_node = node
            elif visited[node] < visited[min_node]:
              min_node = node

        if min_node is None:
          break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
          weight = current_weight + graph.distance[(min_node, edge)]
          if edge not in visited or weight < visited[edge]:
            visited[edge] = weight
            path[edge] = min_node

      return visited, path


