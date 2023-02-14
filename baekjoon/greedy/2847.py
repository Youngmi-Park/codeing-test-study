# 게임을 만든 동준
# https://yommi11.tistory.com/31
n = int(input())
score = []
for i in range(n):
    score.append(int(input()))
 
count = 0
for i in reversed(range(n-1)):
    if score[i+1] <= score[i]:
        minus = score[i] - score[i+1] + 1
        score[i] = score[i] - minus
        count += minus
 
print(count)


n = int(input())
nums = [int(input()) for _ in range(n)]
result = 0
 
for i in range(n-1, 0, -1):
  if nums[i] <= nums[i-1]:
    result += nums[i-1] - nums[i] + 1
    nums[i-1] = nums[i] - 1
print(result)
