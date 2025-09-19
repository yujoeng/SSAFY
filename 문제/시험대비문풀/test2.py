
# T = int(input())

# for test_case in range(1, T+1) :
#     K, N, M = list(map(int, input().split()))
#     arr = [0] + list(map(int, input().split()))+ [N]

#     last = 0 # 최근 충전 위치

#     count = 0 # 충전 횟수

#     for idx in range(1, M+2) :

#         # 2번째 값과 1번째 값의 차가 K보다 크면 break

#         if (arr[idx] - arr[idx-1]) > K :
#             count = 0
#             break

#         # 2번째 값과 마지막 충전소 위치의 차가 K보다 크면 count

#         if arr[idx] - last > K :
# #             count += 1
# #             last = arr[idx-1]

# #     print(f'#{test_case} {count}')


# T = int(input())

# for test_case in range(1, T+1) :

#     K, N, M = list(map(int, input().split()))
#     arr = [0] + list(map(int, input().split())) + [N]

#     last = 0

#     cnt = 0

#     for idx in range(1, M+2):
#         if (arr[idx] - arr[idx-1]) > K :
#             cnt = 0 
#             break
        
#         if arr[idx] - last > K : 
#             cnt += 1
#             last = arr[idx-1]

#     print(f'#{test_case} {cnt}')



T = int(input())
for tc in range(1, T+1):
    K, N, M = list(map(int, input().split())) # 입력값
    arr = [0] + list(map(int, input().split())) + [N]

    last = 0 
    cnt = 0 

    for idx in range(1, M+2):
        if (arr[idx] - arr[idx-1]) > K :
            cnt = 0
            break
        if arr[idx] - last > K :
            cnt += 1
            last = arr[idx-1]
    print(f'#{tc} {cnt}')

