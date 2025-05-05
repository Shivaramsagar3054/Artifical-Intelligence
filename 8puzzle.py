from collections import deque

goal_state = [1, 2, 3,
              4, 5, 6,
              7, 8, 0]
moves = {
    'UP': -3,
    'DOWN': 3,
    'LEFT': -1,
    'RIGHT': 1
}
def is_valid(pos, move):
    if move == 'LEFT' and pos % 3 == 0:
        return False
    if move == 'RIGHT' and pos % 3 == 2:
        return False
    if move == 'UP' and pos < 3:
        return False
    if move == 'DOWN' and pos > 5:
        return False
    return True

def solve_puzzle(start):
    visited = set()
    queue = deque()
    queue.append((start, []))

    while queue:
        current, path = queue.popleft()
        visited.add(tuple(current))

        if current == goal_state:
            return path + [current]

        zero_pos = current.index(0)

        for move, delta in moves.items():
            if is_valid(zero_pos, move):
                new_board = current[:]
                new_pos = zero_pos + delta
                new_board[zero_pos], new_board[new_pos] = new_board[new_pos], new_board[zero_pos]

                if tuple(new_board) not in visited:
                    queue.append((new_board, path + [current]))

    return None
start_state = [5, 4, 0,
               6, 1, 8,
               7, 3, 2]

solution = solve_puzzle(start_state)

if solution:
    for step in solution:
        print(step[:3])
        print(step[3:6])
        print(step[6:9])
        print("------")
else:
    print("No solution found.")