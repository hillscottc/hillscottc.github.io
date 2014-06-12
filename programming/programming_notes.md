---
layout: default
title: Programming Notes
---


- Distributed programming via Map/Reduce [wiki](http://en.wikipedia.org/wiki/MapReduce)
  > *Map*
  >  The master node takes input, divides it into sub-problems, and distributes them to workers. 
  >  Worker nodes may do this again in turn, leading to a multi-level tree structure. 
  >  Worker nodes process the smaller problems, and pass answer back to its master node.
  >
  > *Reduce*
  > The master node collects all the answers and combines them in some way to form the output.

- Concurrency: 
    Process is in instance. It contains threads. Threads can share resources. Celery. Task queues are a scalable mechanism to distribute work across threads or machines. Celery communicates via messages, using a broker to mediate between clients and workers. To initiate a task a client puts a message on the queue, the broker then delivers the message to a worker. The message broker is an in-memory data structure store. Redis, Gevent. Pykka


- SQL aggregate functions

        SELECT ID, AVG(Bonus) as 'Avg Bonus', SUM(SalesYTD) as 'Year Sales'
        FROM Sales.Table GROUP BY ID;
  


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




