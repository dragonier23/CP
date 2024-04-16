testcases = int(input())

for i in range(testcases):
    cardCount = int(input())
    cards = list(map(int, input().split(" ")))
    solution = len(cards) - len(set(cards))
    print(solution)