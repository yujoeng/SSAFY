# 현재 자리에서 이전 곳의 가로, 세로, 대각선을 고려
def check(row, col) :
    # 1. 같은 열에 놓은 적이 있는가?
    for i in range(row) :
        if visited[i][col] :
            return False


    i -= 1
    j -= 1

    # 2. 좌상단 대각선에 놓은 적이 있는가? (\)
    i, j = row -1, col -1
    while i >= 0 and j >= 0:
        if visited[i][j]:
            return False


    # # [참고] for문으로 하고 싶다!
    # for i, in zip(range(row -1, -1, -1), range(col-1, -1, -1)) :
    #     if visited[i][j] :
    #         return False

    # 3. 우상단 대각선에 놓은 적이 있는가? (/)
    i, j = row -1, col +1
    while i >= 0 and j < N:
        if visited [i][j]
            return  False
        i -= 1
        j += 1

# 가지의 수: N개의 열

def recur(row) :
    global answer

    # 종료 조건: N개의 행을 모두 고려하면 종료
    if row == N :
        return

    for col in range(N):
        # 가지치기1: 같은 열을 못 고르도록
        # 가지치기2: 유망하지 않은 케이스를 모두 삭제(세로, 대각선)
        if check(row, col) is False : continue

        # col을 선택했다.
        visited[row][col]  = 1
        recur(row + 1)
        visited[row][col] = 0

N = 4
answer = 0  # 가능한 정답 수
visited = [[0] * N for _ in range(N)]
recur(0)
print(f'N= {N}/answer = {answer}')

N = 8
answer = 0  # 가능한 정답 수
visited = [[0] * N for _ in range(N)]
recur(0)
print(f'N= {N}/answer = {answer}')
