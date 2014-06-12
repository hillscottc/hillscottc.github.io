### KiloManX, Ammo Problem

From TopCoders

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



