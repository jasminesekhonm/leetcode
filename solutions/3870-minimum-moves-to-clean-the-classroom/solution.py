from collections import deque

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        if not classroom or not classroom[0]:
            return -1

        rows, cols = len(classroom), len(classroom[0])
        start_r = start_c = -1
        litter_positions = {}
        litter_id = 0

        # 1. Locate the start position and map each litter to a unique bit index
        for r in range(rows):
            for c in range(cols):
                if classroom[r][c] == 'S':
                    start_r, start_c = r, c
                elif classroom[r][c] == 'L':
                    litter_positions[(r, c)] = litter_id
                    litter_id += 1

        # Edge case: No litter to collect
        if litter_id == 0:
            return 0

        target_mask = (1 << litter_id) - 1

        # Queue stores: (row, col, collected_litter_mask, current_energy, step_count)
        queue = deque([(start_r, start_c, 0, energy, 0)])

        # Visited dictionary maps (row, col, mask) -> max_energy_remaining
        # This prevents infinite loops while allowing longer paths if they yield more energy
        visited = {}
        visited[(start_r, start_c, 0)] = energy

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # 2. BFS Traversal
        while queue:
            r, c, mask, curr_energy, steps = queue.popleft()

            # If energy is depleted and we didn't just land on a Reset ('R'), we cannot move further.
            if curr_energy == 0:
                continue

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Check boundaries and obstacles
                if 0 <= nr < rows and 0 <= nc < cols and classroom[nr][nc] != 'X':
                    next_energy = curr_energy - 1
                    next_mask = mask

                    # Update the mask if we step on uncollected litter
                    if classroom[nr][nc] == 'L':
                        next_mask |= (1 << litter_positions[(nr, nc)])
                    
                    # If this move collects the last piece of litter, return immediately
                    if next_mask == target_mask:
                        return steps + 1

                    # If we step on a Reset cell, restore energy to maximum
                    if classroom[nr][nc] == 'R':
                        next_energy = energy

                    state = (nr, nc, next_mask)
                    
                    # Only explore this state if it's unvisited OR if we've found a path 
                    # to this exact state that leaves us with strictly MORE energy.
                    if state not in visited or visited[state] < next_energy:
                        visited[state] = next_energy
                        queue.append((nr, nc, next_mask, next_energy, steps + 1))

        # If the queue empties without returning, it's impossible to collect everything
        return -1
