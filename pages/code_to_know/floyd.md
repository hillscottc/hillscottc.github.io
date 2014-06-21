---
layout: page
markdown: redcarpet
title: floyd.py
group: code
---
{% include JB/setup %}

[My floyd code](/pycode/floyd.py)



[gist:floyd-warshall](https://gist.github.com/hillscottc/61002306aa5b026ed73c)


    def floyd(g):
        """The Floyd-Warshall Algorithm...shortest paths for all vertices.
        """
        vertices = g.keys()
     
        d = g
        for v2 in vertices:
            d = {v1: {v3: min(d[v1][v3], d[v1][v2] + d[v2][v3])
                      for v3 in vertices}
                 for v1 in vertices}
        return d