---
layout: default
title: Programming Notes
---

[TopCoder Algorithm Tutorial](http://community.topcoder.com/tc?module=Static&d1=tutorials&d2=importance_of_algorithms)

A *heuristic* is an approximation of something that is relevant to the problem, and is often computed by an algorithm of its own.


## Approximate algorithms, NP-complete

There are quite a few important problems for which the best-known algorithm that produces an optimal answer is insufficiently slow for most purposes. The most famous group of these problems is called NP, which stands for **non-deterministic polynomial**. When a problem is said to be NP-complete or NP-hard, it mean no one knows a good way to solve them optimally. Furthermore, if someone did figure out an efficient algorithm for one NP-complete problem, that algorithm would be applicable to all NP-complete problems. 

A good example of an NP-hard problem is the famous traveling salesman problem. A salesman wants to visit N cities, and he knows how long it takes to get from each city to each other city. The question is "how fast can he visit all of the cities?" Since the fastest known algorithm for solving this problem is too slow - and many believe this will always be true - programmers look for sufficiently fast algorithms that give good, but not optimal solutions. 


## Maximum Flow

The maximum flow problem has to do with determining the best way to get some sort of stuff from one place to another, through a network of some sort.

The first efficient algorithm for finding the maximum flow was the **Ford-Fulkerson algorithm**.

The idea behind the algorithm is as follows: As long as there is a path from the source (start node) to the sink (end node), with available capacity on all edges in the path, we send flow along one of these paths. Then we find another path, and so on. A path with available capacity is called an augmenting path.

Graduation, from SRM 200, is a good example of a TopCoder problem that lends itself to a solution using max flow. 


## Sequence comparison

For example, transform sequence A into sequence B...

For example, lets consider two sequences of letters, "AABAA" and "AAAB". To transform the first sequence into the second, the simplest thing to do is delete the B in the middle, and change the final A into a B. 

This algorithm has many applications, including some DNA problems and plagiarism detection. However, the form in which many programmers use it is when comparing two versions of the same source code file.

## Dynamic Programming

[TopCoder Tutorial](http://community.topcoder.com/tc?module=Static&d1=tutorials&d2=dynProg)

See the [Coins Problems](/problems/coins.html).


## Distributed programming via Map/Reduce 

[wiki](http://en.wikipedia.org/wiki/MapReduce)
  > *Map*
  >  The master node takes input, divides it into sub-problems, and distributes them to workers. 
  >  Worker nodes may do this again in turn, leading to a multi-level tree structure. 
  >  Worker nodes process the smaller problems, and pass answer back to its master node.
  >
  > *Reduce*
  > The master node collects all the answers and combines them in some way to form the output.


## Concurrency: 

Process is in instance. It contains threads. Threads can share resources. Celery. Task queues are a scalable mechanism to distribute work across threads or machines. Celery communicates via messages, using a broker to mediate between clients and workers. To initiate a task a client puts a message on the queue, the broker then delivers the message to a worker. The message broker is an in-memory data structure store. Redis, Gevent. Pykka


## Memoization

To explain memoization, see these different versions of Fibonacci.

Purely recursive. Highly inefficient. Recalculates every value for every calculation.
<script src="https://gist.github.com/hillscottc/0e95de91f03658c77e5d.js"></script>

Iterative. Much faster.
<script src="https://gist.github.com/hillscottc/b086891d57f65509350d.js"></script>

Here is the memoization technique. A 'cache' dictionary of { (args) : (return_val),  } is created.
This allows us to quickly locate and reuse any value that has already been calculated.
<script src="https://gist.github.com/hillscottc/a2c5dec8512a96ac60b9.js"></script>

Here is the same memoization design, implemented as a decorator.
<script src="https://gist.github.com/hillscottc/c68a2b85ec2f1bc145d2.js"></script>




