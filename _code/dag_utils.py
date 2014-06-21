"""Utils for Directed Acyclic Graphs."""

# Directed Acyclic Graph (DAG)
# A -> B -> D -> E
#           |
#           C

# Adjacency List = dict of nodes to list of adjacent nodes (weight=1)
ADJL = {
    'A': ['B'],
    'B': ['D'],
    'C': ['D'],
    'D': ['E'],
    'E': []
}

# Weighted Graph = distances of all reachable nodes
WG = {
    'A': {'B': 1, 'D': 2, 'E': 3},
    'B': {'D': 1, 'E': 2},
    'C': {'D': 1, 'E': 2},
    'D': {'E': 1},
    'E': {}
}

# Directed Adjacency Graph (DAG)
# (Matrix of WG, with weight-self:0, weight-unreachable:INF)
INF = float('inf')
DAG = {
    'A': {'A': 0, 'B': 1, 'C': INF, 'D': 2, 'E': 3},
    'B': {'A': INF, 'B': 0, 'C': INF, 'D': 1, 'E': 2},
    'C': {'A': INF, 'B': INF, 'C': 0, 'D': 1, 'E': 2},
    'D': {'A': INF, 'B': INF, 'C': 0, 'D': 0, 'E': 1},
    'E': {'A': INF, 'B': INF, 'C': INF, 'D': INF, 'E': 0}
}


def adj(g):
    """
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


def chars_to_adj_matrix(*paths):
    return {v1: {v2: float('inf') if v1 != v2 and paths[v1][v2] == '0' else int(paths[v1][v2])
                 for v2 in range(len(paths))}
            for v1 in range(len(paths))}


def floyd(graph):
    vertices = graph.keys()
    d = graph
    for v2 in vertices:
        d = {v1: {v3: min(d[v1][v3], d[v1][v2] + d[v2][v3])
                  for v3 in vertices}
             for v1 in vertices}
    return d


if __name__ == '__main__':
    from pprint import pprint

    # From the probs given examples, as (paths, returns),
    # where 'results' = (count-can-reach-all, count-reachable-by-all)
    test = (
        {'paths': ("010", "000", "110"), 'results': (1, 1)},
        {'paths': ("0010", "1000", "1100", "1000"), 'results': (1, 3)},
        {'paths': ("01000", "00100","00010", "00001", "10000"), 'results': (5, 5)},
        {'paths': ("0110000", "1000100", "0000001", "0010000", "0110000",
         "1000010", "0001000"), 'results': (1, 3)}
    )

    for test in test:
        print "\nPaths:"
        pprint(test['paths'])

        print "\nAdj Matrix:"
        matrix = chars_to_adj_matrix(*test['paths'])
        pprint(matrix)

        print "\nFloyd"
        fg = floyd(matrix)
        pprint(fg)

        print "\nResults"
        r = get_results(fg)

        print("Can reach all", r[0])
        assert(r[0] == test['results'][0])

        # print("Reachable by all", r[1])
        # assert(r[1] == test['results'][1])