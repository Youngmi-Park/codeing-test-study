# 플로이드 워셜 알고리즘 소스코드
INF = int(1e9) # 무한을 의미하는 값 10억

n = int(input()) # 노드 개수
m = int(input()) # 간선 개수

# 최단 거리 정보를 저장하는 2차원 리스트
graph = [[INF] * (n+1) for _ in range(n+1)] # 노드 개수의 제곱만큼, 처음에는 무한으로 초기화

# 자기 자신으로 가는 비용은 0으로 변경
# for a in range(1, n+1):
#   for b in range(1, n+1):
#     if a == b: # 같다면, 자기자신이라면
#       graph[a][b] = 0 # 비용으로 0으로 설정
for i in range(1, n+1):
  graph[i][i] = 0

# 간선 m개의 정보를 입력 받아 그 값으로 초기화
for _ in range(m):
  a, b, c = map(int, input().split())# 노드 A에서 노드 B로 가는 비용은 C
  graph[a][b] = c
 
# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b]) # 기존의 A→B 비용과 A→K + K→B 비용을 비교
      
# 수행 결과 출력, 2차원 리스트 형태로 출력
for a in range(1, n+1):
  for b in range(1, n+1):
    # 도달할 수 없는 경우 INFINITY라고 출력
    if graph[a][b] == INF:
      print("INFINITY", end=' ')
    else:
      print(graph[a][b], end=' ')
  print()
