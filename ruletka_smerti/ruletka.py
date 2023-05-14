def dfs(v, p, d, pos):
    # v: current vertex
    # p: parent vertex
    # d: distance from starting vertex
    # pos: position on cycle (if part of a cycle)

    global coords

    coords[v] = (d % 2, pos)

    for u in adj[v]:
        if u == p:
            continue
        if coords[u]:
            # cycle detected
            cycle_len = d - coords[u][0] + 1
            cycle_start = coords[u][1]
            for i in range(cycle_len):
                coords[u] = ((coords[u][0] + i) % 2, cycle_start + i)
                u = adj[u][0]  # follow cycle
            return True
        elif dfs(u, v, d+1, 0 if not cycles[v] else (pos+1)%len(cycles[v])):
            return True
    return False

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    # check if graph is a tree
    if m != n-1:
        print("No")
        continue

    # find cycles and their lengths
    cycles = [None] * (n+1)
    cycle_len = [0] * (n+1)
    visited = [False] * (n+1)
    stack = []
    for i in range(1, n+1):
        if visited[i]:
            continue
        stack.append((i, 0))
        while stack:
            v, p = stack.pop()
            visited[v] = True
            for u in adj[v]:
                if u == p:
                    continue
                if visited[u]:
                    # cycle detected
                    cycles[v] = []
                    while stack[-1][0] != u:
                        cycles[v].append(stack.pop()[0])
                    cycles[v].append(u)
                    cycle_len[v] = len(cycles[v])
                else:
                    stack.append((u, v))

    # assign coordinates using DFS
    coords = [(0, 0)] * (n+1)
    dfs(1, 0, 0, 0)

    # check if embedding is possible
    for v in range(1, n+1):
        for u in adj[v]:
            if coords[v][0] == coords[u][0]:
                print("No")
                break
        else:
            continue
        break
    else:
        print("Yes")
        for v in range(1, n+1):
            print(coords[v][0], coords[v][1])
