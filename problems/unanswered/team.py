def make_adj(*rows):
    graph = {}
    for i in range(len(rows)):
        nodes = graph.setdefault(i, {})
        for j in range(len(rows[i])):
            nodes[j] = int(rows[i][j])

    return graph


def floyd(g):
    """The Floyd-Warshall...shortest paths for all vertices."""
    vertices = g.keys()

    d = g
    for v2 in vertices:
        d = {v1: {v3: min(d[v1][v3], d[v1][v2] + d[v2][v3])
                  for v3 in vertices}
             for v1 in vertices}
    return d


# def get_results(graph):
#     """returns (count-can-reach-all, count-reachable-by-all)"""
#     reach_all, by_all = 0, 0
#     for k, v in graph.iteritems():
#         if len(v) == len(graph) - 1:
#             print k, 'can reach all other items.'
#             reach_all += 1
#         if graph[k]
#     return reach_all, by_all


if __name__ == '__main__':
    from pprint import pprint

    # From the probs given examples, as (paths, returns),
    # where returns is (count-can-reach-all, count-reachable-by-all)
    test_data = (
        {'paths': ("010", "000", "110"), 'results': (1, 1)},
        {'paths': ("0010", "1000", "1100", "1000"), 'results': (1, 3)},
        # {'paths': ("01000", "00100","00010", "00001", "10000"), 'results': (5, 5)},
        # {'paths': ("0110000", "1000100", "0000001", "0010000", "0110000",
        #   "1000010", "0001000"), 'results': (1, 3)}
    )

    for test in test_data:

        print "\nPaths:"
        pprint(test['paths'])

        graph = make_adj(*test['paths'])
        print "\nGraph:"
        pprint(graph)

        all_shortest = floyd(graph)
        print "\nFloyd:"
        pprint(all_shortest)




        # for k, v in graph.iteritems():
        #     if not v:
        #         print k, 'can visit no other items.'
        #     elif len(v) == len(graph) - 1:
        #         print k, 'can visit all other items.'


