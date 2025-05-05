from collections import deque
def water_jug_bfs(jug1_cap, jug2_cap, target):
    visited = set()
    queue = deque()
    queue.append((0, 0))
    while queue:
        jug1, jug2 = queue.popleft()
        if (jug1, jug2) in visited:
            continue
        print(f"Jug1: {jug1}L, Jug2: {jug2}L")
        visited.add((jug1, jug2))
        if jug1 == target or jug2 == target:
            print("Goal reached!")
            return True
        actions = [
            (jug1_cap, jug2),           
            (jug1, jug2_cap),           
            (0, jug2),                  
            (jug1, 0),                  
            (0, jug1 + jug2) if jug1 + jug2 <= jug2_cap else (jug1 - (jug2_cap - jug2), jug2_cap),  # Pour Jug1 → Jug2
            (jug1 + jug2, 0) if jug1 + jug2 <= jug1_cap else (jug1_cap, jug2 - (jug1_cap - jug1))   # Pour Jug2 → Jug1
        ]

        for action in actions:
            
            if action not in visited:
                queue.append(action)
    print("No solution found.")
    return False
water_jug_bfs(4, 3, 2)