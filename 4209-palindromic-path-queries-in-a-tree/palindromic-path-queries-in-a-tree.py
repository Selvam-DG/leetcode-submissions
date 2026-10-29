from typing import List

class Solution:
    def palindromePath(
        self,
        n: int,
        edges: List[List[int]],
        s: str,
        queries: List[str]
    ) -> List[bool]:

        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        chars = list(s)
        LOG = n.bit_length()

        parent = [0] * n
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        prefix = [0] * n

        # Step 1: DFS + Euler Tour
        timer = 0
        stack = [(0, -1, False)]

        while stack:
            u, p, exiting = stack.pop()

            if exiting:
                tout[u] = timer
                continue

            parent[u] = u if p == -1 else p
            tin[u] = timer
            timer += 1

            mask = 1 << (ord(chars[u]) - ord('a'))

            if p == -1:
                prefix[u] = mask
            else:
                depth[u] = depth[p] + 1
                prefix[u] = prefix[p] ^ mask

            stack.append((u, p, True))

            for v in graph[u]:
                if v != p:
                    stack.append((v, u, False))

        # Step 2: Binary Lifting for LCA
        up = [parent[:]]

        for j in range(1, LOG):
            prev = up[-1]
            up.append([prev[prev[u]] for u in range(n)])

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]

            for j in range(LOG):
                if diff & (1 << j):
                    u = up[j][u]

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if up[j][u] != up[j][v]:
                    u = up[j][u]
                    v = up[j][v]

            return parent[u]

        # Step 3: Fenwick Tree (XOR)
        bit = [0] * (n + 1)

        def add(i, value):
            i += 1
            while i <= n:
                bit[i] ^= value
                i += i & -i

        def get(i):
            i += 1
            result = 0

            while i > 0:
                result ^= bit[i]
                i -= i & -i

            return result

        def root_xor(u):
            return prefix[u] ^ get(tin[u])

        # Step 4: Process Queries
        answer = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                ch = parts[2]

                old_mask = 1 << (ord(chars[u]) - ord('a'))
                new_mask = 1 << (ord(ch) - ord('a'))

                delta = old_mask ^ new_mask

                # Update all root-prefix XORs in subtree(u)
                add(tin[u], delta)
                add(tout[u], delta)

                chars[u] = ch

            else:
                u = int(parts[1])
                v = int(parts[2])

                w = lca(u, v)

                lca_mask = 1 << (ord(chars[w]) - ord('a'))

                mask = root_xor(u) ^ root_xor(v) ^ lca_mask

                answer.append((mask & (mask - 1)) == 0)

        return answer