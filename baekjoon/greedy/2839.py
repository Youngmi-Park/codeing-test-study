# 2839번 설탕 배달
# https://yommi11.tistory.com/106
N = int(input())
total = 0
 
while N >= 0:
    if N % 5 == 0:
        total += int(N // 5)
        print(total)
        break
    N -= 3
    total += 1
else:
    print(-1)

n = int(input())
result = 0
five = n // 5 # 최대로 가져갈 수 있는 5킬로그램 봉지 수
for i in range(five,-1, -1):
    if (n - i * 5) % 3 == 0:
        result += i
        result += (n - i * 5) // 3
        break
else:
    result = -1
print(result)
