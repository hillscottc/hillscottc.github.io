"""
Dijkstra's algorithm for shortest paths.
http://code.activestate.com/recipes/577343-dijkstras-algorithm-for-shortest-paths/)

> dijkstra(G, s) finds all shortest paths from s to each other vertex in the graph.
> shortest_path(G, s, t) uses dijkstra to find the shortest path from s to t.

The input graph G is assumed to have the following representation:
A vertex can be any object that can be used as an index into a dictionary.
G is a dictionary, indexed by vertices.  For any vertex v, G[v] is itself a dictionary,
indexed by the neighbors of v.  For any edge v->w, G[v][w] is the length of the edge.

This is related to the representation in <http://www.python.org/doc/essays/graphs.html> where
Guido van Rossum suggests representing graphs as dictionaries mapping vertices to lists of neighbors,
however dictionaries of edges have many advantages over lists: they can store extra information (here, the lengths),
they support fast existence tests, and they allow easy modification of the graph by edge insertion and removal.
Such modifications are not needed here but are important in other graph algorithms.
Since dictionaries obey iterator protocol, a graph represented as described here could be handed without
modification to an algorithm using Guido's representation.

Of course, G and G[v] need not be Python dict objects; they can be any other object that obeys dict protocol,
for instance a wrapper in which vertices are URLs and a call to G[v] loads the web page and finds its links.
The output is a pair (D,P) where D[v] is the distance from start to v and P[v] is the predecessor of v along
the shortest path from s to v. Dijkstra's algorithm is only guaranteed to work correctly when all edge lengths
are positive. This code does not verify this property for all edges (only the edges seen before the end vertex
is reached), but will correctly compute shortest paths even for some graphs with negative edges, and will
raise an exception if it discovers that a negative edge has caused it to make a mistake.
"""
from priodict import priorityDictionary


def dijkstra(graph, start, end=None):
    final_distances = {}
    predecessors = {}
    estimated_distances = priorityDictionary()
    estimated_distances[start] = 0

    for vertex in estimated_distances:
        final_distances[vertex] = estimated_distances[vertex]
        if vertex == end:
            break

        for edge in graph[vertex]:
            path_distance = final_distances[vertex] + graph[vertex][edge]
            if edge in final_distances:
                if path_distance < final_distances[edge]:
                    raise ValueError("Found better path to already-final vertex")
            elif edge not in estimated_distances or path_distance < estimated_distances[edge]:
                estimated_distances[edge] = path_distance
                predecessors[edge] = vertex

    return final_distances, predecessors


def shortest_path(graph, start, end):
    """
    Find a single shortest path from the given start vertex to the given end vertex,
    output as list of vertices in order along the shortest path.
    """

    final_distances,predecessors = dijkstra(graph,start,end)
    path = []
    while 1:
        path.append(end)
        if end == start: break
        end = predecessors[end]
    path.reverse()
    return path

if __name__ == "____main__":
    pass
    # G = {'s':{'u':10, 'x':5}, 'u':{'v':1, 'x':2}, 'v':{'y':4},
    #      'x':{'u':3, 'v':9, 'y':2}, 'y':{'s':7, 'v':6}}
    # The shortest path from s to v is ['s', 'x', 'u', 'v'] and has length 9.