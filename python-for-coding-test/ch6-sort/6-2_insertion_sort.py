# 삽입 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1,len(array)): # 두번째 원소부터 시작
    for j in range(i,0,-1): # 선택한 원소부터 1까지 1씩 감소하면서 반복, 세 번째는 step
        print(i, j, array)
        if array[j] < array[j -1]: # j는 현재 삽입하고자하는 원소, 왼쪽에 있는 데이터와 비교했을 때 자기가 더 작으면 swap
            array[j], array[j-1] = array[j-1], array[j]
            print("swap:", array,"j:",j,"j-1:",j-1)
        else:# 현재 삽입하고자 하는 원소가 왼쪽에 있는 데이터보다 크거나 같다면 그 자리에서 멈추면 된다.
            print("break. 왼쪽 원소가 더 작습니다.")
            break # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤

print("\nresult",array)

'''
1 1 [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
swap: [5, 7, 9, 0, 3, 1, 6, 2, 4, 8] j: 1 j-1: 0
2 2 [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
break. 왼쪽 원소가 더 작습니다.
3 3 [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
swap: [5, 7, 0, 9, 3, 1, 6, 2, 4, 8] j: 3 j-1: 2
3 2 [5, 7, 0, 9, 3, 1, 6, 2, 4, 8]
swap: [5, 0, 7, 9, 3, 1, 6, 2, 4, 8] j: 2 j-1: 1
3 1 [5, 0, 7, 9, 3, 1, 6, 2, 4, 8]
swap: [0, 5, 7, 9, 3, 1, 6, 2, 4, 8] j: 1 j-1: 0
4 4 [0, 5, 7, 9, 3, 1, 6, 2, 4, 8]
swap: [0, 5, 7, 3, 9, 1, 6, 2, 4, 8] j: 4 j-1: 3
4 3 [0, 5, 7, 3, 9, 1, 6, 2, 4, 8]
swap: [0, 5, 3, 7, 9, 1, 6, 2, 4, 8] j: 3 j-1: 2
4 2 [0, 5, 3, 7, 9, 1, 6, 2, 4, 8]
swap: [0, 3, 5, 7, 9, 1, 6, 2, 4, 8] j: 2 j-1: 1
4 1 [0, 3, 5, 7, 9, 1, 6, 2, 4, 8]
break. 왼쪽 원소가 더 작습니다.
5 5 [0, 3, 5, 7, 9, 1, 6, 2, 4, 8]
swap: [0, 3, 5, 7, 1, 9, 6, 2, 4, 8] j: 5 j-1: 4
5 4 [0, 3, 5, 7, 1, 9, 6, 2, 4, 8]
swap: [0, 3, 5, 1, 7, 9, 6, 2, 4, 8] j: 4 j-1: 3
5 3 [0, 3, 5, 1, 7, 9, 6, 2, 4, 8]
swap: [0, 3, 1, 5, 7, 9, 6, 2, 4, 8] j: 3 j-1: 2
5 2 [0, 3, 1, 5, 7, 9, 6, 2, 4, 8]
swap: [0, 1, 3, 5, 7, 9, 6, 2, 4, 8] j: 2 j-1: 1
5 1 [0, 1, 3, 5, 7, 9, 6, 2, 4, 8]
break. 왼쪽 원소가 더 작습니다.
6 6 [0, 1, 3, 5, 7, 9, 6, 2, 4, 8]
swap: [0, 1, 3, 5, 7, 6, 9, 2, 4, 8] j: 6 j-1: 5
6 5 [0, 1, 3, 5, 7, 6, 9, 2, 4, 8]
swap: [0, 1, 3, 5, 6, 7, 9, 2, 4, 8] j: 5 j-1: 4
6 4 [0, 1, 3, 5, 6, 7, 9, 2, 4, 8]
break. 왼쪽 원소가 더 작습니다.
7 7 [0, 1, 3, 5, 6, 7, 9, 2, 4, 8]
swap: [0, 1, 3, 5, 6, 7, 2, 9, 4, 8] j: 7 j-1: 6
7 6 [0, 1, 3, 5, 6, 7, 2, 9, 4, 8]
swap: [0, 1, 3, 5, 6, 2, 7, 9, 4, 8] j: 6 j-1: 5
7 5 [0, 1, 3, 5, 6, 2, 7, 9, 4, 8]
swap: [0, 1, 3, 5, 2, 6, 7, 9, 4, 8] j: 5 j-1: 4
7 4 [0, 1, 3, 5, 2, 6, 7, 9, 4, 8]
swap: [0, 1, 3, 2, 5, 6, 7, 9, 4, 8] j: 4 j-1: 3
7 3 [0, 1, 3, 2, 5, 6, 7, 9, 4, 8]
swap: [0, 1, 2, 3, 5, 6, 7, 9, 4, 8] j: 3 j-1: 2
7 2 [0, 1, 2, 3, 5, 6, 7, 9, 4, 8]
break. 왼쪽 원소가 더 작습니다.
8 8 [0, 1, 2, 3, 5, 6, 7, 9, 4, 8]
swap: [0, 1, 2, 3, 5, 6, 7, 4, 9, 8] j: 8 j-1: 7
8 7 [0, 1, 2, 3, 5, 6, 7, 4, 9, 8]
swap: [0, 1, 2, 3, 5, 6, 4, 7, 9, 8] j: 7 j-1: 6
8 6 [0, 1, 2, 3, 5, 6, 4, 7, 9, 8]
swap: [0, 1, 2, 3, 5, 4, 6, 7, 9, 8] j: 6 j-1: 5
8 5 [0, 1, 2, 3, 5, 4, 6, 7, 9, 8]
swap: [0, 1, 2, 3, 4, 5, 6, 7, 9, 8] j: 5 j-1: 4
8 4 [0, 1, 2, 3, 4, 5, 6, 7, 9, 8]
break. 왼쪽 원소가 더 작습니다.
9 9 [0, 1, 2, 3, 4, 5, 6, 7, 9, 8]
swap: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] j: 9 j-1: 8
9 8 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
break. 왼쪽 원소가 더 작습니다.
result [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
'''
