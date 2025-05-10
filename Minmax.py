def minimax(total, is_max_turn):
    if total >= 15:
        return -1 if is_max_turn else 1
    if is_max_turn:
        best = -float('inf')
        for i in range(1, 4):
            score = minimax(total + i, False)
            best = max(best, score)
        return best
    else:
        best = float('inf')
        for i in range(1, 4):
            score = minimax(total + i, True)
            best = min(best, score)
        return best
def best_move(total):
    best_score = -float('inf')
    move = -1
    for i in range(1, 4):
        score = minimax(total + i, False)
        if score > best_score:
            best_score = score
            move = i
    return move
current_total = 0
print("Best move at start:", best_move(current_total))