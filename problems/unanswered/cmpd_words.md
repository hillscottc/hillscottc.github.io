---
layout: default
title: Compound Words
---

TopCoder problem "CmpdWords" used in SRM 268 (Division I Level One , Division II Level Two)

### Problem Statement

Some languages allow the use of compound words, words that are the concatenation of words from the language's dictionary.

We have defined a language that consists of a dictionary of distinct words. We want to know whether we should allow the use of compound words constructed by concatenating exactly two distinct dictionary words. 

The potential problem is that a compound word is ambiguous if either (or both) of the following conditions applies:

    - the compound word is a dictionary word
    - the compound word can be formed in more than one way.

For example, if "am","eat","a", "meat", "hook", and "meathook" were all in the dictionary, then "meathook" would be ambiguous according to the first condition, and "ameat" would be ambiguous according to the second condition.

Create a class CmpdWords that contains a method ambiguous that is given a String[] dictionary and that returns the number of ambiguous words that would result from allowing the compounding of distinct pairs of dictionary words. An ambiguous word should be counted only once, no matter how many different ways it could be formed.
Note that compound words are NOT added to the dictionary. So the dictionary {"a", "b","c"} does not allow "abc" as a compound word.

### Definition
        
Class:     CmpdWords
Method:     ambiguous
Parameters:     String[]
Returns:     int
Method signature:     int ambiguous(String[] dictionary)
(be sure your method is public)
   

### Constraints
- dictionary will contain between 1 and 50 elements inclusive.
- The elements of dictionary will be distinct.
- Each element of dictionary will contain between 1 and 20 characters inclusive.
- Each character in each element of dictionary will be a lowercase letter 'a'-'z'.

### Examples
0)    
        
{"am","eat","a", "meat", "hook","meathook"}
Returns: 2
"meathook" and "ameat" are ambiguous as explained above.
1)    
        
{"a","b","c"}
Returns: 0
All the compound words are: "ab","ac","bc","ba","ca","cb" and none of these is ambiguous.
2)    
        
{"a","aa","aaa"}
Returns: 3
The ambiguous words are "aaa": ("a"+"aa" and "aa"+"a" and "aaa") "aaaa": ("a"+"aaa" and "aaa"+"a") "aaaaa": ("aa"+"aaa" and "aaa"+"aa")
3)    
        
{"abc","bca","bab","a"}
Returns: 1
"abc"+"a" = "a"+"bca"
Problem url: http://www.topcoder.com/stat?c=problem_statement&pm=3490
Problem stats url: http://www.topcoder.com/tc?module=ProblemDetail&rd=8001&pm=3490
Writer: dgoodman Testers: PabloGilberto , brett1479 , Olexiy Problem categories: Brute Force, String Manipulation