'''
정수 N이 입력되면
00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중
3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램

십의자리는 0부터 5까지 가능
일의자리는 0부터 9까지 가능
가능한 모든 경우의 수를 모두 확인한다. → 완전탐색 유형
비효율적인 시간 복잡도로 데이터 개수가 100만개 이하일 때 사용하면 적절하다.

'''
n = int(input()) # 시
result = 0
for h in range(n+1):
  for m in range(60):
    for s in range(60):
      # 매 시각마다 '3'이 포함되어 있는지 확인
      if '3' in str(h) + str(m) + str(s): # '032035'
        result += 1
print(result)
