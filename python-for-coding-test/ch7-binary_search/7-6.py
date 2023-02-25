'''
7장 이진탐색 실전문제2 - 부품 찾기
계수정렬로 풀기
counting sort
각 숫자가 몇번 등장했는지 세어준다.
'''
n = int(input())
count = [0] * (1000001)

# 가게에 있는 부품을 입력받아서 개수 확인
for i in list(map(int, input().split())):
  count[i] += 1

m = int(input())
m_arr = list(map(int, input().split()))
for i in m_arr:
  if count[i] != 0: # 개수가 0이 아니면
    print("yes", end = " ")
  else:
    print("no", end = " ")
