'''
피보나치 수열 탑다운 방식 - 재귀함수, 메모이제이션
'''
# 한 번 계산된 결과를 메모이제이션하기 위한 리스트 초기화
d = [0] * 100

def fibo(x):
  if x == 1 or x == 2: # 종료조건
    return 1
  if d[x] != 0: # 이미 계산한 적 있는 문제라면 그대로 반환
    return d[x]
  d[x] = fibo(x - 2) + fibo(x - 1)
  return d[x]

print(fibo(99))
