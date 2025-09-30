#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.
#
from collections import defaultdict
class Node:
    def __init__(self, ch=""):
        self.ch = ch
        self.children = {}
        self.is_last = False

def noPrefix(words):
    # Write your code here
    root = Node("root")
    for word in words:
        cur_node = root
        for ch in word:
            if ch in cur_node.children:
                cur_node = cur_node.children[ch]
            else:
                cur_node.children[ch] = Node(ch)
                cur_node = cur_node.children[ch]
                
            if cur_node.is_last:
                print("BAD SET")
                print(word)
                return
        if len(cur_node.children) > 0:
            print("BAD SET")
            print(word)
            return
        cur_node.is_last = True
    print("GOOD SET")
    return 
        
        

if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)
