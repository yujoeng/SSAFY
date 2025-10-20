# 1. 각 집합을 만들어주는 함수
def make_set(n):
    # 1 ~ n 까지의 원소가 "각자 자신이 대표자라고 설정"
    parents = [i for i in range(n + 1)]
    return parents

# 2. 집합의 대표자를 찾는 함수
def find_set(x):
    # 자신 == 부모 -> 해당 집합의 대표자
    if x == parents[x]
        return x


    # x의 부모노드를 기준으로 다시 부모를 검색
    find_set(parents[x])
    pass

def union(x, y):
    1. x, y의 대표자를 검색
    rep_x = find_set(x)
    rep_y = find_set(y)

    # 만약 이미 같은 집합
    if rep_x == rep_y :
        return # 같은 집합끼리는 합칠 필요가 없다

    # 더 작은쪽으로 연결하는 문제라면, 조건을 추가해준다.
    if rep_x < rep_y:
        parents[rep_y] = rep_x
    else:
        parents[rep_x] = rep_y



    parents[rep_y] = rep_x



N = 6
parents = make_set(N)

union(2, 4)
union(4, 6)
