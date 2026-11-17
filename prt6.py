CAP_A = 4
CAP_B = 3
GOAL = 2


def get_next_states(state):
    a, b = state
    states = []

    states.append(((CAP_A, b), "Fill A"))
    states.append(((a, CAP_B), "Fill B"))
    states.append(((0, b), "Empty A"))
    states.append(((a, 0), "Empty B"))

    amount = min(a, CAP_B - b)
    states.append(((a - amount, b + amount), "Pour A -> B"))

    amount = min(b, CAP_A - a)
    states.append(((a + amount, b - amount), "Pour B -> A"))

    result = []
    seen = set()

    for new_state, action in states:
        if new_state not in seen and new_state != state:
            seen.add(new_state)
            result.append((new_state, action))

    return result


def dfs(state, visited, path):
    a, b = state

    if a == GOAL or b == GOAL:
        return path

    visited.add(state)

    for next_state, action in get_next_states(state):
        if next_state not in visited:
            result = dfs(
                next_state,
                visited,
                path + [(action, next_state)]
            )

            if result is not None:
                return result

    return None


start = (0, 0)
visited = set()
solution = dfs(start, visited, [])

if solution:
    print("Solution found!")
    print("Initial state:", start)

    for i, (action, state) in enumerate(solution, 1):
        print("Step", i, ":", action, "->", state)

    print("Number of steps:", len(solution))
else:
    print("No solution exists.")