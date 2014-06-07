# Trees

- A tree is an undirected graph that is connected and acyclic.
- Search is a factor of height.

- A tree cannot have a loop.

- Many kinds by tweaking the balance, height, or adding props like color, etc.

- Dijkstras Algorithm for shortest path is used for many solutions.
  <script src="https://gist.github.com/hillscottc/7d2e17c59d96e26ec855.js"></script>


## Binary Search Trees

A node-based data structure where:

- Each node has a comparable key
- Each node has no more than two child nodes.
- The left sub-tree contains only nodes with keys less than the parent node.
- The right sub-tree contains only nodes with keys greater than the parent node.

Operations include:
- SEARCH
- MIN / MAX
- PREDECESSOR / SUCCESSOR
- INSERT / DELETE


## Suffix Trees

Suffix trees can be used to solve *longest common substring* problems.

Given strings "ABAB" and "BABA", the matrix would look like:

        |   |   | A | B | A | B |
        |   | O | O | O | O | O |
        | B | O | O | 1 | O | 1 |
        | A | O | 1 | 0 | 2 | 0 |
        | B | O | 0 | 2 | 0 | 3 |
        | A | O | 1 | 0 | 3 | 0 |


In this matrix, the 5th column tests the substring ABA of the ABAB sequence.
So cell [5, 5] compares ABA to BAB ... the lcs is BA, length 2.


The other approach is to construct a generalized suffix tree for the strings, 
then find the deepest internal nodes which have leaf nodes from all the strings in the subtree below it.

## *Tries*, for text problems.



![suffix tree img][suffix_tree]

A Simple Suffix Tree Implementation:
<script src="https://gist.github.com/hillscottc/f0460657daca55f95b62.js"></script>

Or, here's a [more complete version][suffix_tree_big].

### What is a Trie?

[Tries on TopCoder][tries1]

- The tries can insert and find strings in O(L) time (where L represent the length of a single word). 
- The trie is a tree where each vertex represents a single word or a prefix.
- The root represents an empty string (""), the vertexes that are direct sons of the root represent prefixes of length 1, the vertexes that are  2 edges of distance from the root represent prefixes of length 2, the vertexes that are 3 edges of distance from the root represent prefixes of length 3 and so on. In other words, a vertex that are k edges of distance of the root have an associated prefix of length k.
- Let v and w be two vertexes of the trie, and assume that v is a direct father of w, the\n v must have an associated prefix of w.

The next figure shows a trie with the words "tree", "trie", "algo", "assoc", "all", and "also."

![trie nodes][trie_nodes]

### Coding a Trie

Trie from StackOverflow
<script src="https://gist.github.com/hillscottc/d60e7fbe714a6a4b8f9b.js"></script>


### Problems to Practice:

- WordFind SRM 232
- SearchBox SRM 361
- CyclicWords SRM 358
- TagalogDictionary SRM 342
- JoinedString SRM 302
- CmpdWords SRM 268




# Graphs

[TopCoder Graphs][topcoder_graphs]

Graphs are a fundamental data structure in the world of programming. 

Knowing the correct data structures to use with graph problems is critical. A problem that appears intractable may prove to be a few lines with the proper data structure.

While a tree only allows a node to have children, and there cannot be any loops in the tree, with a more general graph we can represent many different situations.

A very common example used is flight paths between cities. If there is a flight between city A and city B there is an edge between the cities. The *cost* of the edge can be the length of time that it takes for the flight, or perhaps the amount of fuel used.

    structure node
       [list of nodes] neighbors
       [data]
    end

    cost(X, Y) := if (X.neighbors contains Y) return X.neighbors[Y];
             else "Not possible"


### Recognizing a graph problem:

Some common keywords associated with graph problems are: vertices, nodes, edges, connections, connectivity, paths, cycles and direction.

An example of a description of a simple problem that exhibits some of these characteristics is:

"Bob has become lost in his neighborhood. He needs to get from his current position back to his home. Bob's neighborhood is a 2 dimensional grid, that starts at (0, 0) and (width - 1, height - 1). There are empty spaces upon which bob can walk with no difficulty, and houses, which Bob cannot pass through. Bob may only move horizontally or vertically by one square at a time.""

Bob's initial position will be represented by a 'B' and the house location will be represented by an 'H'. Empty squares on the grid are represented by '.' and houses are represented by 'X'. Find the minimum number of steps it takes Bob to get back home, but if it is not possible for Bob to return home, return -1.

An example of a neighborhood of width 7 and height 5:

    ...X..B
    .X.X.XX
    .H.....
    ...X...
    .....X."

Once you have recognized that the problem is a graph problem it is time to start building up your representation of the graph in memory.


### Singly linked lists

An example of one of the simplest types of graphs is a singly linked list! Now we can start to see the power of the graph data structure, as it can represent very complicated relationships, but also something as simple as a list.
A singly linked list has one "head" node, and each node has a link to the next node. So the structure looks like this:

    structure node
       [node] link;
       [data]
    end

