'''
게임 개발
게임 캐릭터가 맵 안에서 움직이는 시스템 개발
캐릭터가 있는 곳은 1x1크기의 정사각형으로 이루어진 NxM 크기의 직사각형으로 각각의 칸은 육지 또는 바다이다.
캐릭터는 동서남북 중 한 곳을 바라본다.
맵의 각 칸은 (A, B)로 나타낼 수 있다.
A는 북쪽으로부터 떨어진 칸의 개수
B는 서쪽으로부터 떨어진 칸의 개수
캐릭터는 상하좌우로 이동 가능
바다로는 이동 불가

캐릭터 이동 메뉴얼
1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반시계 방향 90도)부터 차례대로 갈 곳을 정한다.
2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면 왼쪽 방향으로 회전한 다음 왼쪽으로 한칸 전진한다. 왼쪽 방향에 가보지 않은 칸이 없다면 왼쪽 방향으로 회전만 수행 후 1 단계로
3. 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우 바라보는 방향을 유지한 채로 한칸 뒤로 가고 1 단계로. 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.

이동을 마친 후 캐릭터가 방문한 칸의 수를 출력
'''
n, m = map(int, input().split()) # n, m 입력받기
x, y, d = map(int, input().split()) # 칸의 좌표 a, b 방향 d
# d 0: 북쪽 1: 동쪽 2: 남쪽 3: 서쪽
graph = [list(map(int, input().split())) for _ in range(n)] # 입력받은 맵, 0 육지, 1 바다, 외곽은 항상 바다 
visited = [[0] * m for _ in range(n)]# 맵에서 방문한 칸 저장

dir = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 북, 동, 남, 서

# 왼쪽으로 회전
def turn_left():
  global d
  d -= 1
  if d == -1:
    d = 3

visited[x][y] = 1 # 현재 좌표 방문 처리
count = 1 # 방문한 칸 수, 시작 지점도 카운
turn_time = 0 # 동서남북 회전 수

while True:
  turn_left() # 왼쪽으로 회전
  nx, ny = x + dir[d][0], y + dir[d][1] # 왼쪽 방향으로 이동
  #외곽이 항상 바다이기 때문에 nx, ny 범위 확인 안해도 됨
  if graph[nx][ny] == 0 and visited[nx][ny] == 0:  # 육지(0)이고 방문하지 않은 칸이면 이동
    count += 1 # 방문한 칸 수 증가
    visited[nx][ny] = 1 # 방문 처리
    x, y = nx, ny # 현재 위치 갱신
    turn_time = 0
    continue
    '''
   continue 구문이 없어도 동일한 결과가 출력됩니다.
   저는 while 문 안에 2개 이상의 if 문 블록(block)이 존재하는 상황에서 앞쪽에 존재하는 if 문이 실행된 이후에 
   뒤쪽의 if 문이 실행되지 않을 것이 명확한 경우에 앞쪽 if 문 내부에 continue 구문을 명시적으로 넣어주는 코드 작성 습관이 있습니다.
   https://github.com/ndb796/python-for-coding-test/issues/53
    '''
  else:  # 회전한 칸이 바다이거나 방문한 칸이면 회전 수 증가
    turn_time += 1
  if turn_time == 4: # 4방향 모두 갈 수 없는 경우
    nx, ny = x - dir[d][0], y - dir[d][0] # 현재 방향에서 뒤의 좌표 확인
    if graph[nx][ny] == 0: # 육지면 뒤로 갈 수 있음
      x, y = nx, ny
    else: # 바다면
      break # 종료
    turn_time = 0

print(count)