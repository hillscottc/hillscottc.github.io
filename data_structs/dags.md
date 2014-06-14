---
layout: default
title: Directed Acyclic Graphs
---

A directed graph with no cycles is called a directed acyclic graph or a DAG. 

In an operating system, at the most abstract level, how do you get deadlock? You have a collection of processes waiting for (dependent on) other processes. There is a cycle in the dependencies.  If you expect to finish a collection of tasks with dependencies, there can be no cyclic dependency!

A workable dependency graph is a directed acyclic graph (DAG).

In parallel processes, tasks that do not depend on each other can be done at the same time. The chain of dependencies that takes the longest time determines the minimum time to completion. This longest time chain of dependencies is a **critical path**. 


## Topological Sorting of directed acyclic graphs (DAGs)

Topological sorting is the most important operation on directed acyclic graphs (DAGs). It orders the vertices on a line such that all directed edges go from left to right. Such an ordering cannot exist if the graph contains a directed cycle, because there is no way you can keep going right on a line and still return back to where you started from! Each DAG has at least one topological sort.

The importance of topological sorting is that it gives us an ordering to process each vertex before any of its successors. Suppose the edges represented precedence constraints, such that edge (x, y) means job x must be done before job y. Then, any topological sort defines a legal schedule.


### An excellent example, from this [blog post](http://blog.jupo.org/2012/04/06/topological-sorting-acyclic-directed-graphs/)

![An acylic directed graph, fig 1](/img/topological_1.png)

(gist embedded)

<script src="https://gist.github.com/hillscottc/ee407aea701ef342fce0.js"></script>







