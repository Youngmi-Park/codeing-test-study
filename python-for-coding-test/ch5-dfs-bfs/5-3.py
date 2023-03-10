'''
5장 DFS/BFS 실전문제3 - 음료수 얼려 먹기
난이도: 중하, 풀이시간: 40분, 시간제한: 1초, 메모리제한: 128MB
문제설명
N x M 크기의 얼음틀에서 뚫려 있는 부분은 0 칸막이가 있는 부분은 1로 표시된다.
구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.
이대 얼름 들의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 장성하시오.
입력조건
첫번째 줄에 얼음 틀의 세로 길이 N과 가로길이 M이 주어진다.(1<=N,M<=1000)
두번째 줄부터 N+1번쨰 줄까지 얼음 틀의 형태가 주어진다.
이때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1이다.
출력조건
한번에 만들수 있는 아이스크림의 개수를 출력한다.
문제 풀이 아이디어
그래프로 간주하고 풀이하면 dfs로 풀수있는 문제이다.
한 칸이 노드라고 생각했을 때, 그래프를 표현할 수 있다.
노드가 0이면 상하좌우의 값을 확인하고 0인지 1인지 판단한 다음 0이라면 같은 작업을 반복하면된다.
만일 1이라면 탐색을 멈추고 다음 노드로 넘어가면 된다.
쉽게 말하면 0끼리 연결된 것들의 개수를 구하면 됨! dfs 호출 횟수가 아이스크림의 개수
dfs는 스택으로 구현한다. (python의 list를 사용)
노드를 방문하면 스택에 넣었다가 자식노드 중에 방문안한 노드가 있으면 그중 하나를 또 스택에 넣는다.(없을 때까지 반복)
자식노드들을 모두 방문하면 스택에서 제거
재귀적 호출로 작업가능.
'''

n, m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1 # 방문처리
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

result = 0 # dfs 호출 횟수
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우 방향
def dfs(graph, x, y):
  graph[x][y] = 1 # 방문처리
  for dx, dy in dir:
    nx, ny = x + dx, y + dy
    if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
      dfs(graph, nx, ny)

count = 0 # dfs 호출 횟수
for i in range(n):
  for j in range(m):
    if graph[i][j] == 0:
      dfs(graph, i, j)
      count += 1
print(count)
