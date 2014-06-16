---
layout: default
title: lcs.py
---
[gist:longest-common-substring](https://gist.github.com/hillscottc/947a1f5ddd01bdc85c72#file-long_substr-py)


    def long_substr(data):
        """Finds the longest common string in any arbitrary array of strings"""
        substr = ''
        if len(data) > 1 and len(data[0]) > 0:
            for i in range(len(data[0])):
                for j in range(len(data[0])-i+1):
                    if j > len(substr) and all(data[0][i:i+j] in x for x in data):
                        substr = data[0][i:i+j]
        return substr
