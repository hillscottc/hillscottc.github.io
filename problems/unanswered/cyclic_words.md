---
layout: default
title: Cyclic Words
---

TopCoder problem "CyclicWords" used in SRM 358 (Division II Level One)

Problem Statement
We can think of a cyclic word as a word written in a circle. To represent a cyclic word, we choose an arbitrary starting position and read the characters in clockwise order. So, "picture" and "turepic" are representations for the same cyclic word.

You are given a String[] words, each element of which is a representation of a cyclic word. Return the number of different cyclic words that are represented.

Definition
        
Class:     CyclicWords
Method:     differentCW
Parameters:     String[]
Returns:     int
Method signature:     int differentCW(String[] words)
(be sure your method is public)
   
Constraints
- words will contain between 1 and 50 elements, inclusive.
- Each element of words will contain between 1 and 50 lowercase letters ('a'-'z'), inclusive.

Examples
0)            
{ "picture", "turepic", "icturep", "word", "ordw" }
Returns: 2
"picture", "turepic" and "iceturep" are representations of the same cyclic word. "word" and "ordw" are representations of a second cyclic word.

1)            
{ "ast", "ats", "tas", "tsa", "sat", "sta", "ttt" }
Returns: 3

2)    
        
{"aaaa", "aaa", "aa", "aaaa", "aaaaa"}
Returns: 4


Problem url: http://www.topcoder.com/stat?c=problem_statement&pm=7694
Problem stats url: http://www.topcoder.com/tc?module=ProblemDetail&rd=10768&pm=7694
Writer: icanadi Testers: PabloGilberto , brett1479 , Olexiy , Andrew_Lazarev Problem categories: Simple Search, Iteration, String Manipulation