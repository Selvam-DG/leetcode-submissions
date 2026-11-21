class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:


        n = len(parent)

        # Build original tree
        tree = [[] for _ in range(n)]
        for i in range(1, n):
            tree[parent[i]].append(i)

        # Find the new parents
        new_parent = parent[:]
        last_seen = {}

        def dfs(node):
            char = s[node]
            prev = last_seen.get(char)

            if prev is not None:
                new_parent[node] = prev

            last_seen[char] = node

            for child in tree[node]:
                dfs(child)

            # Backtrack
            if prev is None:
                del last_seen[char]
            else:
                last_seen[char] = prev

        dfs(0)

        # Build modified tree
        new_tree = [[] for _ in range(n)]
        for i in range(1, n):
            new_tree[new_parent[i]].append(i)

        # Calculate subtree sizes
        ans = [1] * n

        def count(node):
            for child in new_tree[node]:
                ans[node] += count(child)
            return ans[node]

        count(0)
        return ans
