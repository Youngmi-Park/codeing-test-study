from collections import deque

# 정점 개수, 간선 개수, 탐색 시작 정점
n, m, v = map(int,input().split())
# m개의 두 정점 번호
graph = [[] for _ in range(n + 1)] # 빈 배열 선언
for i in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
  graph[a].sort()
  graph[b].sort()
  
# stack - 재귀적으로 구현
def dfs(graph, visited, v):
  visited[v] = True # 방문 처리
  print(v, end = ' ')
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, visited, i)

# queue
def bfs(graph, visited, v):
  queue = deque([])
  queue.append(v)
  visited[v] = True
  while queue:
    node = queue.popleft()
    print(node, end = ' ')
    for i in graph[node]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True
        

visited = [False] * (n + 1)
dfs(graph, visited, v)
print()
visited = [False] * (n + 1)
bfs(graph, visited, v)
