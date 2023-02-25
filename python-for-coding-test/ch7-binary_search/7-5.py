'''
7장 이진탐색 실전문제2 - 부품 찾기
난이도: 중하, 풀이시간: 30분, 시간제한: 1초, 메모리제한: 128MB

문제설명
전자매장 부품 N개
부품의 정수 형태 고유 번호
손님이 M개 종류 부품을 대략 구매
가게 안에 부품이 모두 있는지 확인하는 프로그램 작성

입력조건
첫째 줄에 N이 주어진다.(1<=N<=1,000,000), 가게 부품 개수
둘째 줄에 공백으로 구분하여 1이상 1,000,000이하의 N개 정수가 주어짐, 부품 고유번호
셋째 줄에 정수 M이 주어진다.(1<=M<=1,000,000), 손님이 주문한 부품 개수
넷째 줄에 공백으로 구분하여 1이상 1,000,000이하의 M개 정수가 주어짐, 부품 고유번호

출력조건
첫째 줄에 공백으로 구분하여 각 부품이 존재하면 yes를 없으면 no를 출력한다.

문제 풀이 아이디어
이진탐색을 통해 빠르게 물건을 찾으면 된다.
for문으로 m개의 부품의 유무를 체크
none이라면 no를 출력
전부 확인했을 때 있으면 yes를 출력
'''
def binary_search(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    if array[mid] == target: # 찾은 경우 yes
      return "yes"
    elif array[mid] < target: # 중간점 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
      start = mid + 1
    else: # 중간점 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
      end = mid - 1
  return "no"

n = int(input())
n_arr = list(map(int, input().split()))
m = int(input())
m_arr = list(map(int, input().split()))

for i in m_arr:
  print(binary_search(n_arr, i, 0, n-1), end = " ")
