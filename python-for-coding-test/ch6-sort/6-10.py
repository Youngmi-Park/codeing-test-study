'''
6장 정렬 실전문제2 - 위에서 아래로
난이도: 하, 풀이시간: 15분, 시간제한: 1초, 메모리제한: 128MB 기출: T 기업 코딩 테스트

문제설명
하나의 수열에는 다양한 수가 존재한다. 이러한 수는 크기에 상관없이 나열되어 있다.
이 수를 큰 수 부터 작은 수의 순서로 정렬해야한다. 수열을 내림차순으로 정렬하는 프로그램을 만드시오.

입력조건
첫째 줄에 수열에 속해 있는 수의 개수 N이 주어진다.(1<=N<=500)
둘째 줄부터 N+1번째 줄까지 N개의 수가 입력된다. 수의 범위는 1 이상 100,000 이하의 자연수이다.

출력조건
입력으로 주어진 수열이 내림차순으로 정렬된 결과를 공백으로 구분하여 출력한다. 동일한 수의 순서는 자유롭게 출력해도 괜찮다.

문제 풀이 아이디어
입력받은 숫자를 리스트에 저장하고 sort() 메소드로 정렬한다.
이때 내림차순 정렬이므로 reverse=True로 설정한다.
'''
n = int(input())
arr = [int(input()) for _ in range(n)] # 입력받은 숫자를 저장 n번 반복한다
arr.sort(reverse=True) # 내림차순 정렬
print(' '.join(map(str, arr)))
