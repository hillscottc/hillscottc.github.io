---
layout: page
markdown: redcarpet
title: Suffix Trees and Tries
group: data_structs
---
{% include JB/setup %}


Suffix trees can be used to solve *longest common substring* problems.

Given strings "ABAB" and "BABA", the matrix would look like:

        |   |   | A | B | A | B |
        |   | O | O | O | O | O |
        | B | O | O | 1 | O | 1 |
        | A | O | 1 | 0 | 2 | 0 |
        | B | O | 0 | 2 | 0 | 3 |
        | A | O | 1 | 0 | 3 | 0 |


In this matrix, the 5th column tests the substring ABA of the ABAB sequence.
So cell `[5, 5]` compares ABA to BAB ... the lcs is BA, length 2.

Construct a generalized suffix tree for the strings, 
then find the deepest internal nodes which have leaf nodes from all the strings in the subtree below it.

A basic Suffix Tree imp.

    """http://goo-apple.appspot.com/article/2e8d3c6a-2c38-48b9-96c6-240b4ded253a"""
    class Node:
            def __init__(self, start, substr):
                    self.start = start
                    self.substr = substr
                    self.branches = {}
                  
    def insert_into_tree(subroot, suffix, start):
            prefix_len = len(subroot.substr)
            new_suffix = str(suffix[prefix_len:])
            if(len(subroot.branches) == 0):
                    left_child = Node(subroot.start, "")
                    right_child = Node(start, new_suffix)
                    subroot.branches[""] = left_child
                    subroot.branches[new_suffix] = right_child
            else:
                    for (substr, node) in subroot.branches.items():
                            if len(substr) > 0 and new_suffix.startswith(substr):
                                    insert_into_tree(node, new_suffix, start)
                                    break
                    else:
                            new_child = Node(start, new_suffix)
                            subroot.branches[new_suffix] = new_child
                  
    def build_suffix_tree(t_str):
            len_str = len(t_str)
            i = len_str - 1
            root = Node(len_str, "")
            while i >= 0:
                    insert_into_tree(root, str(t_str[i:]), i)
                    i -= 1
            return root
                  
    def display_all_suffix(subroot, suffix_s_prefix, level = 0):
            if len(subroot.branches) == 0:
                    print suffix_s_prefix, level
                    return
            for (substr, node) in subroot.branches.items():
                    display_all_suffix(node, suffix_s_prefix + substr, level + 1)
                  
    root = build_suffix_tree("BCABC")
    display_all_suffix(root, "")





## *Tries* are really PREFIX TREES?

![suffix tree img][suffix_tree]

A Simple Suffix Tree Implementation:
`<script src="https://gist.github.com/hillscottc/f0460657daca55f95b62.js"></script>`

Or, here's a [more complete version][suffix_tree_big].

### What is a Trie?

[Tries on TopCoder][tries1]


    - The trie is a tree where each vertex represents a single word or a prefix.
    - The root represents an empty string ("")
    - direct sons of root rep prefixes of length 1, vertexes 2 edges distant rep prefixes of length 2, etc. 
    So, a vertex k edges of distance of the root has as an associated prefix of length k.
    - Let v and w be two vertexes of the trie, and assume that v is a direct father of w, the\n v must have an associated prefix of w.

The tries can insert and find strings in `O(L)` time (where L represent the length of a single word). 

The next figure shows a trie with the words "tree", "trie", "algo", "assoc", "all", and "also."

![trie nodes][trie_nodes]

### Coding a Trie

From from post on [stackoverflow](http://stackoverflow.com/questions/11015320/how-to-create-a-trie-in-python)

**Nested dictionaries** ... For a large, scalable trie, nested dictionaries might become space inefficient. 
But they are the easiest approach...just a few lines.

[nested dicts for suffix tries](https://gist.github.com/hillscottc/d60e7fbe714a6a4b8f9b)

Note, The method setdefault() is a get-or-create.

    >>> def make_trie(*words):
    ...     root = dict()
    ...     for word in words:
    ...         current_dict = root
    ...         for letter in word:
    ...             current_dict = current_dict.setdefault(letter, {})
    ...         current_dict = current_dict.setdefault('_end_', '_end_')
    ...     return root

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


Your algorithm here is basically O(N*M*L) (where N is the length of the sentence, M is the number of words you're looking for, and L is the longest word you're looking for) for each sentence.


[suffix_tree]: /img/suffix_tree.png
[suffix_tree_big]: https://gist.github.com/hillscottc/e27f7acbc235f6a3e75d
[trie_stack]: https://gist.github.com/hillscottc/d60e7fbe714a6a4b8f9b.js
[tries1]: http://help.topcoder.com/data-science/competing-in-algorithm-challenges/algorithm-tutorials/using-tries/
[trie_nodes]: /img/trie.png