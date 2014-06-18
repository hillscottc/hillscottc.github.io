def make_adj(*rows):
    graph = {}
    for i in range(len(rows)):
        nodes = graph.setdefault(i, {})
        for j in range(len(rows[i])):
            nodes[j] = rows[i][j]
            # if rows[i][j]:
            #     nodes[j] = rows[i][j]

    return graph




def floyd(graph):
    """The Floyd-Warshall...shortest paths for all vertices."""
    vertices = graph.keys()
    fg = graph
    for v2 in vertices:
        fg = {v1: {v3: min(fg[v1][v3], fg[v1][v2] + fg[v2][v3])
                  for v3 in vertices}
             for v1 in vertices}
    return fg


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

    # for test in test_data:
    #     print "\nPaths:"
    #     pprint(test['paths'])
    #     graph = make_adj(*test['paths'])
    #     print "\nGraph:"
    #     pprint(graph)


    paths = ((0,   5,  None, 10),
             (None,  0,  3,  None),
             (None, None, 0,   1),
             (None, None, None, 0))

    pprint(make_adj(*paths))

    # print floyd(make_adj(*paths))


        # fg = floyd(graph)
        # print "\nFloyd:"
        # pprint(fg)

        # reach_all, by_all = 0, 0
        # for key, nodes in fg.iteritems():
        #     print "sum of %s is %d" % (key, sum([1 for v in nodes.values() if v == 0]))
            

        # reach_all, by_all = 0, 0
        # for k, v in graph.iteritems():
        #     if len(v) == len(graph) - 1:
        #         print k, 'can reach all other items.'
        #         reach_all += 1
        #     if graph[k]
        # return reach_all, by_all
            

