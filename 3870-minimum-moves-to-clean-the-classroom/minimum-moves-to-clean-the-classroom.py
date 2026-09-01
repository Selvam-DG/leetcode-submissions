from typing import List
from collections import deque

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])

        # Find start and give every litter cell a bit index
        start = None
        litter_id = {}
        litter_count = 0

        for row in range(m):
            for col in range(n):
                if classroom[row][col] == 'S':
                    start = (row, col)

                elif classroom[row][col] == 'L':
                    litter_id[(row, col)] = litter_count
                    litter_count += 1

        # No litter to collect
        if litter_count == 0:
            return 0

        # All bits = 1 means all litter collected
        target_mask = (1 << litter_count) - 1
        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        # state:
        # row, col, litter_mask, remaining_energy, moves
        sr, sc = start

        q = deque([
            (sr, sc, 0, energy, 0)
        ])

        visited = {
            (sr, sc, 0, energy)
        }

        while q:
            row, col, mask, curr_energy, moves = q.popleft()

            if mask == target_mask:
                return moves

            # Cannot make another move
            if curr_energy == 0:
                continue

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                # Outside classroom
                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                # Obstacle
                if classroom[nr][nc] == 'X':
                    continue

                # Every move consumes 1 energy
                new_energy = curr_energy - 1
                new_mask = mask

                # Reset energy
                if classroom[nr][nc] == 'R':
                    new_energy = energy

                # Collect litter
                elif classroom[nr][nc] == 'L':
                    litter_index = litter_id[(nr, nc)]
                    new_mask |= (1 << litter_index)


                state = (nr, nc, new_mask, new_energy)

                if state not in visited:
                    visited.add(state)
                    q.append(
                        (nr, nc, new_mask, new_energy, moves + 1)
                    )

        return -1