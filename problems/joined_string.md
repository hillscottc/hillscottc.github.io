---
layout: default
title: JoinedString
---


TopCoder problem "JoinedString" used in SRM 302 (Division I Level Three)

Problem Statement
         You are given a String[] words. Return the shortest String that contains all the words as substrings. If there are several possible answers, return the one that comes first lexicographically.

Definition
        
Class:     JoinedString
Method:     joinWords
Parameters:     String[]
Returns:     String
Method signature:     String joinWords(String[] words)
(be sure your method is public)
   

Constraints
-     words will contain between 1 and 12 elements, inclusive.
-     Each element of words will contain between 1 and 50 characters, inclusive.
-     Each element of words will consist of only uppercase letters ('A'-'Z').

Examples
0)    
        
{"BAB", "ABA"}
Returns: "ABAB"
There are two strings of length 4 that contain both given words: "ABAB" and "BABA". "ABAB" comes earlier lexicographically.
1)    
        
{"ABABA", "AKAKA", "AKABAS", "ABAKA"}
Returns: "ABABAKAKABAS"
2)    
        
{"AAA","BBB", "CCC", "ABC", "BCA", "CAB"}
Returns: "AAABBBCABCCC"
3)    
        
{"OFG", "SDOFGJTILM", "KBWNF", "YAAPO", "AWX", "VSEAWX", "DOFGJTIL", "YAA"}
Returns: "KBWNFSDOFGJTILMVSEAWXYAAPO"
4)    
        
{"NVCSKFLNVS", "HUFSPMRI", "FLNV", "KMQD", "RPJK", "NVSQORP", "UFSPMR", "AIHUFSPMRI"}
Returns: "AIHUFSPMRINVCSKFLNVSQORPJKMQD"
5)    
        
{"STRING", "RING"}
Returns: "STRING"
Problem url: http://www.topcoder.com/stat?c=problem_statement&pm=6215
Problem stats url: http://www.topcoder.com/tc?module=ProblemDetail&rd=9823&pm=6215
Writer: Andrew_Lazarev Testers: PabloGilberto , brett1479 , legakis , Olexiy Problem categories: Dynamic Programming, String Manipulation