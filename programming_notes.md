---
layout: default
title: Programming Notes
---

## Recursion

- [Recursion](recursion.md)

Like the robots of Asimov, all recursive algorithms must obey three important laws:  

    1. Must have a base case. Typically a problem that is small enough to solve directly.  
    2. Must change its state and move toward the base case. Usually, data getting smaller.  
    3. A recursive algorithm must call itself, recursively.  

## Sum of a List of Numbers
We will begin our investigation with a simple problem that you already know how to solve without using recursion. Suppose that you want to calculate the sum of a list of numbers such as: [1,3,5,7,9]. An iterative function that computes the sum is shown. The function uses an accumulator variable (theSum) to compute a running total.

We could rewrite the list as a fully parenthesized expression, like this:

    ((((1+3)+5)+7)+9) , or  (1+(3+(5+(7+9))))

See the innermost set of paren, `(7+9)` can be solved without a loop or any special constructs. 

To state it in a functional form:
    
    sum_nums(nums) = first(nums) + sum_nums(rest(nums))

There are two key ideas in this listing to look at.
- First, on line 2 is escape clause check. The sum of a list of length 1 is trivial.
- Then, it's a series of simplifications. Each recursive call solves a smaller problem, til it can't get any smaller.

    def sum_nums(nums):
        """
        >>> sum_nums([2, 20, 20])
        42
        """    
        if len(nums) == 1:
            return nums[0]
        else:
            return nums[0] + sum_nums(nums[1:])

    def echo(txt):
        """
        >>> echo('hello')
        'hello'
        """      
        if len(txt) == 1:
            return txt[0]
        else:
            return txt[0] + echo(txt[1:])

    def rev(txt):
        """
        >>> rev('hello')
        'olleh'
        """      
        if len(txt) == 1:
            return txt[0]
        else:
            return  rev(txt[1:]) + txt[0]


### Factorial 

4! = 4 * 3 * 2 * 1

Recursive:

    def factorial(n):
        if n == 1:
            return 1
        else:
            return n * factorial(n-1)

Iterative:

    def iterative_factorial(n):
        result = 1
        for i in range(2,n+1):
            result *= i
        return result

### Fibonacci

0,1,1,2,3,5,8,13,21,34,55,89, ...

The Fibonacci numbers are defined by:

    Fn = Fn-1 + Fn-2
    with F0 = 0 and F1 = 1

Recursive solution:

    def fib(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n-1) + fib(n-2)

Iterative solution:

    def fibi(n):
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return a

The iterative version fibi() is a lot faster than the recursive version fib().

### Compute an Exponent

    def exp(x, n):
        if n == 0:
            return 1
        else:
            return x * exp(x, n-1)

### Flatten a nested list

    def flatten_list(a, result=None):
        if result is None:
            result = []

        for x in a:
            if isinstance(x, list):
                flatten_list(x, result)
            else:
                result.append(x)

        return result



- Dynamic Programming. (Build matrices, iterate.)

[Berkely, Chapter 6]

Dynamic programming
In the preceding chapters we have seen some elegant design principles—such as divide-and-
conquer, graph exploration, and greedy choice—that yield definitive algorithms for a variety
of important computational tasks. The drawback of these tools is that they can only be used
on very specific types of problems. We now turn to the two sledgehammers of the algorithms
craft, dynamic programming and linear programming, techniques of very broad applicability
that can be invoked when more specialized methods fail. Predictably, this generality often
comes with a cost in efficiency.
6.1 Shortest paths in dags, revisited
At the conclusion of our study of shortest paths (Chapter 4), we observed that the problem is
especially easy in directed acyclic graphs (dags). Let’s recapitulate this case, because it lies at
the heart of dynamic programming.
The special distinguishing feature of a dag is that its nodes can be linearized; that is, they
can be arranged on a line so that all edges go from left to right (Figure 6.1). To see why
this helps with shortest paths, suppose we want to figure out distances from node S to the
other nodes. For concreteness, let’s focus on node D. The only way to get to it is through its

Figure 6.1 A dag and its linearization (topological ordering).


