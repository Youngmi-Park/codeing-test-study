'''
n-queen
link: https://www.acmicpc.net/problem/9663

nxn 체스 보드에 n개의 퀸을 배치하는 문제
- 어떤 퀸도 다른 퀸에 의해서 잡아먹히지 않도록 배치해야한다.
- 퀸은 같은 행, 열, 대각선에 다른 퀸을 둘 수 없다.

문제 풀이 아이디어
상태 공간 트리를 탐색하는 백트래킹 방법
기본적으로 같은 행에는 놓을 수 없다고 가정하면 
n=4일 때, 후보 해답은 4x4x4x4=256가지의 탐색 공간이 있음
그렇다면 어떻게 pruning 할것인가
현재 노드가 promising한지 확인하고 아니라면 하위노드는 가지 않는다.
promising function을 찾아야 pruning할 수 있다.

'''
n = int(input()) # 체스판 크기와 퀸 개수 N
queen = [0] * n # 퀸을 저장하는 배열, 열 위치 저장
result = 0 # 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수

def is_promising(x):
  for i in range(x):
    # 현재 놓고자 하는 퀸이 이전에 저장된 퀸들과 비교했을 때 유망한지를 확인한다.
    # 유망하지 않은 조건: 같은 열일 때, 열 차이와 행 차이가 같을 때 
    if queen[x] == queen[i] or abs(queen[x] - queen[i]) == abs(x - i):
      return 0
  return True
  
def n_queens(x):
  global result
  if x == n : #저장한 퀸의 개수가 n개 라면 
    result += 1 # 경우의 수 +1
    return # 종료
  else:
    for i in range(n): # n개의 열에 대해서 탐색
      queen[x] = i # x 행 i 열, # [x, i]에 퀸을 놓겠다.
      if is_promising(x): # 현재 노드가 유망한지 확인
        n_queens(x+1) # 다음 행에 대해서 탐색

n_queens(0) # depth 표시, 행을 의미
print(result)
