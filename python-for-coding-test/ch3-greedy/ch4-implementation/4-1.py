'''
여행가 A는 NxN 크기의 정사각형 공간 위에 서있다.
공간은 1x1 크기의 정사각형으로 이루어져있다.
가장 왼쪽 위 좌표는 (1, 1) 가장 오른쪽 아래 좌표는 (N, N)이다.
A는 상, 하, 좌, 우로 이동할 수 있으며 시작 좌표는 항상 (1, 1)이다.
A가 이동할 여행 계획서가 있다.
L: 왼쪽으로 한칸
R: 오른쪽으로 한칸
U: 위쪽으로 한칸
D: 아래쪽으로 한칸
정사각형 공간을 벗어나는 움직임은 무시된다.
A가 최종적으로 도착하는 지점을 출력하는 프로그램
최종 좌표 (X, Y)를 공백으로 구분하여 출력
'''
n = int(input()) # 공간의 크기
plan = input().split()# 여행가의 이동 계획

direction = {'L':(0, -1), 'R':(0, 1), 'U':(-1, 0) , 'D':(1, 0)} # 이동 방향
x, y = 1, 1 # 시작 좌표

for i in plan: # 이동 계획 순서대로 처리, O(N)
  nx, ny = x + direction[i][0], y + direction[i][1]
  if 1 <= nx <= n and 1 <= ny <= n:
    x, y = nx, ny

print(x, y)
# 연산횟수는 이동 횟수에 비례한다 O(N)


n = int(input())
d = list(map(str,input().split()))
start = [1,1]
print(start[0],start[1])
for i in d:
    if i == 'R' and start[1] < n:
        start[1] += 1
    elif i == 'L' and start[1] > 1:
        start[1] -= 1
    elif i == 'D' and start[0] < n:
        start[0] +=1
    elif i == 'U' and start[0] > 1:
        start[0] -=1

print(' '.join(map(str,start)))
