'''
알고리즘 유형별 기출문제-그리디
3 문자열 뒤집기

문제 설명
0과 1로만 이루어진 문자열 S
S의 모든 숫자를 전부 같게 만들고자 한다.
S에서 연속된 하나 이상의 숫자를 모두 뒤집을 수 있다. 1→0, 0→1
문자열 S가 주어졌을 때 행동의 최소 횟수

입력
0과 1로만 이루어진 문자열 S가 주어진다. 길이는 100만 이하

출력
다솜이가 해야 하는 행도의 최소 횟수

문제풀이 아이디어
순차탐색을 통해 0과 1 덩어리 개수를 카운트한다.
현재 숫자를 갱신해주면서 직전과 달라지는지 확인한다.
0과 1 중 적은 것을 뒤집으면 된다.
'''
s = str(input()) # 원소를 하나씩 보기위해서 문자열로 입력받음
zero, one = 0, 0 # 0과 1의 덩어리를 개수 저장
before = s[0] # 현재 문자열은 첫번째 숫자

for i in s:
  if i == '0' and before != '0': # 이전 문자와 달라지는 경우 +1
    zero += 1
  elif i == '1' and before != '1': #  이전 문자와 달라지는 경우 +1
    one += 1
  before = i # 이전문자 갱신
  
print(min(zero, one)) # 둘 중 작은 것 출력
