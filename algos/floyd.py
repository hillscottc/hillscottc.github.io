"""
My implementation and utils for the Floyd Warshall Algorithm.

(Floyd finds cost of shortest path between every
pair of vertices in a weighted graph.)
"""


def adj(g):
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


