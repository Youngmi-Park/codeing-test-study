# 개선된 다익스트라 알고리즘 O(ElogV)

import sys
import heapq # 힙 자료구조 사용 가장 가까운 노드를 찾는데 O(logV)를 보장 V는 노드 개수
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값 10억 설정

n, m = map(int, input().split())# 노드 개수, 간선 개수
start = int(input()) # 시작 노드
graph = [[] for i in range(n+1)]# 각 노드에 연결되어 있는 노드 정보를 담는 리스트
distance = [INF] * (n+1) # 최단 거리를 저장하기 위한 1차원 리스트(최단 거리 테이블), 무한으로 초기화
 
# 그래프 연결 정보 입력받기
for _ in range(m):
  a, b, c = map(int, input().split()) # 노드, 노드, 거리
  graph[a].append((b, c)) # a 노드에서 b 노드로 가는 비용c 

# 다익스트라 함수
def dijkstra(start):
  q = [] 
  heapq.heappush(q,(0, start)) # 시작 노드로 가기 위한 최단경로는 0으로 설정하여 삽입 (거리, 노드)
  distance[start] = 0 # 시작 노드에 대한 최단 거리는 0으로 정의
  while q: # 큐가 비어있지 않다면
    dist, node = heapq.heappop(q) # 힙에 있는 가장 최단 거리가 짧은 노드 꺼내기
    if distance[node] < dist: # visited 대신 현재 노드가 이미 처리된적 있는 노드인지 확인하고 무시한다.
      continue
    # 현재 노드와 연결된 다른 인접한 노드들을 확인
    for i in graph[node]:
      cost = dist + i[1] # 현재노드의 거리 + 인접노드의 거리
      if distance[i[0]] > cost: # cost가 최단 거리 리스트에 저장된 값보다 작다면
        distance[i[0]] = cost # 최단 거리 갱신
        heapq.heappush(q, (cost, i[0]))# 힙에 삽입 (거리, 노드)
        
# 다익스트라 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단거리 출력
for i in range(1, n+1):
  if distance[i] == INF: # 값이 10억이면 무한이라고 출력
    print("INFINITY")
  else: # 도달할 수 있으면 거리를 출력
    print(distance[i]) 
