class Node:
    def __init__(self, k):
        self.prod = 1
        self.cnt = [0] * k


class SegmentTree:

    def __init__(self, nums, k):
        self.n = len(nums)
        self.k = k
        self.tree = [None] * (4 * self.n)

        self.build(1, 0, self.n - 1, nums)


    def merge(self, left, right):
        k = self.k

        res = Node(k)

        # product of entire segment
        res.prod = (left.prod * right.prod) % k

        # prefixes completely inside left
        res.cnt = left.cnt[:]

        # prefixes = whole left + prefix of right
        for r in range(k):

            new_r = (left.prod * r) % k

            res.cnt[new_r] += right.cnt[r]

        return res


    def build(self, node, l, r, nums):

        if l == r:
            value = nums[l] % self.k

            cur = Node(self.k)
            cur.prod = value
            cur.cnt[value] = 1

            self.tree[node] = cur
            return

        mid = (l + r) // 2

        self.build(node * 2, l, mid, nums)
        self.build(node * 2 + 1, mid + 1, r, nums)

        self.tree[node] = self.merge(
            self.tree[node * 2],
            self.tree[node * 2 + 1]
        )


    def update(self, node, l, r, index, value):

        if l == r:
            value %= self.k

            cur = Node(self.k)
            cur.prod = value
            cur.cnt[value] = 1

            self.tree[node] = cur
            return

        mid = (l + r) // 2

        if index <= mid:
            self.update(node * 2, l, mid, index, value)
        else:
            self.update(node * 2 + 1, mid + 1, r, index, value)

        self.tree[node] = self.merge(
            self.tree[node * 2],
            self.tree[node * 2 + 1]
        )


    def query(self, node, l, r, ql, qr):

        if ql <= l and r <= qr:
            return self.tree[node]

        mid = (l + r) // 2

        if qr <= mid:
            return self.query(node * 2, l, mid, ql, qr)

        if ql > mid:
            return self.query(node * 2 + 1, mid + 1, r, ql, qr)

        left = self.query(
            node * 2, l, mid, ql, qr
        )

        right = self.query(
            node * 2 + 1, mid + 1, r, ql, qr
        )

        return self.merge(left, right)


class Solution:
    def resultArray(self, nums, k, queries):

        n = len(nums)

        seg = SegmentTree(nums, k)

        ans = []

        for index, value, start, x in queries:

            seg.update(
                1, 0, n - 1,
                index, value
            )

            node = seg.query(
                1, 0, n - 1,
                start, n - 1
            )

            ans.append(node.cnt[x])

        return ans