# 계수 정렬 소스코드
# 모든 원소의 값이 0보다 크거나 같은 정수라고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

# 모든 범위를 포함하는 리스트 선언
count = [0] * (k+1) # 가장 큰 수 k+1만큼, 모든 항목은 0개로 초기화

# 숫자 개수 세기
for i in array:
  count[i] += 1 # 각 데이터에 해당하는 count 리스트의 index의 값을 +1을 해준다.

# 정렬된 결과 출력
for i in range(len(count)):
    print((str(i)+' ') * count[i], end='')
