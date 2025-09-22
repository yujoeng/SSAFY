'''
숫자 차례로 출력하기 
[문제]

정수 n이 주어지면 재귀함수 2개 작성하여 첫 번째 재귀함수를 이용하여 1부터 n까지 숫자를 차례대로 출력하고, 
두 번째 재귀함수를 이용하여 n부터 1까지 차례로 출력하는 프로그램을 작성해보세요. 단 두 재귀함수 모두 인자로 n을 넘기는 함수여야만 합니다.

'''
n = int(input())

def print_number(n): # 재귀 함수 
    if n == 0 : # 재귀함수 종료 조건
        return # 반환 

    print_number(n -1) # n - 1의 값을 반복하기 위함
    print(n, end=" ") # 1 2 3 4 5 6 7

def print_number1(n):
    if n == 0 :
        return
    
    print(n, end=" ")
    print_number1(n - 1)

print_number(n)
print( )
print_number1(n)


# 재귀함수 print_number 이랑 print 사용 기준을 정확하게 구분하기 
# 출력하는건 print를 사용하고 조건은 무조건 재귀함수 변수 이름 적기 