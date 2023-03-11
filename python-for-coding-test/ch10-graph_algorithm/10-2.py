# 서로소 집합을 활용한 사이클 판별 소스코드
# 특정 원소가 속한 집합을 찾기, 경로 압축 기법
def find_parent(parent, node):
  if parent[node] != node:
    parent[node] = find_parent(parent, parent[node])
  return parent[node]

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
  a = find_parent(parent, a) # 루트 노드 찾기
  b = find_parent(parent, b) # 루트 노드 찾기
  if a < b:
    parent[b] = a # 큰 노드가 작은 노드를 가리키게 함
  else:
    parent[a] = b

v, e = map(int, input().split()) # 노드 개수, 간선(unoin) 개수 입력
parent = [0] * (v+1) # 부모 테이블 생성
for i in range(1, v+1): # 자기자신으로 부모 갱싱
  parent[i] = i

cycle = False # 사이클 발생 여부
for i in range(e):
  a, b = map(int, input().split()) # 간선에 해당하는 노드 2개
  # 이미 같은 집합이라면, 사이클이 발생한 것이므로 종료
  if find_parent(parent, a) == find_parent(parent, b):
    cycle = True # 사이클 발생
    break
  # 사이클이 발생하지 않았다면 union
  else:
    union_parent(parent, a, b)

# 사이클 발생 여부 출력
if cycle:
  print("사이클이 발생했습니다.")
else:
  print("사이클이 발생하지 않았습니다.")
