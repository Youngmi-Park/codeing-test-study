# 간단한 다익스트라 알고리즘
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

n, m = map(int, input().split())# 노드 개수, 간선 개수 입력 받기
start = int(input())# 시작 노드 번호

# 노드개수+1 크기로 할당하여 노드 번호를 인덱스로 바로 접근할 수 있도록 함
graph = [[] for _ in range(n+1)] # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
visited = [False] * (n+1) # 방문정보를 체크하는 리스트
distance = [INF] * (n+1) # 각 노드에 대한 최단 거리를 담는 1차원 리스트 선언, 무한으로 초기화

# 모든 간선 정보 입력 받기(방향 그래프)
for _ in range(m):
  a, b, c = map(int, input().split()) # 노드, 노드, 비용 
  graph[a].append((b, c))

# 방문하지 않은 노드 중에서 가장 최단 거리가 짧은 노드의 번호를 반환하는 함수
def get_smallest_node():
  min_value = INF # 최단 거리 확인
  index =  0 # 가장 최단 거리가 짧은 노드의 인덱스
  for i in range(1, n+1):
    if distance[i] < min_value and not visited[i]:
      min_value = distance[i]
      index = i
  return index     

# 다익스트라 함수: 하나의 출발노드에서 다른 노드로 최단거리를 구함
def dijkstra(start):
  distance[start] = 0 # 시작노드 초기화, 자기자신까지의 거리는
  visited[start] = True # 방문처리
  for j in graph[start]: # start 노드에 연결된 노드를 탐
    distance[j[0]] = j[1] # j[0]는 노드b j[1]는 비용 c
  for i in range(n-1):
    now = get_smallest_node() # 최단거리가 가장 짧은 
    visited[now] = True # 방문처리
    for j in graph[now]: # 현재 노드에 연결된 노드 탐색
        # 현재 노드를 거쳐서 가는 것과 현재 최단 거리를 비교
      distance[j[0]] = min(distance[j[0]], distance[now] + j[1])

# 다익스트라 수행
dijkstra(start) # start 노드로 부터 탐색
	
# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n+1):
  if distance[i] == INF:
    print("INFINITY")
  else:
    print(distance[i]) # start 노드에서 i까지의 최단거리 출력
