---
layout: default
title: Problems Notes
---


### Word Ladder

Make collection of nodes that are different by one letter. Turn that into adjacency lists for each word. That would be the tricky part get right. But from there, do a breadth-first search to find the closest. 

    def bfs_iter(graph, start, visited=None):
        visited = [] if not visited else visited
        q = [start]
        while q:
            v = q.pop(0)
            if not v in visited:
                visited = visited + [v]
                q = q + graph[v]
        return visited

Or to get the total faster, could use Dijkstra's Algo. (mention) 


Problems still to think:
- dags

Problems tricky, double check:
- convex hull
- skyline
- sorts
- maze
- knapsack




## By Topic:

- BFS. (best for first match?)
    - word_find
    - bacon
- DFS. 
    - knight
- Dynamic / Optimization
    - coins
    - least common substring, sequence
    - word_find
- Text 
    - word find
    - cmpd_words
    - cyclical words
    - joined_string
    - tagalog
    - word_ladder
- DAGs
    - 


Some good questions here:
- http://interactivepython.org/courselib/static/pythonds/index.html
- http://leetcode.com/
- http://xorswap.com/
- http://topcoder.com


### The Kevin Bacon problem... a graph with an adjacency list representation

    graph = {
         '1': ['2', '3', '4'],
        '2': ['5', '6'],
        '5': ['9', '10'],
        '4': ['7', '8'],
        '7': ['11', '12']}


### Other problems...


- Dynamic: 
    - SRM 150 - Div 1 1000 - RoboCourier
    - SRM 194 - Div 1 1000 - IslandFerries
    - SRM 198 - Div 1 500 - DungeonEscape
    - TCCC '04 Round 4 - 500 - Bombman


### Longest Common Substring.

    """
    http://stackoverflow.com/questions/2892931/longest-common-substring-from-more-than-two-strings-python
    """
    def long_substr(data):
        substr = ''
        if len(data) > 1 and len(data[0]) > 0:
            for i in range(len(data[0])):
                for j in range(len(data[0])-i+1):
                    if j > len(substr) and all(data[0][i:i+j] in x for x in data):
                        substr = data[0][i:i+j]
        return substr


- Convex Hull
Problem: Find smallest polygon enclosing n points on plane.
Algo: For each pair of points p1 and p2, determine whether all other points lie to the same side of a straight line through p1 and p2


- Mazes 
Naturally represented by graphs, where each graph vertex denotes a junction of the maze, and each graph edge denotes a hallway in the maze. Thus, any graph traversal algorithm must be powerful enough to get us out of an arbitrary maze. For efficiency, we must make sure we don’t get trapped in the maze and visit the same place repeatedly. For correctness, we must do the traversal in a systematic way to guarantee that we get out of the maze. Our search must take us through every edge and vertex in the graph.

- Test indexing
    You want to find the 10 most popular words in the entire publication of the Wall Street Journal (WSJ). Someone generous has spent the time digitizing the entire WSJ catalog and loading it onto hard disks. It's so big that we don't have space for it on a single machine so it's been split up into pieces onto N machines such that each machine has a separate piece of the entire catalog as a text file. The switch connecting the machines only allows for two machines to communicate at once.
    
    a. First write an indexing function for the text file on a single machine. It should be able to read the entire file and be able to store a count for the number of times each word in the file has been seen. 
    
    Example: If the text file contained "Little bunny foo foo", your index should be able to tell you that "little" appeared one time, "bunny" appeared once, and "foo" appeared twice.
    
    Brainstorming questions: Which data structure would you use and why? Is it efficient with time and memory? Does it give you easy access to the data you put in it?
    
    b. Your next task is to use the populated index on each machine to find the 10 most popular words in the whole WSJ. Remember that the machines can communicate over that switch, but only two at a time.
    
    Let's pretend that someone has written all the networking code for you. You don't have to worry about how to make the machines talk to each other. You can just write a function which takes in the index data structure from two different machines and do interesting things with them. You need to write a function which can go through all the indices you created in the previous step and merge them into a single index.
    
    c. The final part is to write a function to traverse the final aggregated index to find the top 10 (or N) words in the WSJ.


- Given a set of 2-dimensional points, compute a skyline. This was easy. I drew upon a common data structure known as a max heap.

    (a) Report the order of the vertices encountered on a breadth-first search starting
    from vertex A. Break all ties by picking the vertices in alphabetical order (i.e.,
    A before Z).
    (b) Report the order of the vertices encountered on a depth-first search starting
    from vertex A. Break all ties by picking the vertices in alphabetical order (i.e.,
    A before Z).


- Consider a set of movies M1 , M2 , . . . , Mk . 
    There is a set of customers, each one
    of which indicates the two movies they would like to see this weekend. Movies are
    shown on Saturday evening and Sunday evening. Multiple movies may be screened
    at the same time.

    You must decide which movies should be televised on Saturday and which on Sun-
    day, so that every customer gets to see the two movies they desire. Is there a
    schedule where each movie is shown at most once? Design an efficient algorithm to
    find such a schedule if one exists.


