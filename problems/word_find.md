## Word Find

TopCoder problem "WordFind" used in SRM 232 (Division I Level One , Division II Level Two)
         
You have been given a "word search" puzzle, which consists of a rectangular grid of letters, in which several words are hidden. 
Words may be oriented horizontally, vertically, or diagonally, however, all go down, right, or down-right. 

You are given a String[], grid, indicating the letters in the grid to be searched. Character j of element i of grid is the letter at row i, column j. 
You are also given a String[], wordList, indicating the words to be found in the grid. 
You are to return a String[] indicating the locations of each word within the grid.

The return value should have the same number of elements as wordList, and in the same order.

### Definition:       

- Class: WordFind, Method: findWords
- Method signature: String[] findWords(String[] grid, String[] wordList)

### Constraints:

- grid will contain between 1 and 50 elements, inclusive.
- Each element of grid will contain between 1 and 50 characters, inclusive.
- Each element of grid will contain the same number of characters.
- Each character of each element of grid will be 'A'-'Z'.
- wordList will contain between 1 and 50 elements, inclusive.
- Each element of wordList will contain between 1 and 50 characters, inclusive.
- Each character of each element of wordList will be 'A'-'Z'.


Example 0:

    (["TEST", "GOAT", "BOAT"],
     ["GOAT", "BOAT", "TEST"])

    Returns: ["1 0", "2 0", "0 0"]


Example 1:

    (["SXXX", "XQXM", "XXLA", "XXXR"],
     ["SQL", "RAM"])

    Returns: ["0 0", ""]


Example 2:

    (["EASYTOFINDEAGSRVHOTCJYG",
      "FLVENKDHCESOXXXXFAGJKEO",
      "YHEDYNAIRQGIZECGXQLKDBI",
      "DEIJFKABAQSIHSNDLOMYJIN",
      "CKXINIMMNGRNSNRGIWQLWOG",
      "VOFQDROQGCWDKOUYRAFUCDO",
      "PFLXWTYKOITSURQJGEGSPGG"],
     ["EASYTOFIND", "DIAG", "GOING", "THISISTOOLONGTOFITINTHISPUZZLE"])
    
    Returns: ["0 0", "1 6", "0 22", ""]

