# SLE-3 – Architectural Design Using C4 Model

## Student Details

- **Name:** Gayatri Sanjay Bhoite
- **PRN:** 25UAM110
- **Division:** B
- **Subject:** SLE-3
- **System:** Graph Search System
- **Algorithms:** BFS-1 and DFS-1

---

## 1. Project Overview

This project presents the architectural design of a Graph Search System using the **C4 Model**.

The system performs graph search from a **Start Node S** to a **Goal Node AF** on a **32-node graph** using two search algorithms:

- Breadth-First Search (BFS-1)
- Depth-First Search (DFS-1)

The architecture is represented using the four C4 Model levels: Context, Container, Component, and Code.

---

## 2. Objective

The main objectives of this SLE-3 are:

- To represent the architecture of the Graph Search System.
- To show how the user interacts with the system.
- To identify the major containers and their responsibilities.
- To represent the internal components of the Search Engine.
- To identify the main functions and data structures used at the code level.
- To connect the architectural design with the BFS-1 and DFS-1 implementation from SLE-2.

---

## 3. C4 Model

### Level 1 – Context Diagram

The Context Diagram shows the Graph Search System as a single system and represents the interaction between the user and the system.

**Input:**
- 32-node graph
- Start Node: S
- Goal Node: AF
- Search Algorithm: BFS-1 or DFS-1

**Output:**
- Search result/path

---

### Level 2 – Container Diagram

The Container Diagram breaks the system into its major functional parts:

1. Graph / Input
2. Search Controller
3. BFS-1
4. DFS-1
5. Visited Node Tracking
6. Goal Check
7. Result Output

These containers show the flow of graph data through the selected search algorithm and finally produce the search result.

---

### Level 3 – Component Diagram

The Component Diagram focuses on the **Search Controller / Search Engine** and represents its internal components:

- **BFS-1** – Queue + Level Search
- **DFS-1** – Depth + Backtracking
- **Visited Set** – Avoids repeated exploration
- **Goal Test** – Checks whether the current node is AF
- **Search Result** – Provides the path/result

---

### Level 4 – Code Level

The Code Level identifies the main functions and data structures used in the search implementation.

| Code Element | Purpose |
|---|---|
| `bfs_search()` | Performs Breadth-First Search using a queue and level-wise exploration. |
| `dfs_search()` | Performs Depth-First Search using depth-first exploration and backtracking. |
| `visited_set` | Tracks visited nodes and prevents repeated exploration. |
| `goal_test()` | Checks whether the current node is the goal node AF. |
| `search_result` | Stores and returns the search result/path. |

---

## 4. System Flow

```text
Graph / Input
      ↓
Search Controller
      ↓
 ┌────┴────┐
 ↓         ↓
BFS-1     DFS-1
 └────┬────┘
      ↓
Visited Node Tracking
      ↓
Goal Check
      ↓
Result Output