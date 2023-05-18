graph = [[0, 1, 0, 0],
         [1, 0, 1, 0],
         [0, 1, 0, 1],
         [0, 0, 1, 0]]

n = len(graph)
visited = [False] * n
tin = [0] * n
low = [0] * n
timer = 0

def dfs(node, parent=-1):
    global timer
    visited[node] = True
    tin[node] = low[node] = timer
    timer += 1
    for neighbor in range(n):
        if graph[node][neighbor]:
            if neighbor == parent:
                continue
            if visited[neighbor]:
                low[node] = min(low[node], tin[neighbor])
            else:
                dfs(neighbor, node)
                low[node] = min(low[node], low[neighbor])
                if low[neighbor] > tin[node]:
                    print("bridge: ", node, neighbor)

for i in range(n):
    if not visited[i]:
        dfs(i)
