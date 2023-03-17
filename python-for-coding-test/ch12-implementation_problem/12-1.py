'''
알고리즘 유형별 기출문제-구현
8 럭키 스트레이트
link: https://www.acmicpc.net/problem/18406

문제 설명
게임 캐릭터의 필살기 럭키 스트레이트는 점수가 특정조건을 만족할 때 사용가능
특정조건: 현재 캐릭터의 점수 N → 자릿수를 기준으로 점수 N을 반으로 나누고 왼쪽 부분의 각 자릿수의 합과 오른쪽 부분의 각 자릿수의 합이 동일한 상황
N이 주어졌을 때 럭키 스트레이트를 사용할 수있는 상태인지 아닌지 판별

입력조건
점수 N(10<= N <= 99,999,999)
N의 자릿수는 항상 짝수 형태로만 주어짐

출력조건
럭키 스트레이트를 사용할 수 있으면 LUCKY, 없다면 READY 출력

문제풀이 아이디어
N을 입력받고 문자열로 보고 left와 right로 반반 나눈다
left의 합과 right의 합을 비교하여 결과를 출력
'''
n = str(input())
half = len(n)//2 # 절반길이
left = sum(map(int, n[:half]))
right = sum(map(int, n[half:]))

if left == right:
  print("LUCKY")
else:
  print("READY")
