#빅 - 오 표기법 스터디
def solution(n):
    count = 0
    for i in range(n):        #n^2번 연산을 수행하는 2중 반복문
        for j in range(n):
            count += 1

    for k in range(n):        #n번 연산을 수행하는 반복문
        count += 1

    for i in range(2*n):      #2n번 연산을 수행하는 반복문
        count += 1

    for i in range(5):        #5번 연산을 수행하는 반복문
        count += 1

    print(count)

#solution 함수에서의 시간 복잡도는 n^2 + 3n + 5임! -> 고로, O(n^2)이다.
#함수 실행하는 부분
solution(6) 
"""
빅-오 표기법 : 함수의 상한을 표시하는 법
빅-세타 표기법 : 함수의 상한과 하한을 동시에 표시하는 법
빅-오메가 표기법 : 함수의 하한을 표시하는 법
"""
