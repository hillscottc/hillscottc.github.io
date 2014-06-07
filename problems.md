
### Problems


Got:
- coin change. dynamic. optimization.
- bacon. 
    - edge list hash


- [least common substring](tries.md)
-


Problems still to think:
- dags

Problems tricky, double check:
- bacon
- convex hull
- skyline
- sorts
- maze
- knapsack


Some good questions here:
- http://interactivepython.org/courselib/static/pythonds/index.html
- http://leetcode.com/
- http://xorswap.com/
- http://topcoder.com


Find the only number that occurs an odd number of times in a list
- same as parens. use a stack. push


### The Kevin Bacon problem... a graph with an adjacency list representation

    graph = {
         '1': ['2', '3', '4'],
        '2': ['5', '6'],
        '5': ['9', '10'],
        '4': ['7', '8'],
        '7': ['11', '12']}

### Convex Hull
Problem: Find smallest polygon enclosing n points on plane.
Algo: For each pair of points p1 and p2, determine whether all other points lie to the same side of a straight line through p1 and p2


### Mazes are naturally represented by graphs, where each graph vertex denotes a junction of the maze, and each graph edge denotes a hallway in the maze. Thus, any graph traversal algorithm must be powerful enough to get us out of an arbitrary maze. For efficiency, we must make sure we don’t get trapped in the maze and visit the same place repeatedly. For correctness, we must do the traversal in a systematic way to guarantee that we get out of the maze. Our search must take us through every edge and vertex in the graph.

2. You want to find the 10 most popular words in the entire publication of the Wall Street Journal (WSJ). Someone generous has spent the time digitizing the entire WSJ catalog and loading it onto hard disks. It's so big that we don't have space for it on a single machine so it's been split up into pieces onto N machines such that each machine has a separate piece of the entire catalog as a text file. The switch connecting the machines only allows for two machines to communicate at once.

a. First write an indexing function for the text file on a single machine. It should be able to read the entire file and be able to store a count for the number of times each word in the file has been seen.

Example: If the text file contained "Little bunny foo foo", your index should be able to tell you that "little" appeared one time, "bunny" appeared once, and "foo" appeared twice.

Brainstorming questions: Which data structure would you use and why? Is it efficient with time and memory? Does it give you easy access to the data you put in it?

b. Your next task is to use the populated index on each machine to find the 10 most popular words in the whole WSJ. Remember that the machines can communicate over that switch, but only two at a time.

Let's pretend that someone has written all the networking code for you. You don't have to worry about how to make the machines talk to each other. You can just write a function which takes in the index data structure from two different machines and do interesting things with them. You need to write a function which can go through all the indices you created in the previous step and merge them into a single index.

c. The final part is to write a function to traverse the final aggregated index to find the top 10 (or N) words in the WSJ.

Followups:
What's the runtime of each of your functions?
What's the runtime of the overall algorithm?
How does the switch limit your ability to compute the answer? If you could modify the switch, what changes would you want to make?
Do you have any concerns about memory consumption? (hint: you probably should) How could you optimize to use less memory?


 Given a set of 2-dimensional points, compute a skyline. This was easy. I drew upon a common data structure known as a max heap.

 


(a) Report the order of the vertices encountered on a breadth-first search starting
from vertex A. Break all ties by picking the vertices in alphabetical order (i.e.,
A before Z).
(b) Report the order of the vertices encountered on a depth-first search starting
from vertex A. Break all ties by picking the vertices in alphabetical order (i.e.,
A before Z).


[5] Consider a set of movies M1 , M2 , . . . , Mk . There is a set of customers, each one
of which indicates the two movies they would like to see this weekend. Movies are
shown on Saturday evening and Sunday evening. Multiple movies may be screened
at the same time.
You must decide which movies should be televised on Saturday and which on Sun-
day, so that every customer gets to see the two movies they desire. Is there a
schedule where each movie is shown at most once? Design an efficient algorithm to
find such a schedule if one exists.



Interview Problems
5-31. [3] Which data structures are used in depth-first and breath-first search?
5-32. [4] Write a function to traverse binary search tree and return the ith node in sorted
order.

