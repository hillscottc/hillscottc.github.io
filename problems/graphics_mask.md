---
layout: default
title: Graphics Mask
---

TopCoder [problem "grafixMask"](http://topcoder.bgcoder.com/print.php?id=677), Division I Level Two SRM 211 

## Problem Statement
        
In one mode of the grafix software package, the user blocks off portions of a masking layer using opaque rectangles. The bitmap used as the masking layer is 400 pixels tall and 600 pixels wide. Once the rectangles have been blocked off, the user can perform painting actions through the remaining areas of the masking layer, known as holes. To be precise, each hole is a maximal collection of contiguous pixels that are not covered by any of the opaque rectangles. Two pixels are contiguous if they share an edge, and contiguity is transitive.

You are given a `String[]` named `rectangles`, the elements of which specify the rects that have been blocked off in the masking layer. Each String in `rectangles` consists of four ints separated by single spaces. The first two ints are top left pixels, and the last two are bottom right. 

The window coords of a pixel are a pair of ints for row and col. Rows are numbered from top to bottom, 0 to 399. Cols are numbered from left to right, 0 to 599.  Rectangles contains between 1 and 50 elements.

Return an int[] containing the area, in pixels, of every hole in the resulting masking area, sorted from smallest area to greatest.
 
Method signature:  `int[] sortedAreas(String[] rectangles)`

### Examples
 
Examples 0
        
    {"0 292 399 307"}
    Returns: { 116800,  116800 }

The masking layer is depicted below in a 1:4 scale diagram.

![diag1](/img/grafixMask_diagram_1.png)

Example 1  
        
    {"48 192 351 207", "48 392 351 407", "120 52 135 547", "260 52 275 547"}
    Returns: { 22816,  192608 }

![diag2](/img/grafixMask_diagram_2.png)

Example 2
        
    {"0 192 399 207", "0 392 399 407", "120 0 135 599", "260 0 275 599"}
    Returns: { 22080,  22816,  22816,  23040,  23040,  23808,  23808,  23808,  23808 }

![diag3](/img/grafixMask_diagram_3.png)







*A Simple Dynamic Programing Problem?*

This problem essentially asks us to find the number of discrete regions in a grid that has been filled in with some values already. 

Dealing with grids as graphs is a very powerful technique, and in this case makes the problem quite easy.

We will define a graph where each node has 4 connections, one each to the node above, left, right and below. 
However, we can represent these connections implicitly within the grid, we need not build out any new data structures. 

The structure we will use to represent the grid in grafixMask is a two dimensional array of booleans, 
where regions that we have already determined to be filled in will be set to true, and regions that are unfilled are set to false.

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