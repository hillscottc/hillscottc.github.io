"""Structured data samples."""

# Adjacency Lists.

#    A
#  /   \
# B--D--C
#  \ |
#    E
ADJL_1 = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['B', 'D']
}


# A ----- E
# |       |
# B - C - D
ADJL_2 = {
    'A': ['B', 'E'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['C', 'E'],
    'E': ['A', 'D']
}
