import sys
sys.stdin = open("input.txt", "r")

def bfs(star_node):
    # q의 의미 :
    q = [star_node] # 시작점을 queue에 넣고 시작

V, E = map(int, input().split())

    