predecessors, B or C; so to find the shortest path to D, we need only compare these two routes:
dist(D) = min{dist(B) + 1, dist(C) + 3}.
A similar relation can be written for every node. If we compute these dist values in the
left-to-right order of Figure 6.1, we can always be sure that by the time we get to a node v,
we already have all the information we need to compute dist(v). We are therefore able to
compute all distances in a single pass:
initialize all dist(·) values to ∞
dist(s) = 0
for each v ∈ V \{s}, in linearized order:
dist(v) = min (u,v)∈E {dist(u) + l(u, v)}
Notice that this algorithm is solving a collection of subproblems, {dist(u) : u ∈ V }. We
start with the smallest of them, dist(s), since we immediately know its answer to be 0. We
then proceed with progressively “larger” subproblems—distances to vertices that are further
and further along in the linearization—where we are thinking of a subproblem as large if we
need to have solved a lot of other subproblems before we can get to it.
This is a very general technique. At each node, we compute some function of the values
of the node’s predecessors. It so happens that our particular function is a minimum of sums,
but we could just as well make it a maximum, in which case we would get longest paths in the
dag. Or we could use a product instead of a sum inside the brackets, in which case we would
end up computing the path with the smallest product of edge lengths.
Dynamic programming is a very powerful algorithmic paradigm in which a problem is
solved by identifying a collection of subproblems and tackling them one by one, smallest first,
using the answers to small problems to help figure out larger ones, until the whole lot of them
is solved. In dynamic programming we are not given a dag; the dag is implicit. Its nodes are
the subproblems we define, and its edges are the dependencies between the subproblems: if
to solve subproblem B we need the answer to subproblem A, then there is a (conceptual) edge
from A to B. In this case, A is thought of as a smaller subproblem than B—and it will always
be smaller, in an obvious sense.
But it’s time we saw an exam








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
  
- Misc
    - Discussion - challenges , designs, optimizations, testing, ideas, nltk 
    - don't ask, "Are algorithms *really* all that important in real life?"
    - bring your own whiteboard dry-erase markers


