---
layout: page
title: Sorting
group: programming
---

## Bubble Sort

Because of its abysmal O(n2) performance, it is not used often for large (or even medium-sized) datasets.

The bubble sort works by passing sequentially over a list, comparing each value, and switching them if neccess.

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


## Insertion Sort

Moves data around too much. Each time an insertion is made, all elements in a greater position are shifted.

Time Complexity of Solution: Best O(n); Average O(n^2); Worst O(n^2).

    def insertionsort( aList ):
      for i in range( 1, len( aList ) ):
        tmp = aList[i]
        k = i
        while k > 0 and tmp < aList[k - 1]:
            aList[k] = aList[k - 1]
            k -= 1
        aList[k] = tmp



## Selection Sort

A step up from insertion sort in terms of memory - only swaps elements that need it. 
In terms of time complexity, however, insertion sort is better.

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



## Merge Sort
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



## QuickSort

Time Complexity of Solution: Best = Average = O(nlog(n)); Worst = O(n^2).

Quicksort.....for contrast, recall that merge sort
first partitions an array into smaller pieces, then sorts each piece,
then merge the pieces back. Quicksort actually sorts the array
during the partition phase.

Quicksort works by selecting an element called a pivot and splitting
the array around that pivot such that all the elements in, say, the
left sub-array are less than pivot and all the elements in the right
sub-array are greater than pivot. The splitting continues until the
array can no longer be broken into pieces. 

Their time complexity is about the same...but quicksort is better than 
mergesort if you consider memory usage..it's is an in-place algorithm.


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





