'''
피보나치 수열 단순 재귀 소스코드
'''
def fibo(x):
  if x == 1 or x == 2: # 종료조건 a1=1, a2=1
    return 1
  return fibo(x - 2) + fibo(x - 1)

print(fibo(4))
