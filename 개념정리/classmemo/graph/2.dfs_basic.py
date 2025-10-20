import sys
sys.stdin = open(input.txt, "r")



def dfs(node):
    print(node, end="")

    # 다음 재귀 호출
    # node 로 부터 갈 수 있는 노드들을 모두 확인
    --> 그 중에서 한 곳으로 진행
    for next_node in graph[node]:
        # 이미 방문한 지점은 가지마라!
        if visited[next_node]:
            continue

        visited[next_node] = 1 # 방문처리


