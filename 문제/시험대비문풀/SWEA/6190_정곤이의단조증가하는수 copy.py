'''
[문제]
정곤이는 자신이 엄청난 수학자임을 증명하기 위해, 어떤 규칙 만족하는 수를 찾아보기로 했다.
그 규칙은 단조 증가하는 수인데, 각 숫자의 자릿수가 단순하게 증가하는 수를 말한다.
어떤 k자리 수 X = d1d2…dk 가 d1 ≤ d2 ≤ … ≤ dk 를 만족하면 단조 증가하는 수이다.
예를 들어 111566, 233359는 단조 증가하는 수이고, 12343, 999888은 단조 증가하는 수가 아니다.
양의 정수 N 개 A1, …, AN이 주어진다.
1 ≤ i < j ≤ N 인 두 i, j에 대해, Ai x Aj값이 단조 증가하는 수인 것들을 구하고 그 중의 최댓값을 출력하는 프로그램을 작성하라.

[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N(1 ≤N ≤ 1,000) 이 주어진다.
두 번째 줄에는 N개의 정수 A1, …, AN(1 ≤ Ai ≤ 30,000) 이 공백 하나로 구분되어 주어진다.

[출력]
각 테스트 케이스마다 단조 증가하는 수인 Ai x Aj중에서 그 최댓값을 출력한다.
만약 Ai x Aj중에서 단조 증가하는 수가 없다면 -1을 출력한다.


import sys
# 각 숫자의 자릿수가 d1 <= d2 <= ...<= dn 인지 확인 

def is_monotone(N:int)-> bool:
    s = str(N)   # 정수를 문자열로 바꿔 각 자릿수를 비교 
    for i in range(len(s)-1):  # 인접한 자리끼리 비교 
        if s[i] < s[i+1]:  # 앞자리가 뒷자리보다 크면 단조 증가 아님
            return False
        return True   # 끝까지 통과하면 단조증가 

input = sys.stdin.readline
T= int(input())    # 테스트케이스 수

for tc in range(1, T+1):
    N = int(input().strip()) # 수의 개수 
    A = list(map(int, input().split())) # 수열
    ans = -1 # 단조증가 곱이 없으면 -1 출력해야하므로 초기값 -1

    # 모든 쌍(i, j), i < j 확인 
    for i in range(N -1):
        for j in range(i+1, N):
            prod = A[i] * A[j]   # 두 수의 곱
            # 현재 최대값보다 크고, 단조 증가이면 갱신
            if prod > ans and is_monotone(prod):
                ans = prod

    print(ans)

'''

숫자의 각 자릿수가 d1 <= d2 <= ... <= dk 인지 확인
import sys
input = sys.stdin.readline # 더 빠른 입력 함수로 교체 

def is_monotone(n: int) -> bool:
    s = str(n)                      # 정수를 문자열로 바꿔 각 자릿수를 비교
    for i in range(len(s) - 1):     # 인접한 자리끼리 비교
        if s[i] > s[i + 1]:         # 앞자리가 뒷자리보다 크면 단조 증가 아님
            return False
    return True                     # 끝까지 통과하면 단조 증가

T = int(input())          # 테스트 케이스 수
for _ in range(T):
    N = int(input())        # 수의 개수
    arr = list(map(int, input().split()))  # 수열 A1..AN
    ans = -1                         # 단조 증가 곱이 없으면 -1 출력해야 하므로 초기값 -1

    # 모든 쌍 (i, j), i < j 확인
    for i in range(N):
        first_pick = arr[i]
        for j in range(i + 1, N):
            second_pick = arr[j]

            target = first_pick * second_pick

            if is_monotone(target) == True:
                if target > ans:
                    ans =target



    #         prod = A[i] * A[j]      # 두 수의 곱
    #         # 현재 최댓값보다 크고, 단조 증가이면 갱신
    #         if prod > ans and is_monotone(prod):
    #             ans = prod

    # print(ans)








T = int(input())          # 테스트 케이스 수
for _ in range(1, T+1):
    