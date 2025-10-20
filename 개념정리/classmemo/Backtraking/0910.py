## 병합정렬 
# -------------------
# 1. 분할 : 리스트의 길이가 1일 때까지 분할
# 2. 정복(정렬) : 리스트의 길이가 1이 되면 자동으로 정렬됨
# 3. 병합
#     - 왼쪽, 오른쪽 리스트 중
#         작은 원소부터 정답 리스트에 추가하면서 진행

def merge(left, right):
    # 두 리스트를 병합한 결과 리스트
    result = [0] *(len(left) + len(right))
    l = r = 0 # 인덱스

    # 두 리스트에서  비교할 대상이 남아있을 때 까지 반복
    while l < len(left) and r < len(right)
        if left[l] < right[r]:
            result[l + r] = left[l]   #-> 뭣을 위한 과정인지 코드 설명 듣기
            l += 1
        else:
            result[l + r] = right[r]
            r += 1

    # 왼쪽 리스트에 남은 데이터들을 모두 result 에 추가
    while l < len(left):
        result[l + r] = left[l]
        l += 1
    # 오른쪽 리스트에 남은 데이터들을 모두 result에 추가
    while r < len(right):
        result[l + r] = right[r]
        r += 1

    return result

def merge_sort(li):
    if len(li) == 1:
        return li
    
    # 절반씩 분할하여 출력해라
    mid = len(li) // 2
    left = li[:mid]     # 리스트의 앞쪽 절반
    right = li[mid:]    # 리스트의 뒤쪽 절반

    left_list = merge_sort(left)
    right_list = merge_sort(right)
    # print(left_list,right_list)
    # 분할이 완료되면

    # 2. 병합
    # 병합하면서 해야할 일 : 작은 값을 먼저 넣고 그 다음 큰 값을 입력
    # 그 과정이 merge 함수에 입력됨
    merge_list = merge(left_list, right_list)
    return merge_list

    

arr = [69, 10, 30, 2, 16, 8, 31, 22]
sorted_arr = merge_sort(arr)
print(sorted_arr)

# --------------------------------------
#  [ Hoare ]

arr = [3, 2, 4, 6, 9, 1, 8, 7, 5]
# arr = [11, 45, 23, 81, 28, 34]
# arr = [11, 45, 22, 81, 23, 34, 99, 22, 17, 8]
# arr = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

# 피벗 : 제일 왼쪽 요소
# 이미 정렬된 배열이나 역순으로 정렬된 배열에서 최악의 성능을 보일 수 있음
def hoare_partition1(left, right):
    pivot = arr[left] # 피벗을 제일 왼쪽 요소로 설정
    i = left + 1
    j = right

    while i <= j: # 교차가 되면 끝
        while i <= j and arr[i] <= pivot: # i는 pivot 보다 큰 값을 검색 (작거나 같으면 i += 1)
            i += 1
        while i <= j and arr[j] >= pivot # j 는 pivot 보다 작은 값을 검색 ( 크거나 같으면 j -= 1)
            j -= 1

        if i < j: # swap
            arr [i], arr[j] = arr[j], arr[i]

    # pivot 과 j 위치를 swap
    arr[left], arr[j] = arr[i], arr[left]
    return j


# 피벗 : 제일 오른쪽 요소
# 이미 정렬된 배열이나 역순으로 정렬된 배열에서 최악의 성능을 보일 수 있음
def hoare_partition2(left, right):
    pivot = arr[right] # 피벗을 제일 오른쪽 요소로 설정
    i = left
    j = right -1

    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and >= arr[j] >= pivot:
            j -= 1
        if i < j :
            arr[i], arr[j] = arr[j], arr[i]

    arr[i], arr[right] = arr[right], arr[i]
    return i

# 피벗 : 중간 요소로 설정
# 일반적으로 더 균형 잡힌 분할이 가능하며, 퀵 정렬의 성능을 최적화할 수 있습니다.
def hoare_partition3(left, right):
    mid = (left + right) // 2
    pivot = arr[mid] # 피벗을 중간 요소로 설정
    arr[left], arr[mid] = arr[mid], arr[left] # 중간 요소를 왼쪽으로 이동(필요 시)
    i = left + 1
    j = right

    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[left], arr[j] = arr[j], arr[left]
    return j

def quick_sort(left, right):
    if left < right:
        pivot = hoare_partition1(left, right)
        pivot = hoare_partition2(left, right)
        pivot = hoare_partition3(left, right)
        quick_sort(left, pivot - 1)
        quick_sort(pivot + 1, right)

quick_sort(0, len(arr) - 1)
print(arr)





# ----------------------------
# 이진 검색 라이브 중 구현해본 코드

def binary_search_while(target):
    left = 0                # 검색 시작점
    right = len(arr) -1     # 검색 끝점
    cnt = 0             # 몇 번만에 찾았는 가?

    while left <= right # 교차되면 못 찾은 것
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid # mid 위치에 존재한다고 return
        
        # target 보다 정답이 왼쪽에 있는 경우
        if target < arr[mid]:
            right = mid - 1
        # target 보다 정답이 오른쪽에 있는 경우 
        else:
            left = mid + 1


    # 못찾은 경우
    return -1, cnt


#--------[참고] 이진 검색 재귀 호출
def

arr = [4, 2, 9, 7, 11, 23, 19]

# 이진 검색은 항상 정렬된 데이터에 적용 
arr.sort()   # 2 4 7 9 11 19 23

print(f'9 ={binary_search_while(9)}번째에 위치')