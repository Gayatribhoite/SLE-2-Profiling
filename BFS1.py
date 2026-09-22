import timeit
from collections import deque

graph = {
    'S': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['E', 'F'],
    'C': ['G', 'H'],
    'D': ['I', 'J'],
    'E': ['K', 'L'],
    'F': ['M', 'N'],
    'G': ['O', 'P'],
    'H': ['Q'],
    'I': ['R'],
    'J': ['T', 'U'],
    'K': ['V', 'W'],
    'L': ['X'],
    'M': ['Y'],
    'N': ['Z'],
    'O': ['AA'],
    'P': [],
    'Q': [],
    'R': [],
    'T': [],
    'U': [],
    'V': [],
    'W': [],
    'X': [],
    'Y': [],
    'Z': [],
    'AA': ['AB', 'AC'],
    'AB': ['AD'],
    'AC': ['AE'],
    'AD': [],
    'AE': ['AF'],
    'AF': []
}

def bfs(start, goal):
    queue = deque([start])
    visited = set([start])
    nodes_explored = 0

    while queue:
        current = queue.popleft()
        nodes_explored += 1

        if current == goal:
            return nodes_explored

        for neighbour in graph[current]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

    return nodes_explored


runs = 100000

time_taken = timeit.timeit(
    lambda: bfs('S', 'AF'),
    number=runs
)

nodes = bfs('S', 'AF')

average_time_ms = (time_taken / runs) * 1000

print("BFS-1")
print("Nodes explored:", nodes)
print("Average execution time (ms):", average_time_ms)