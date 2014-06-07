# Big-Oh

When we look at input sizes large enough to make only the order of growth of the running time relevant, we are studying the asymptotic efficiency of algorithms. That is, we are concerned with how the running time of an algorithm increases with the size of the input in the limit, as the size of the input increases without bound. Usually, an algorithm that is asymptotically more efficient will be the best choice for all but very small inputs.

The formal definitions for Big Oh notation are as follows:

> `O (g(n))` **Big-Oh**. Upper bound. Worst case.  
> `Ω (g(n))` **Big-Omega**. Lower bound. Best case, and  
> `Θ (g(n))` **Big-Theta**. Bounded upper and lower.  


    Constant     f(n) = 1       No dependence on n.
    Logarithmic  f(n) = log n   Binary searches.
    Linear       f(n) = n       Each elem once. (Max, Min, Avg)
    Superlinear  f(n) = n log n Mergesort and Quicksort. Grows slightly faster than linear.
    Quadratic    f(n) = n^2     Items in pairs. 
    Cubic        f(n) = n^3     Items in trips.
    Exponential  f(n) = 2^n     All subsets of n items.
    Factorial    f(n) = n!      All permutations of n items


![Big Oh Chart][big_oh_chart]


### Sort Algortitm speeds 

    Most of em :  O(   n^2    )
    Merge      :  O( n log(n) )


### Search operation complexity, by structure

    Array/List       :  O(   n    )
    Trees            :  O( log(n) )
    Adj List         :  O(  |V|   )  # num vertices
    Adj Matrix       :  O(   1    ) 
    Incidece List    :  O(  |E|   )  # num edges
    Incidence Matrix :  O(  |E|   )


### Array, hash by ints, hash by strings

Given strings A, B, and C.

- array

        str[3] data;  
        data = [A, B, C];


    > exists = O(n), get_by_pos = O(1), get_by_val = O(n)  


- hash by seq of ints

        hash{int:str} data;
        data = {0:A, 1:B, 2:C};

    > exists = O(n), get_by_pos = O(1), get_by_val = O(n)  


- hash with strings

        hash{str:str} data;
        data = {A:A, B:B, C:C};

    > exists = O(1)  
    > get_by_pos = O(n), if keys are NOT sorted. Otherwise, O(1)  
    > get_by_val = O(1), because val is the same as key.


basic data structures
![basic structures complexity img][data_sets]

heaps
![heap complexity img][heaps]

graphs
![graphs complexity img][graphs]


[big_oh_chart]: /img/big-oh-chart.png
[data_sets]: imgs/complexity-ds.png
[heaps]: imgs/complexity-heaps.png
[graphs]: imgs/complexity-graphs.png






