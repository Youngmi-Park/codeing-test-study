# https://www.acmicpc.net/problem/15649
# 순열문제, 뽑고 순서를 고려해야함
n, m = map(int, input().split())
num = []

def dfs():
  if len(num) == m: # 선택한 숫자의 개수가 m개라면
    print(' '.join(map(str, num))) # 출력
    return

  for i in range(1, n+1): # 1부터 n까지 숫자를 탐색
    if i not in num: # 배열 안에 없다면, 중복X, 순서O
      num.append(i)
      dfs()
      num.pop()
     
dfs()
