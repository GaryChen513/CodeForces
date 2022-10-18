class Solution:
    def maximumSegmentSum(self, nums, removeQueries):
        return 0

class Node:
    def __init__(self, lower, upper, left=None, right=None):
        self.lower = lower
        self.upper = upper
        self.left = left
        self.right = right
        self.Maximum = -1
        self.hasZero = False


class SegTree():
    def __init__(self, val):
        self.root = Node(0, val)

    def add(self, val):
        self._add(self.root, val)

    def _add(self, node, val):
        mid = (node.lower + node.upper) // 2

        if not node.left:
            node.left = Node(lower, mid)
        if not node.right:
            node.right = Node(mid + 1, upper)

        if 