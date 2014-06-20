---
layout: default
title: Solution to Teambuilder Problem
---

[Teambuilder Problem](teambuilder.html)

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
