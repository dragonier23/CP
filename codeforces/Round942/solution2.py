testcases = int(input())
'''
def flip(pos, xs):
    xs[(pos - 1) % len(xs)] = 'D' if xs[(pos - 1) % len(xs)] == 'U' else 'U'
    xs[(pos + 1) % len(xs)] = 'D' if xs[(pos + 1) % len(xs)] == 'U' else 'U'
    xs.pop(pos)
    return (xs)

# if it is alive turn, turn = true, else false 
def solution(turn, xs):
    if len(xs) == 0  or (not('U' in xs)):
        return 0 if turn else 1
    # from this point, at least one U 
    if len(xs) == 1: 
        return 1 if turn else 0
    if len(xs) == 2:
        if xs == ['U', 'U']:
            return 0 if turn else 1
        else:
            return 1 if turn else 0
    return max([solution(not(turn), flip(i, xs.copy())) for i in range(len(xs)) if xs[i] == 'U'])
'''
for i in range(testcases):
    length = int(input())
    puzzle = list(input())
    print("YES" if (len(list(filter(lambda x: x == 'U', puzzle))) % 2) else "NO")
    