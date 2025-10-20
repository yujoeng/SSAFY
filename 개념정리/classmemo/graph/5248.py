def union(x, y):  #y의 대표원서를 x의 대표원소로 대체
    p[find_set(y)] = find_set(x)

def find_set(x):    # x가 속한 집합의 대표원소 리턴ㅍ어ㅏ.........ㄹ ㅡㅠㅎ퍼ㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓ4
    while p[x] != x:
            x = p[x]
    return x

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # 1번부터 N번까지의 출석번호가 있고, M 장의 신청서가 있을 때

    arr = list(map(int, input().split()))
    # 상호배타집합
    p = [i for i in range(N+1)]  # 대표원소 (1~N)

    for i in range(M):
        a, b = arr[i*2], arr[i*2+1]
        union(a, b)



    # 전체 몇 개의 조가 만들어지는지 출력
    ans = 0
    for i in range(1, N+1):
        if p[i] == i: #대표원소면
