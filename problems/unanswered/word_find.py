"""
Words may be oriented horiz, vertically, or diagonally, however, all go down, right, or down-right.
- Method signature: String[] findWords(String[] grid, String[] wordList)
"""


def find_words(grid, words):
    results = {}
    for row in grid:
        for i, word in enumerate(words):
            pos = row.find(word)
            if pos > -1:
                old_val = results.get(word)
                if pos > old_val:
                    results[word] = pos
                    continue
    return results


if __name__ == '__main__':

    grid = ["EASYTOFINDEAGSRVHOTCJYG",
            "FLVENKDHCESOXXXXFAGJKEO",
            "YHEDYNAIRQGIZECGXQLKDBI",
            "DEIJFKABAQSIHSNDLOMYJIN",
            "CKXINIMMNGRNSNRGIWQLWOG",
            "VOFQDROQGCWDKOUYRAFUCDO",
            "PFLXWTYKOITSURQJGEGSPGG"]

    words = ["EASYTOFIND", "DIAG", "GOING", "THISISTOOLONGTOFITINTHISPUZZLE"]

    res_dict = find_words(grid, words)

    print res_dict

    results = []
    for i, word in enumerate(words):
        if not res_dict.get(word):
            results.append((i, 0))
        else:
            results.append((i, res_dict[word]))

    print words
    print results
