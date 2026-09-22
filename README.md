# SLE-2: BFS and DFS Profiling

## Course

**02AML204 – Introduction to Artificial Intelligence**

## Problem Statement

Perform a search from **Start Node S** to **Goal Node AF** using **BFS and DFS search algorithms**, and compare their performance based on **execution time and number of nodes explored**.

## Student Details

* **Name:** Gayatri Sanjay Bhoite
* **PRN:** 25UAM110
* **Division:** B

## Algorithms Implemented

1. **BFS-1** – Breadth First Search using a queue.
2. **DFS-1** – Depth First Search using a stack.

## Graph

**Start Node:** S
**Goal Node:** AF

The same graph and the same start and goal nodes were used for both algorithms.

## Profiling Method

* Execution time was measured using Python `timeit`.
* Profiling was performed using **py-spy 0.4.2**.
* Both programs were successfully profiled with **0 errors**.

## Results

| Algorithm | Nodes Explored | Average Execution Time (ms) | py-spy Samples | Errors |
| --------- | -------------: | --------------------------: | -------------: | -----: |
| BFS-1     |             32 |                    0.005897 |              4 |      0 |
| DFS-1     |             11 |                    0.002954 |             10 |      0 |

## Observation

For this particular graph and traversal order, DFS-1 explored fewer nodes than BFS-1. DFS-1 also recorded a lower measured execution time in the test run. BFS-1 explored 32 nodes, while DFS-1 explored 11 nodes. The results depend on the graph structure, node ordering, implementation and execution environment.

## Best, Average and Worst Case

* **Best Case:** Goal node is found very early in the traversal.
* **Average Case:** The goal node is found after exploring a moderate number of nodes.
* **Worst Case:** The algorithm explores most or all reachable nodes before finding the goal or determining that it is not present.

## AI Contribution

AI was used for guidance in understanding the SLE-2 requirements, algorithm implementation support, profiling guidance, and preparation of the README and report.

## Files

* `BFS1.py`
* `DFS1`
* `bfs1.svg`
* `dfs1.svg`
* `README.md`
* `Contribution_Log.md`