node head;

A simple example would be:

    node B, C;
    head.next = B;
    B.next = C;
    C.next = null;

This would be represented graphically as `head -> B -> C -> null`.

The *cost function* would look as follows:

    cost(X, Y) := if (X.link = Y) return 1;
               else if (X = Y) return 0;
               else "Not possible"

This cost function represents the fact that we can only move directly to the link node from our current node. 
Get used to seeing cost functions because anytime that you encounter a graph problem you will be dealing with them in some form or another.




# Graph Traversals


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


    dfs(node start) {
        stack<node> s;
        s.push(start);
        while (s.empty() == false) {
            top = s.top();
            s.pop();

            if (top is not marked as visited) {
                check for termination condition (have we reached the node we want to?)
                mark top as visited;
                add all of top's neighbors to the stack.
            }
        }
    }



### GrafixMask problem

This problem essentially asks us to find the number of discrete regions in a grid that has been filled in with some values already. Dealing with grids as graphs is a very powerful technique, and in this case makes the problem quite easy.

We will define a graph where each node has 4 connections, one each to the node above, left, right and below. However, we can represent these connections implicitly within the grid, we need not build out any new data structures. The structure we will use to represent the grid in grafixMask is a two dimensional array of booleans, where regions that we have already determined to be filled in will be set to true, and regions that are unfilled are set to false.

To set up this array given the data from the problem is very simple, and looks something like this:


    bool fill[600][400];
    initialize fills to false;

    foreach rectangle in Rectangles
        set from (rectangle.left, rectangle.top) to (rectangle.right, retangle.bottom) to true


Now we have an initialized connectivity grid. When we want to move from grid position (x, y) we can either move up, down, left or right. When we want to move up for example, we simply check the grid position in (x, y-1) to see if it is true or false. If the grid position is false, we can move there, if it is true, we cannot.

Now we need to determine the area of each region that is left. We don't want to count regions twice, or pixels twice either, so what we will do is set fill[x][y] to true when we visit the node at (x, y). This will allow us to perform a Depth-First search to visit all of the nodes in a connected region and never visit any node twice, which is exactly what the problem wants us to do! So our loop after setting everything up will be:


    int[] result;

    for x = 0 to 599
        for y = 0 to 399
            if (fill[x][y] == false)
                result.addToBack(doFill(x,y));


All this code does is check if we have not already filled in the position at (x, y) and then calls doFill() to fill in that region. At this point we have a choice, we can define doFill recursively (which is usually the quickest and easiest way to do a depth first search), or we can define it explicitly using the built in stack classes. I will cover the recursive method first, but we will soon see for this problem there are some serious issues with the recursive method.

We will now define doFill to return the size of the connected area and the start position of the area:
    
    int doFill(int x, int y) {
        
        // Check to ensure that we are within the bounds of the grid, if not, return 0
        if (x < 0 || x >= 600) return 0;
        
        // Similar check for y
        if (y < 0 || y >= 400) return 0;
        
        // Check that we haven't already visited this position, as we don't want to count it twice
        if (fill[x][y]) return 0;

        // Record that we have visited this node
        fill[x][y] = true;

        // Now we know that we have at least one empty square, then we will recursively attempt to
        // visit every node adjacent to this node, and add those results together to return.
        return 1 + doFill(x - 1, y) + doFill(x + 1, y) + doFill(x, y + 1) + doFill(x, y - 1);
    }


## BREADTH-FIRST

Radiate from start with a **queue**

It has the extremely useful property -- if all of the edges in a graph are unweighted (or the same weight) then the first time a node is visited is the shortest path to that node from the source node.

The depth first search is well geared towards problems where we want to find any solution to the problem (not necessarily the shortest path), or to visit all of the nodes in the graph. 

The basic structure of a breadth first search will look this:

    void bfs(node start) {
        queue<node> s;
        s.push(start);
        mark start as visited
        while (s.empty() == false) {
            top = s.front();
            s.pop();

            check for termination condition (have we reached the node we want to?)

            add all of top's unvisited neighbors to the queue
            mark all of top's unvisited neighbors as visited
        }
    }


## Finding the best path through a graph

Dijkstra (Heap method)

Dijkstra using a Heap is one of the most powerful techniques to add to your TopCoder arsenal. It essentially allows you to write a Breadth First search, and instead of using a Queue you use a Priority Queue/Heap with  has a sorting func on nodes such that lowest cost nodes are on top.

This allows us to find the best path through a graph in:

> O(m * log(n)) time where n is the number of vertices and m is the number of edges in the graph.

The Heap's nice properties:

- inserting an element or removing the top element takes O(log n) time, where n is the num elems in the heap. 
- Getting the top value is an O(1) operation

Topcoders' version of djikstra:

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