- Resources
    - [Harrington at Loyola, Comp 363: Algorithms](http://anh.cs.luc.edu/363/notes/)
    - [InteractivePython, Problem Solving with Algorithms and Data Structures](http://interactivepython.org/courselib/static/pythonds/index.html)
    - [Vazirani at Berekely, Algorithms](http://www.cs.berkeley.edu/~vazirani/algorithms/)


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







# Sorting
#  Time Complexity of Solution:
#  Best = Average = Worst = O(nlog(n)).
#
#  Approach:
#  Merge sort is a divide and conquer algorithm. 
#
#  NOTE to the Python experts: While it might seem more "Pythonic" to take such approach as
#        mid = len(aList) / 2
#        left = mergesort(aList[:mid])
#        right = mergesort(aList[mid:])
#
#    That approach take too much memory for creating sublists.
#=======================================================================

    def mergesort( aList ):
      _mergesort( aList, 0, len( aList ) - 1 )
    def _mergesort( aList, first, last ):
      # break problem into smaller structurally identical pieces
      mid = ( first + last ) / 2
      if first < last:
        _mergesort( aList, first, mid )
        _mergesort( aList, mid + 1, last )
      # merge solved pieces to get solution to original problem
      a, f, l = 0, first, mid + 1
      tmp = [None] * ( last - first + 1 )
      while f <= mid and l <= last:
        if aList[f] < aList[l] :
          tmp[a] = aList[f]
          f += 1
        else:
          tmp[a] = aList[l]
          l += 1
        a += 1
      if f <= mid :
        tmp[a:] = aList[f:mid + 1]
      if l <= last:
        tmp[a:] = aList[l:last + 1]
      a = 0
      while first <= last:
        aList[first] = tmp[a]
        first += 1
        a += 1



Chapter 2

Merge Sort
The merge sort algorithm closely follows the divide-and-conquer paradigm. 
Intuitively, it operates as follows.

Divide: Divide the n-element sequence to be sorted into two subsequences of n=2 elements each.
Conquer: Sort the two subsequences recursively using merge sort.
Combine: Merge the two sorted subsequences to produce the sorted answer.

The key operation of the merge sort algorithm is the merging of two sorted
sequences in the “combine” step. We merge by calling an auxiliary procedure
MERGE (A, p, q, r), where A is an array and p, q, and r are indices into the array
such that p < q < r.

Our MERGE procedure takes time , where n = r - p + 1 is the total
number of elements being merged.

Our basic step consists of choosing the smaller of the two cards on top of the face-up piles, removing it
from its pile (which exposes a new top card), and placing this card face down onto
the output pile. We repeat this step until one input pile is empty, at which time
we just take the remaining input pile and place it face down onto the output pile.
Computationally, each basic step takes constant time, since we are comparing just
the two top cards. Since we perform at most n basic steps, merging takes  time.





Here's wikipedia..http://rosettacode.org/wiki/Sorting_algorithms/Merge_sort

The merge sort is a recursive sort of order n*log(n). It is notable for having a worst case and average complexity of O(n*log(n)), and a best case complexity of O(n) (for pre-sorted input). The basic idea is to split the collection into smaller groups by halving it until the groups only have one element or no elements (which are both entirely sorted groups). Then merge the groups back together so that their elements are in order. This is how the algorithm gets its "divide and conquer" description.Write a function to sort a collection of integers using the merge sort. The merge sort algorithm comes in two parts: a sort function and a merge function. The functions in pseudocode look like this:

    function mergesort(m)
       var list left, right, result
       if length(m) ≤ 1
           return m
       else
           var middle = length(m) / 2
           for each x in m up to middle - 1
               add x to left
           for each x in m at and after middle
               add x to right
           left = mergesort(left)
           right = mergesort(right)
           if last(left) ≤ first(right) 
              append right to left
              return left
           result = merge(left, right)
           return result

    function merge(left, right)
       var list result
       while length(left) > 0 and length(right) > 0
           if first(left) ≤ first(right)
               append first(left) to result
               left = rest(left)
           else
               append first(right) to result
               right = rest(right)
       if length(left) > 0 
           append rest(left) to result
       if length(right) > 0 
           append rest(right) to result
       return result




The basic idea is to split the collection into smaller groups by halving it until the groups only have one element or no elements (which are both entirely sorted groups). Then merge the groups back together so that their elements are in order. This is how the algorithm gets its "divide and conquer" description.
Write a function to sort a collection of integers using the merge sort. The merge sort algorithm comes in two parts: a sort function and a merge function. The functions in pseudocode look like this:
function mergesort(m)
   var list left, right, result
   if length(m) â¤ 1
       return m
   else
       var middle = length(m) / 2
       for each x in m up to middle - 1
           add x to left
       for each x in m at and after middle
           add x to right
       left = mergesort(left)
       right = mergesort(right)
       if last(left) â¤ first(right)
          append right to left
          return left
       result = merge(left, right)
       return result

function merge(left,right)
   var list result
   while length(left) > 0 and length(right) > 0
       if first(left) â¤ first(right)
           append first(left) to result
           left = rest(left)
       else
           append first(right) to result
           right = rest(right)
   if length(left) > 0
       append rest(left) to result
   if length(right) > 0
       append rest(right) to result
   return result





QUICKSORT


#  Time Complexity of Solution: Best = Average = O(nlog(n)); Worst = O(n^2).
#
#  Approach:
#  Quicksort.....for contrast, recall that merge sort
#  first partitions an array into smaller pieces, then sorts each piece,
#  then merge the pieces back. Quicksort actually sorts the array
#  during the partition phase.
#
#  Quicksort works by selecting an element called a pivot and splitting
#  the array around that pivot such that all the elements in, say, the
#  left sub-array are less than pivot and all the elements in the right
#  sub-array are greater than pivot. The splitting continues until the
#  array can no longer be broken into pieces. 
#
# Their time complexity is about the same...butquicksort is better than
#    mergesort if you consider memory usage..it's is an in-place
#    algorithm.
#=======================================================================

    def quicksort( aList ):
        _quicksort( aList, 0, len( aList ) - 1 )
    def _quicksort( aList, first, last ):
        if first < last:
          pivot = partition( aList, first, last )
          _quicksort( aList, first, pivot - 1 )
          _quicksort( aList, pivot + 1, last )
    def partition( aList, first, last ) :
        pivot = first + random.randrange( last - first + 1 )
        swap( aList, pivot, last )
        for i in range( first, last ):
          if aList[i] <= aList[last]:
            swap( aList, i, first )
            first += 1
        swap( aList, first, last )
        return first
    def swap( A, x, y ):
      tmp = A[x]
      A[x] = A[y]
      A[y] = tmp





#
#  Time Complexity of Solution:
#  Best O(nlog(n)); Average O(nlog(n)); Worst O(nlog(n)).
#
#  Approach:
#  Heap sort happens in two phases. In the first phase, the array
#  is transformed into a heap. A heap is a binary tree where
#  1) each node is greater than each of its children
#  2) the tree is perfectly balanced
#  3) all leaves are in the leftmost position available.
#  In phase two the heap is continuously reduced to a sorted array:
#  1) while the heap is not empty
#  - remove the top of the head into an array
#  - fix the heap.
#  Heap sort was invented by John Williams not by B. R. Heap.
#
#  MoveDown:
#  The movedown method checks and verifies that the structure is a heap.
#
#  Technical Details:
#  A heap is based on an array just as a hashmap is based on an
#  array. For a heap, the children of an element n are at index
#  2n+1 for the left child and 2n+2 for the right child.
#
#  The movedown function checks that an element is greater than its
#  children. If not the values of element and child are swapped. The
#  function continues to check and swap until the element is at a
#  position where it is greater than its children.
#=======================================================================

    def heapsort( aList ):
      # convert aList to heap
      length = len( aList ) - 1
      leastParent = length / 2
      for i in range ( leastParent, -1, -1 ):
        moveDown( aList, i, length )
      # flatten heap into sorted array
      for i in range ( length, 0, -1 ):
        if aList[0] > aList[i]:
          swap( aList, 0, i )
          moveDown( aList, 0, i - 1 )
    def moveDown( aList, first, last ):
      largest = 2 * first + 1
      while largest <= last:
        # right child exists and is larger than left child
        if ( largest < last ) and ( aList[largest] < aList[largest + 1] ):
          largest += 1
        # right child is larger than parent
        if aList[largest] > aList[first]:
          swap( aList, largest, first )
          # move down to largest child
          first = largest;
          largest = 2 * first + 1
        else:
          return # force exit
    def swap( A, x, y ):
      tmp = A[x]
      A[x] = A[y]
      A[y] = tmp









bubble sort - Because of its abysmal O(n2) performance, it is not used often for large (or even medium-sized) datasets.
insertion sort - it moves data around too much. Each time an insertion is made, all elements in a greater position are shifted.
Selection sort - is a step up from insertion sort in terms of memory - only swaps elements that need it. In terms of time complexity, however, insertion sort is better.



The bubble sort works by passing sequentially over a list, comparing each value to the one immediately after it. If the first value is greater than the second, their positions are switched. 

# Time Complexity of Solution: Best O(n^2); Average O(n^2); Worst O(n^2).
#
#  Approach:
#
#  0] For each element at index i from 0 to n, loop:
#  1] For each element at index k, from n to i exclusive, loop:
#  2] If the element at k is less than that at k-1, swap them.
#=======================================================================

    def bubblesort( A ):
      for i in range( len( A ) ):
        for k in range( len( A ) - 1, i, -1 ):
          if ( A[k] < A[k - 1] ):
            swap( A, k, k - 1 )
    def swap( A, x, y ):
      tmp = A[x]
      A[x] = A[y]
      A[y] = tmp

Insertion Sort

Time Complexity of Solution: Best O(n); Average O(n^2); Worst O(n^2).

Insertion sort is good for collections that are very small or nearly sorted. 
Otherwise it's not a good sorting algorithm: it moves data around too much. 
Each time an insertion is made, all elements in a greater position are shifted.

    def insertionsort( aList ):
      for i in range( 1, len( aList ) ):
        tmp = aList[i]
        k = i
        while k > 0 and tmp < aList[k - 1]:
            aList[k] = aList[k - 1]
            k -= 1
        aList[k] = tmp






Time Complexity of Solution: Best O(n^2); Average O(n^2); Worst O(n^2).

Approach:
Selection sort is a step up from insertion sort from a memory viewpoint.  It only swaps elements that need to be swapped. In terms of time complexity, however, insertion sort is better.


    def selectionsort(aList):
      for i in range(len(aList)):
        least = i
        for k in range(i + 1, len(aList)):
          if aList[k] < aList[least]:
            least = k

        swap(aList, least, i)


    def swap(A, x, y):
      tmp = A[x]
      A[x] = A[y]
      A[y] = tmp


Selection Sort
The algorithm proceeds by finding the smallest (or largest, depending on sorting order) element in the unsorted sublist, exchanging it with the leftmost unsorted element (putting it in sorted order), and moving the sublist boundaries one element to the right.
64 25 12 22 11
11 25 12 22 64
11 12 25 22 64
11 12 22 25 64
11 12 22 25 64


But what if we improve the data structure? It takes O(1) time to remove a
particular item from an unsorted array once it has been located, but O(n) time
to find the smallest item. These are exactly the operations supported by priority
queues. So what happens if we replace the data structure with a better priority
queue implementation, either a heap or a balanced binary tree? Operations within
the loop now take O(log n) time each, instead of O(n). Using such a priority queue
implementation speeds up selection sort from O(n2 ) to O(n log n).
The name typically given to this algorithm, heapsort, obscures the relationship
between them, but heapsort is nothing but an implementation of selection sort
using the right data structure.

Recursive algorithms reduce large problems into smaller ones. A recursive approach
to sorting involves partitioning the elements into two groups, sorting each of the
smaller problems recursively, and then interleaving the two sorted lists to totally
order the elements. This algorithm is called mergesort, recognizing the importance





