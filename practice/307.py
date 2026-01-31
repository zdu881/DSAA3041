"""\
Problem: 307. Range Sum Query - Mutable
Source: https://leetcode.com/problems/range-sum-query-mutable/
Difficulty: Medium
Tags: Segment Tree, Binary Indexed Tree, Design

题意（从截图整理）：
给定一个整数数组 nums，需要支持两类操作：

1) update(index, val)：把 nums[index] 更新为 val
2) sumRange(left, right)：返回 nums[left..right]（包含两端）的元素和

需要实现 NumArray 类：
- NumArray(nums)：用数组初始化
- update(index, val)：单点更新
- sumRange(left, right)：区间求和

示例：
输入：
	["NumArray", "sumRange", "update", "sumRange"]
	[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
输出：
	[null, 9, null, 8]
解释：
	nums = [1, 3, 5]
	sumRange(0, 2) = 1 + 3 + 5 = 9
	update(1, 2) 后 nums = [1, 2, 5]
	sumRange(0, 2) = 1 + 2 + 5 = 8

约束（常见平台约束，和截图一致）：
- 1 <= nums.length <= 3 * 10^4
- -100 <= nums[i] <= 100
- 0 <= index < nums.length
- -100 <= val <= 100
- 0 <= left <= right < nums.length
- update 和 sumRange 总调用次数最多约 3 * 10^4

思路（线段树 Segment Tree，不写实现，只讲思路）：

为什么需要线段树？
- 如果每次 sumRange 都直接把 nums[left..right] 加起来：一次查询 O(n)，调用多会超时。
- 如果用前缀和数组 prefix：查询 O(1)，但 update 会导致后面所有 prefix 都变，需要 O(n)。
- 所以要一种同时支持“单点更新”和“区间求和”的数据结构：线段树可以做到两者都 O(log n)。

线段树怎么表示？
- 把数组看作区间 [0, n-1]。
- 树的每个节点表示一个区间 [l, r]，并维护这个区间的“和”。
- 根节点是 [0, n-1]。
- 每次把区间对半分：mid = (l + r) // 2，左孩子管 [l, mid]，右孩子管 [mid+1, r]。

build（建树，初始化）：
- 递归建树：叶子节点 l == r，对应单个元素 nums[l]，sum = nums[l]
- 内部节点 sum = left.sum + right.sum
- 复杂度：O(n)

update（单点更新 index -> val）：
- 从根开始往下走：
	- 如果当前节点区间 [l, r] 覆盖 index，就继续往包含 index 的那一侧走
	- 直到走到叶子节点 [index, index]，把 sum 改成 val
	- 回溯时把沿途节点的 sum 重新计算为左右孩子之和
- 复杂度：每层走一次，树高约 log2(n)，所以 O(log n)

query（sumRange(left, right)）：
- 从根节点区间 [l, r] 出发，分三种情况：
	1) 查询区间完全覆盖当前节点区间：直接返回该节点 sum
	2) 查询区间和当前节点区间完全不相交：返回 0
	3) 部分相交：把查询分别递归到左右孩子，再把结果相加
- 复杂度：O(log n)

空间：
- 常用数组形式存树（类似堆的下标关系），一般开 4*n 足够。

你也可以用“树状数组 Fenwick Tree”做，update/query 也都是 O(log n)，但本题你要求写线段树思路。
"""

from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        """初始化数据结构（建议：建一棵线段树并保存 nums）。"""
        self.n = len(nums)
        # 4*n is generally enough for a segment tree
        self.tree = [0] * (4 * self.n)
        self.nums = nums  # Optional: keep reference if needed
        if self.n > 0:
            self._build(0, 0, self.n - 1)

    def _build(self, node: int, start: int, end: int):
        if start == end:
            self.tree[node] = self.nums[start]
        else:
            mid = (start + end) // 2
            left_node = 2 * node + 1
            right_node = 2 * node + 2
            self._build(left_node, start, mid)
            self._build(right_node, mid + 1, end)
            self.tree[node] = self.tree[left_node] + self.tree[right_node]

    def update(self, index: int, val: int) -> None:
        """单点更新：把 nums[index] 改为 val。"""
        self._update(0, 0, self.n - 1, index, val)

    def _update(self, node: int, start: int, end: int, idx: int, val: int):
        if start == end:
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            left_node = 2 * node + 1
            right_node = 2 * node + 2
            if start <= idx <= mid:
                self._update(left_node, start, mid, idx, val)
            else:
                self._update(right_node, mid + 1, end, idx, val)
            self.tree[node] = self.tree[left_node] + self.tree[right_node]

    def sumRange(self, left: int, right: int) -> int:
        """区间查询：返回 nums[left..right] 的元素和。"""
        return self._query(0, 0, self.n - 1, left, right)

    def _query(self, node: int, start: int, end: int, l: int, r: int) -> int:
        # Range is completely outside
        if r < start or end < l:
            return 0
        # Range is completely inside
        if l <= start and end <= r:
            return self.tree[node]
        # Partial overlap
        mid = (start + end) // 2
        left_node = 2 * node + 1
        right_node = 2 * node + 2
        sum_left = self._query(left_node, start, mid, l, r)
        sum_right = self._query(right_node, mid + 1, end, l, r)
        return sum_left + sum_right