Interactive Python's dijkstra imp:
<script src="https://gist.github.com/hillscottc/7d2e17c59d96e26ec855.js"></script>                


### KiloManX
For the example here we will be using KiloManX, from SRM 181, the Div 1 1000. This is an excellent example of the application of the Heap Dijkstra problem to what appears to be a Dynamic Programming question initially. In this problem the edge weight between nodes changes based on what weapons we have picked up. So in our node we at least need to keep track of what weapons we have picked up, and the current amount of shots we have taken (which will be our cost). The really nice part is that the weapons that we have picked up corresponds to the bosses that we have defeated as well, so we can use that as a basis for our visited structure. If we represent each weapon as a bit in an integer, we will have to store a maximum of 32,768 values (2^15, as there is a maximum of 15 weapons). So we can make our visited array simply be an array of 32,768 booleans. Defining the ordering for our nodes is very easy in this case, we want to explore nodes that have lower amounts of shots taken first, so given this information we can define our basic structure to be as follows:
boolean visited[32768];

    class node {
        int weapons;
        int shots;
        // Define a comparator that puts nodes with less shots on top appropriate to your language
    };

Now we will apply the familiar structure to solve these types of problems.

    int leastShots(String[] damageChart, int[] bossHealth) {
        priorityQueue pq;

        pq.push(node(0, 0));

        while (pq.empty() == false) {
            node top = pq.top();
            pq.pop();

            // Make sure we don't visit the same configuration twice
            if (visited[top.weapons]) continue;
            visited[top.weapons] = true;

            // A quick trick to check if we have all the weapons, meaning we defeated all the bosses.
            // We use the fact that (2^numWeapons - 1) will have all the numWeapons bits set to 1.
            if (top.weapons == (1 << numWeapons) - 1)
                return top.shots;

            for (int i = 0; i < damageChart.length; i++) {
                // Check if we've already visited this boss, then don't bother trying him again
                if ((top.weapons >> i) & 1) continue;

                // Now figure out what the best amount of time that we can destroy this boss is, given the weapons we have.
                // We initialize this value to the boss's health, as that is our default (with our KiloBuster).
                int best = bossHealth[i];
                for (int j = 0; j < damageChart.length; j++) {
                    if (i == j) continue;
                    if (((top.weapons >> j) & 1) && damageChart[j][i] != '0') {
                        // We have this weapon, so try using it to defeat this boss
                        int shotsNeeded = bossHealth[i] / (damageChart[j][i] - '0');
                        if (bossHealth[i] % (damageChart[j][i] - '0') != 0) shotsNeeded++;
                        best = min(best, shotsNeeded);
                    }
                }

                // Add the new node to be searched, showing that we defeated boss i, and we used 'best' shots to defeat him.
                pq.add(node(top.weapons | (1 << i), top.shots + best));
            } 
        }
    }


There are a huge number of these types of problems on TopCoder; here are some excellent ones to try out:

- SRM 150 - Div 1 1000 - RoboCourier
- SRM 194 - Div 1 1000 - IslandFerries
- SRM 198 - Div 1 500 - DungeonEscape
- TCCC '04 Round 4 - 500 - Bombman






# Directed Acyclic Graph, DAG

A directed graph with no cycles is called a directed acyclic graph or a DAG. 

In an operating system, at the most abstract level, how do you get deadlock? You have a collection of processes waiting for (dependent on) other processes. There is a cycle in the dependencies.  If you expect to finish a collection of tasks with dependencies, there can be no cyclic dependency!  

A workable dependency graph is a directed acyclic graph (DAG).

In parallel processes, tasks that do not depend on each other can be done at the same time. The chain of dependencies that takes the longest time determines the minimum time to completion. This longest time chain of dependencies is a **critical path**. 


## Topological Sorting of directed acyclic graphs (DAGs)

Topological sorting is the most important operation on directed acyclic graphs (DAGs). It orders the vertices on a line such that all directed edges go from left to right. Such an ordering cannot exist if the graph contains a directed cycle, because there is no way you can keep going right on a line and still return back to where you started from! Each DAG has at least one topological sort.

The importance of topological sorting is that it gives us an ordering to process each vertex before any of its successors. Suppose the edges represented precedence constraints, such that edge (x, y) means job x must be done before job y. Then, any topological sort defines a legal schedule.








[suffix_tree]: imgs/suffix_tree.png
[suffix_tree_big]: https://gist.github.com/hillscottc/e27f7acbc235f6a3e75d
[trie_stack]: https://gist.github.com/hillscottc/d60e7fbe714a6a4b8f9b.js
[tries1]: http://help.topcoder.com/data-science/competing-in-algorithm-challenges/algorithm-tutorials/using-tries/
[trie_nodes]: imgs/trie.png

[topcoder_graphs]: http://help.topcoder.com/data-science/competing-in-algorithm-challenges/algorithm-tutorials/introduction-to-graphs-and-their-data-structures-section-1/



