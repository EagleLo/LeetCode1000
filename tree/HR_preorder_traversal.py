"""
HackerRank-style: Tree Preorder Traversal

Problem
Given a Binary Search Tree (BST) built from inserting values in order, print the preorder traversal
of the tree (root, left, right). Use spaces between values on a single line.

Input format
- First line: integer n, the number of values
- Second line: n space-separated integers to insert into the BST in order

Output format
- One line with the preorder traversal (space-separated)

Example
Input
5
1 2 5 3 6
Output
1 2 5 3 6

Notes
- If a value is equal to an existing node value, ignore the insert (standard HR convention)
- The preorder traversal for an empty tree prints nothing

Usage
- Run normally to read from stdin and print preorder traversal
- Run with: `python HR_preorder_traversal.py test` to execute built-in tests
"""

import sys
from typing import List, Optional


class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 


class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
            
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""

def preOrder(root: Optional[Node]) -> None:
    # Write your code here
    result: List[str] = []

    def dfs(cur: Optional[Node]) -> None:
        if cur is None:
            return
        result.append(str(cur.info))
        dfs(cur.left)
        dfs(cur.right)

    dfs(root)
    if result:
        print(' '.join(result))
    else:
        print("")


def _run_cli() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        print("")
        return
    it = iter(data)
    try:
        n = int(next(it))
    except StopIteration:
        print("")
        return
    values: List[int] = []
    for _ in range(n):
        try:
            values.append(int(next(it)))
        except StopIteration:
            break

    tree = BinarySearchTree()
    for v in values:
        tree.create(v)

    preOrder(tree.root)


def _run_tests() -> None:
    cases = [
        ([], ""),
        ([1], "1"),
        ([1, 2, 5, 3, 6], "1 2 5 3 6"),
        ([4, 2, 1, 3, 6, 5, 7], "4 2 1 3 6 5 7"),
        ([5, 3, 7, 3, 5, 7], "5 3 7"),  # duplicates ignored
    ]

    for arr, expected in cases:
        tree = BinarySearchTree()
        for v in arr:
            tree.create(v)
        # capture print
        from io import StringIO
        import contextlib
        buf = StringIO()
        with contextlib.redirect_stdout(buf):
            preOrder(tree.root)
        got = buf.getvalue().strip()
        assert got == expected, f"For {arr}, expected '{expected}' got '{got}'"
    print("All preorder traversal tests passed!")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        _run_tests()
    else:
        _run_cli()
