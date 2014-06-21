---
layout: page
title: topological.py
group: code
---
{% include JB/setup %}
[gist:topological](https://gist.github.com/hillscottc/ee407aea701ef342fce0)


    def topolgical_sort(graph_unsorted):
        """
        Go through each of the node/edges pairs in the unsorted
        graph. If a set of edges doesn't contain any nodes that
        haven't been resolved, that is, that are still in the
        unsorted graph, remove the pair from the unsorted graph,
        and append it to the sorted graph. Note here that by using
        using the items() method for iterating, a copy of the
        unsorted graph is used, allowing us to modify the unsorted
        graph as we move through it. We also keep a flag for
        checking that that graph is acyclic, which is true if any
        nodes are resolved during each pass through the graph. If
        not, we need to bail out as the graph therefore can't be
        sorted.
        """

        # The return list, topological sorted.
        graph_sorted = []

        while graph_unsorted:
            acyclic = False

            for node, edges in graph_unsorted.items():
                for edge in edges:
                    if edge in graph_unsorted:
                        break
                else:
                    acyclic = True
                    del graph_unsorted[node]
                    graph_sorted.append((node, edges))

            if not acyclic:
                raise RuntimeError("A cyclic dependency occurred.")

        return graph_sorted
