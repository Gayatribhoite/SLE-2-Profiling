import timeit

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

def dfs(start, goal):
    stack = [start]
    visited = set()
    nodes_explored = 0

    while stack:
        current = stack.pop()

        if current not in visited:
            visited.add(current)
            nodes_explored += 1

            if current == goal:
                return nodes_explored

            for neighbour in reversed(graph[current]):
                if neighbour not in visited:
                    stack.append(neighbour)

    return nodes_explored


runs = 100000

time_taken = timeit.timeit(
    lambda: dfs('S', 'AF'),
    number=runs
)

nodes = dfs('S', 'AF')

average_time_ms = (time_taken / runs) * 1000

print("DFS-1")
print("Nodes explored:", nodes)
print("Average execution time (ms):", average_time_ms)
