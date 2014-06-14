---
layout: default
title: The KiloManX Problem
---

TopCoder [problem "KiloManX"](http://topcoder.bgcoder.com/print.php?id=487) used in SRM 181 (Division I Level Three)

See Answer Discussion, below.

## Problem Statement
        
The KiloMan series has always had a consistent pattern: you start off with one (rather weak) default weapon, and then defeat some number of bosses. When you defeat a boss, you then acquire his weapon, which can then be used against other bosses, and so on. Usually, each boss is weak against some weapon acquired from another boss, so there is a recommended order in which to tackle the bosses. You want to get more efficient playing the game. 

Your metric for efficiency is the total number of weapon shots fired to defeat all of the bosses. You have a chart in front of you detailing how much damage each weapon does to each boss per shot, and you know how much health each boss has. When a boss's health is reduced to 0 or less, he is defeated. 

You start off only with the Kilo Buster, which does 1 damage per shot to any boss. The chart is represented as a String[], with the ith element containing N one-digit numbers ('0'-'9'), detailing the damage done to bosses 0, 1, 2, ..., N-1 by the weapon obtained from boss i, and the health is represented as a int[], with the ith element representing the amount of health that boss i has.

Given a String[] damageChart representing all the weapon damages, and a int[] bossHealth showing how much health each boss has, your method should return an int which is the least number of shots that need to be fired to defeat all of the bosses.

Method signature: `int leastShots(String[] damageChart, int[] bossHealth)`


### Constraints

-   damageChart will contain between 1 and 15 elements, inclusive.
-   each element of damageChart will be of the same length, which will be the same as the number of elements in damageChart.
-   each element of damageChart will contain only the characters '0'-'9'.
-   bossHealth will contain between 1 and 15 elements, inclusive.
-   damageChart and bossHealth will contain the same number of elements.
-   each element in bossHealth will be between 1 and 1000000, inclusive.
 
### Examples

- Example 0
      
        {"070","500","140"}
        {150,150,150}
        Returns: 218

    The best way to go is to use the KiloBuster to defeat boss 2 (indexed from 0), then use the weapon from boss 2 to defeat boss 1, and then use the weapon from boss 1 to defeat boss 0. This leads to total damage of 150 + 38 + 30 = 218.


- Example 1  
        
        {"1542", "7935", "1139", "8882"}
        {150,150,150,150}
        Returns: 205

Defeat boss 2, use his weapon to defeat boss 3, and then use boss 3's weapon to defeat both bosses 0 and 1, for a total shot count of 150 + 17 + 19 + 19 = 205. It would be more efficient to defeat boss 1 with his own weapon, but it would be cheating to get his weapon before defeating him.

- Example 2
        
        {"07", "40"}
        {150,10}
        Returns: 48

- Example 3 
        
        {"198573618294842",
         "159819849819205",
         "698849290010992",
         "000000000000000",
         "139581938009384",
         "158919111891911",
         "182731827381787",
         "135788359198718",
         "187587819218927",
         "185783759199192",
         "857819038188122",
         "897387187472737",
         "159938981818247",
         "128974182773177",
         "135885818282838"}
        {157, 1984, 577, 3001, 2003, 2984, 5988, 190003,
        9000, 102930, 5938, 1000000, 1000000, 5892, 38}
        Returns: 260445

- Example 4
        
        {"02111111", "10711111", "11071111", "11104111",
         "41110111", "11111031", "11111107", "11111210"}
        {28,28,28,28,28,28,28,28}
        Returns: 92


## Answer Discussion

[From a TopCoders Tutorial](http://community.topcoder.com/tc?module=Static&d1=tutorials&d2=graphsDataStrucs3)

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



