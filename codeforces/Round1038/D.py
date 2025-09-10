import heapq

for _ in range(int(input())):
    n, m = map(int, input().split())

    E = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(lambda x: int(x) - 1, input().split())
        E[u].append(v)
        E[v].append(u)

    pq = []
    heapq.heappush(pq, (0, 0, 0))  # (dist, wait, node)

    best = dict()  # best[(node)] = (dist, wait)
    present = [0] * n

    while pq:
        dist, wait, curr = heapq.heappop(pq)
        present[curr] = 0

        if curr in best and best[curr] <= (dist, wait):
            continue  # We have already seen a better or equal path

        best[curr] = (dist, wait)

        if curr == n - 1:
            print(dist, wait)
            break

        neighbours = E[curr]
        c = len(neighbours)
        for i in range(c):
            nxt = neighbours[(dist + i) % c]
            new_dist = dist + i + 1
            new_wait = wait + i
            if present[nxt] == 0 or (nxt not in best or (new_dist, new_wait) < best.get(nxt, (float('inf'), float('inf')))):
                heapq.heappush(pq, (new_dist, new_wait, nxt))
            present[nxt] = 1