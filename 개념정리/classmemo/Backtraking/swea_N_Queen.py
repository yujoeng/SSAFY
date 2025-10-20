def f(i, N):
    global cnt
    if i == N:
        cnt += 1
    else:
        for j in range(N):
            if col[j] == 0 and dia1[i + j] == 0 and dia2[i + N - 1 - j] == 0:
                col[j] = 1
                dia1[i + j] = 1
                dia2[i + N - 1 - j] = 1
                f(i + 1, N)
                col[j] = 0
                dia1[i + j] = 0
                dia2[i + N - 1 - j] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    board = [[0] * N for _ in range(N)]
    cnt = 0
    col = [0] * N
    dia1 = [0] * (N * 2 - 1)
    dia2 = [0] * (N * 2 - 1)
    f(0, N)
    print(f'#{tc} {cnt}')*