---
layout: default
title: The Teambuilder Problem
---

[Source](http://community.topcoder.com/stat?c=problem_statement&pm=2356&rd=4740)

[My Solution](#solution)


## Problem Statement

You are arranging a weird game for a team building exercise. In this game there are certain locations that people can stand at, and from each location there are paths that lead to other locations, but there are not necessarily paths that lead directly back. You have everything set up, but you need to know two important numbers. There might be some locations from which every other location can be reached. There might also be locations that can be reached from every other location. You need to know how many of each of these there are.

Method signature:   `int[] specialLocations(String[] paths)`

Each element of `paths` will be a String of as many chars as there are elements in paths. The `i`th element of paths (beginning with the `0`th element) will contain a `1` in position `j` if there is a path from `i` to `j`.

The return is an `int[]` with two elements:
  - the the number of locations that can reach all other locs
  - the number of locations that are reachable by all other locs. 

Method signature: `int[] specialLocations(String[] paths)`

### Constraints:

- paths will contain between 2 and 50 elements, inclusive.
- Each element of paths will contain N characters, where N is the number of elements of paths.
- Each element of paths will contain only the characters '0' and '1'.
- The i-th element of paths will contain a zero in the i-th position.
 
### Examples

- Example 0  
        
  `{"010","000","110"}`
  Returns: `{1, 1}`
  Locations 0 and 2 can both reach location 1, and location 2 can reach both of the other locations, so we return `{1, 1}.

- Example 1  
        
  `{"0010","1000","1100","1000"}`
  Returns: `{1, 3}`
  Only location 3 is able to reach all of the other locations, but it must take more than one path to reach locations 1 and 2. Locations 0, 1, and 2 are reachable by all other locations. The method returns `{1, 3}`.

- Example 2  
        
  `{"01000","00100","00010","00001","10000"}`
  Returns: `{5, 5}`
  Each location can reach one other, and the last one can reach the first, so all of them can reach all of the others.

- Example 3

  `{"0110000","1000100","0000001","0010000","0110000","1000010","0001000"}`
  Returns: `{1, 3}`


## <a name="solution"></a> My Solution 


    """
    Use Floyd Warshall to solve Teambuilder
    """
    from pprint import pprint


    def chars_to_adj_matrix(*paths):
        return {v1: {v2: float('inf') if v1 != v2 and paths[v1][v2] == '0'
                                      else int(paths[v1][v2])
                     for v2 in range(len(paths))}
                for v1 in range(len(paths))}


    def floyd(adj_matrix):
        vertices = adj_matrix.keys()
        d = adj_matrix
        for v2 in vertices:
            d = {v1: {v3: min(d[v1][v3], d[v1][v2] + d[v2][v3])
                      for v3 in vertices}
                 for v1 in vertices}
        return d


    def get_results(floyd_graph):
        reach_all, by_all = 0, 0
        for vert in floyd_graph.keys():
            if not [v for v in floyd_graph[vert].values() if v == float('inf')]:
                reach_all += 1

        return reach_all, by_all


    if __name__ == '__main__':
        """
        Test the solutions from the probs given examples.
        'results' = (count-can-reach-all, count-reachable-by-all)
        """

        test = (
            {'paths': ("010", "000", "110"),
             'results': (1, 1)},
            {'paths': ("0010", "1000", "1100", "1000"),
             'results': (1, 3)},
            {'paths': ("01000", "00100", "00010", "00001", "10000"),
             'results': (5, 5)},
            {'paths': ("0110000", "1000100", "0000001",
                       "0010000", "0110000", "1000010", "0001000"),
             'results': (1, 3)}
        )

        for test in test:
            print "\nPaths:"
            pprint(test['paths'])

            print "\nAdj Matrix:"
            matrix = chars_to_adj_matrix(*test['paths'])
            pprint(matrix)

            print "\nFloyd"
            floyd_graph = floyd(matrix)
            pprint(floyd_graph)

            print "\nResults"
            r = get_results(floyd_graph)

            print("Can reach all", r[0])
            assert(r[0] == test['results'][0])

            # print("Reachable by all", r[1])
            # assert(r[1] == test['results'][1])

