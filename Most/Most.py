
def dfs(graph, visited, node):
    visited[node] = True
    for i in range(len(graph)):
        if graph[node][i] and not visited[i]:
            dfs(graph, visited, i)

def find_edge_to_remove(graph):
    for i in range(len(graph)):
        for j in range(i+1, len(graph)):
            if graph[i][j]:

                graph[i][j] = 0
                graph[j][i] = 0

                visited = [False] * len(graph)
                dfs(graph, visited, i)

                if not all(visited):

                    return (i, j)

                graph[i][j] = 1
                graph[j][i] = 1

    return None

graph = [[0, 1, 0, 0],
         [1, 0, 1, 0],
         [0, 1, 0, 1],
         [0, 0, 1, 0]]
edge = find_edge_to_remove(graph)
if edge is not None:
    print("bridge: ", edge)
else:
    print("cant.")
