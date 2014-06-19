

def adj(g):
    """
    Convert a directed graph to an adjacency matrix.
    >>> g = {1: {2: 3, 3: 8, 5: -4},
    ...      2: {4: 1, 5: 7},
    ...      3: {2: 4},
    ...      4: {1: 2, 3: -5},
    ...      5: {4: 6}}
    >>> adj(g) # doctest: +NORMALIZE_WHITESPACE
    {1: {1: 0, 2: 3, 3: 8, 4: inf, 5: -4},
     2: {1: inf, 2: 0, 3: inf, 4: 1, 5: 7},
     3: {1: inf, 2: 4, 3: 0, 4: inf, 5: inf},
     4: {1: 2, 2: inf, 3: -5, 4: 0, 5: inf},
     5: {1: inf, 2: inf, 3: inf, 4: 6, 5: 0}}
    """
    vertices = g.keys()
    return {v1: {v2: 0 if v1 == v2 else g[v1].get(v2, float('inf'))
                 for v2 in vertices}
            for v1 in vertices}


def paths_to_list(paths):
    return {v1: {v2:  0 if v1 == v2 else g[v1].get(v2, float('inf'))
                 for v2 in range(len(paths))}
            for v1 in range(len(paths))}


# def floyd(graph):
#     """The Floyd-Warshall...shortest paths for all vertices."""
#     vertices = graph.keys()
#     fg = graph
#     for v2 in vertices:
#         fg = {v1: {v3: min(fg[v1][v3], fg[v1][v2] + fg[v2][v3])
#                   for v3 in vertices}



if __name__ == '__main__':
    from pprint import pprint

    # From the probs given examples, as (paths, returns),
    # where returns is (count-can-reach-all, count-reachable-by-all)
    test = (
        {'paths': ("010", "000", "110"), 'results': (1, 1)},
        {'paths': ("0010", "1000", "1100", "1000"), 'results': (1, 3)},
        # {'paths': ("01000", "00100","00010", "00001", "10000"), 'results': (5, 5)},
        # {'paths': ("0110000", "1000100", "0000001", "0010000", "0110000",
        #   "1000010", "0001000"), 'results': (1, 3)}
    )


    matrix = paths_to_list(test[0]['paths'])

    pprint(matrix)

    # for test in test_data:
    #     print "\nPaths:"
    #     pprint(test['paths'])
    #     graph = make_adj(*test['paths'])
    #     print "\nGraph:"
    #     pprint(graph)


    # pprint(adj(*paths))
    # print floyd(make_adj(*paths))

    # fg = floyd(graph)
    # print "\nFloyd:"
    # pprint(fg)

    # reach_all, by_all = 0, 0
    # for key, nodes in fg.iteritems():
    #     print "sum of %s is %d" % (key, sum([1 for v in nodes.values() if v == 0]))


