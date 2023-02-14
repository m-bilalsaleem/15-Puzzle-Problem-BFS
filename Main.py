#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import deque

def is_solvable(puzzle):
    inversion = 0
    for i in range(len(puzzle)):
        for j in range(i + 1, len(puzzle)):
            if puzzle[i] != 0 and puzzle[j] != 0 and puzzle[i] > puzzle[j]:
                inversion += 1

    return inversion % 2 == 0

def find_zero_pos(puzzle):
    for i in range(len(puzzle)):
        if puzzle[i] == 0:
            return (i // 4, i % 4)
    return (-1, -1)

def bfs(start, end):
    if not is_solvable(start) or not is_solvable(end):
        return None

    visited = set()
    queue = deque([(start, [])])
    visited.add(tuple(start))

    while queue:
        puzzle, path = queue.popleft()
        if puzzle == end:
            return path

        row, col = find_zero_pos(puzzle)

        for r, c in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
            if 0 <= r < 4 and 0 <= c < 4:
                new_puzzle = puzzle[:]
                index = r * 4 + c
                zero_index = row * 4 + col
                new_puzzle[zero_index], new_puzzle[index] = new_puzzle[index], new_puzzle[zero_index]
                tuple_puzzle = tuple(new_puzzle)
                if tuple_puzzle not in visited:
                    visited.add(tuple_puzzle)
                    queue.append((new_puzzle, path + [tuple_puzzle]))

    return None

start = [1, 8, 3, 2, 5, 6, 7, 4, 9, 10, 11, 12, 13, 14, 0, 15]
end = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 0, 14, 15]

result = bfs(start, end)

if result is None:
    print("No solution found")
else:
    print("Solution found in", len(result), "moves:")
    for move in result:
        print(move)


# In[ ]:




