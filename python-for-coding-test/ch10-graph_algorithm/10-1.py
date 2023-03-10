# 특정 원소가 속한 집합 찾기 (루트 노드를 찾는 함수)
def find_parent(parent, node):
  # 루트노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
  if parent[node] != node:
    return find_parent(parent, parent[node]) 
  return node # 특정 원소가 속한 집합의 루트 노드 번호 반환

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
  a = find_parent(parent, a) # 노드 a의 루트노드 찾기
  b = find_parent(parent, b) # 노드 b의 루트노드 찾기
  # 루트 번호를 비교해서 큰쪽이 작은 쪽을 가리키도록 연결
  if a < b:
    parent[b] = a
  else:
    parent[a] = b
    
v, e = map(int, input().split()) # 노드의 개수 v와 간선의 개수(union 연산) e 입력받기
parent = [0] * (v+1) # 부모 테이블 초기화

# 부모 테이블에 부모를 자기 자신으로 초기화
for i in range(1, v+1):
	parent[i] = i

# union 연산 수행, 간선 개수에 따라서 연결 여부 확인
for i in range(e): 
  a, b = map(int, input().split())
  union_parent(parent, a, b) # 노드 a, b에 대해서 union

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합:', end = ' ')
for i in range(1, v+1):
  print(find_parent(parent, i), end=' ') # 실제로는 루트 노드 출력, 루트노드가 같은 원소끼리는 같은 집합이다.

print()

# 부모테이블 내용 출력, 부모에 대한 정보, 루트는 아님
print('부모 테이블:', end = ' ')
for i in range(1, v+1):
  print(parent[i], end = ' ')
