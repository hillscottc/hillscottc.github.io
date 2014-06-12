---
layout: default
title: Suffix Trees and Tries
---
# Suffix Trees and Tries


## Suffix Trees

Suffix trees can be used to solve *longest common substring* problems.

Given strings "ABAB" and "BABA", the matrix would look like:

        |   |   | A | B | A | B |
        |   | O | O | O | O | O |
        | B | O | O | 1 | O | 1 |
        | A | O | 1 | 0 | 2 | 0 |
        | B | O | 0 | 2 | 0 | 3 |
        | A | O | 1 | 0 | 3 | 0 |


In this matrix, the 5th column tests the substring ABA of the ABAB sequence.
So cell [5, 5] compares ABA to BAB ... the lcs is BA, length 2.


The other approach is to construct a generalized suffix tree for the strings, 
then find the deepest internal nodes which have leaf nodes from all the strings in the subtree below it.

## *Tries* are PREFIX TREES.

![suffix tree img][suffix_tree]

A Simple Suffix Tree Implementation:
<script src="https://gist.github.com/hillscottc/f0460657daca55f95b62.js"></script>

Or, here's a [more complete version][suffix_tree_big].

### What is a Trie?

[Tries on TopCoder][tries1]


    - The trie is a tree where each vertex represents a single word or a prefix.
    - The root represents an empty string ("")
    - direct sons of root rep prefixes of length 1, vertexes 2 edges distant rep prefixes of length 2, etc. 
    So, a vertex k edges of distance of the root has as an associated prefix of length k.
    - Let v and w be two vertexes of the trie, and assume that v is a direct father of w, the\n v must have an associated prefix of w.

The tries can insert and find strings in O(L) time (where L represent the length of a single word). 

The next figure shows a trie with the words "tree", "trie", "algo", "assoc", "all", and "also."

![trie nodes][trie_nodes]

### Coding a Trie

From from post on [stackoverflow](http://stackoverflow.com/questions/11015320/how-to-create-a-trie-in-python)

**Nested dictionaries** ... For a large, scalable trie, nested dictionaries might become space inefficient. 
But they are the easiest approach...just a few lines.

Note, The method setdefault() is a get-or-create.

    In [5]: d = {}
    In [6]: d.setdefault('X', {})
    Out[6]: {}
    In [7]: print d
    {'X': {}}


    >>> def make_trie(*words):
    ...     root = dict()
    ...     for word in words:
    ...         current_dict = root
    ...         for letter in word:
    ...             current_dict = current_dict.setdefault(letter, {})
    ...         current_dict = current_dict.setdefault('_end_', '_end_')
    ...     return root
    ...
    >>> make_trie('foo', 'bar', 'baz', 'barz')
    {'b': {'a': {'r': {'_end_': '_end_', 'z': {'_end_': '_end_'}},
                 'z': {'_end_': '_end_'}}},
     'f': {'o': {'o': {'_end_': '_end_'}}}}

Then search the trie with:
 
    >>> def in_trie(trie, word):
    ...     current_dict = trie
    ...     for letter in word:
    ...         if letter in current_dict:
    ...             current_dict = current_dict[letter]
    ...         else:
    ...             return False
    ...     if _end in current_dict:
    ...         return True
    ...     else:
    ...         return False
    ... 
    >>> in_trie(make_trie('foo', 'bar', 'baz', 'barz'), 'baz')
    True

Your algorithm here is basically O(N*M*L) (where N is the length of the sentence, M is the number of words you're looking for, and L is the longest word you're looking for) for each sentence.

{}







[suffix_tree]: https://hillscottc.github.io/img/suffix_tree.png
[suffix_tree_big]: https://gist.github.com/hillscottc/e27f7acbc235f6a3e75d
[trie_stack]: https://gist.github.com/hillscottc/d60e7fbe714a6a4b8f9b.js
[tries1]: http://help.topcoder.com/data-science/competing-in-algorithm-challenges/algorithm-tutorials/using-tries/
[trie_nodes]: https://hillscottc.github.io/img/trie.png