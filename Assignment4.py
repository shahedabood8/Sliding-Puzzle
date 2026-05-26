from collections import deque

# Define initial and goal states
initial_state = ('A', 'A', '_', 'B', 'B')
goal_state = ('B', 'B', '_', 'A', 'A')

# Slide or jump forward only (no backing up)
def get_successors(state):
    successors = []
    idx = state.index('_')

    def swap(i, j):
        lst = list(state)
        lst[i], lst[j] = lst[j], lst[i]
        return tuple(lst)

    if idx > 0 and state[idx - 1] != '_':
        successors.append((swap(idx, idx - 1), f"{state[idx - 1]} slides left"))
    if idx > 1 and state[idx - 2] != '_':
        successors.append((swap(idx, idx - 2), f"{state[idx - 2]} jumps left"))
    if idx < len(state) - 1 and state[idx + 1] != '_':
        successors.append((swap(idx, idx + 1), f"{state[idx + 1]} slides right"))
    if idx < len(state) - 2 and state[idx + 2] != '_':
        successors.append((swap(idx, idx + 2), f"{state[idx + 2]} jumps right"))

    return successors

# BFS to build and print the search tree
def bfs(start, goal):
    queue = deque([(start, [], [])])  # (state, path, actions)
    visited = set()

    print("Search Tree:\n")
    while queue:
        current, path, actions = queue.popleft()
        print("State:", current, "| Moves:", ' -> '.join(actions))
        if current == goal:
            print("\nSolution Path:")
            for i, act in enumerate(actions):
                print(f"{i + 1}. {act}")
            return

        visited.add(current)
        for succ, action in get_successors(current):
            if succ not in visited:
                queue.append((succ, path + [current], actions + [action]))

    print("No solution found.")

bfs(initial_state, goal_state)