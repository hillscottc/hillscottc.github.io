---
layout: default
title: Directed Acyclic Graphs (DAGs) and Topological Sorting
---

A directed graph with no cycles is called a directed acyclic graph or a DAG. 

In an operating system, at the most abstract level, how do you get deadlock? You have a collection of processes waiting for (dependent on) other processes. There is a cycle in the dependencies.  If you expect to finish a collection of tasks with dependencies, there can be no cyclic dependency!

A workable dependency graph is a directed acyclic graph (DAG).

In parallel processes, tasks that do not depend on each other can be done at the same time. The chain of dependencies that takes the longest time determines the minimum time to completion. This longest time chain of dependencies is a **critical path**. 


## Topological Sorting of directed acyclic graphs (DAGs)

Topological sorting is the most important operation on directed acyclic graphs (DAGs). It orders the vertices on a line such that all directed edges go from left to right. Such an ordering cannot exist if the graph contains a directed cycle, because there is no way you can keep going right on a line and still return back to where you started from! Each DAG has at least one topological sort.

The importance of topological sorting is that it gives us an ordering to process each vertex before any of its successors. Suppose the edges represented precedence constraints, such that edge (x, y) means job x must be done before job y. Then, any topological sort defines a legal schedule.

### A great algorithm, from [this blog post](http://blog.jupo.org/2012/04/06/topological-sorting-acyclic-directed-graphs/)

![An acylic directed graph, fig 1](/img/topological_1.png)

(gist embedded)

<script src="https://gist.github.com/hillscottc/ee407aea701ef342fce0.js"></script>


### The pancake example, from [interactivepython](http://interactivepython.org/courselib/static/pythonds/Graphs/graphdfs.html#topological-sorting)


![Figure 27: The Steps for Making Pancakes](/img/PSADS_27.png)

To determine the precise *order* of the pancake steps, use a **topological sort**. 
The topological sort could compute return the vertices in a list in decreasing order of finish time.

Figure 28 shows the depth first forest constructed by dfs on the pancake-making graph shown in Figure 26.

![Figure 28: Result of Depth First Search on the Pancake Graph](/img/PSADS_28.png)

Finally, Figure 29 shows the results of applying the topological sort algorithm to our graph. Now all the ambiguity has been removed and we know exactly the order in which to perform the pancake making steps.

![Figure 29: Result of Topological Sort on Directed Acyclic Graph](/img/PSADS_29.png)







