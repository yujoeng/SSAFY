import sys
sys.stdin = open("input.txt", "r")

        import heapq

# 특정 정점 기준으로 시작
#         --> 작은 노드를 먼저 꺼내기 위해 우선순위큐(heapq)를 활용한다.

def prim(start_node):
    pq = [0, (start_node)] # (가중치, 노드) 형태
    MST = [0] * V #vistied 와 동일하다
    min_weight = 0  # 최소 비용

    while pq:
        weight,node = heappop # - 갈 수 있는 노드들 중 가치가 가장 작은 노트부터 간다.

        # 이미 방문한 노드라면 continue
        if MST[node]:
            continue
        MST[node] = 1 # node 로 가는 최소 비용이 선택되었다
        min_weight += weight

        for next_node in range(V):

V, E = map(int, input().split())
graph = [0 * V for _ in range(V)] # 인접행렬
            # [선택 과제] 인접 리스트로 구현

for _ in range(E):
    start, end, weight = map(int, input().split())
    graph[start][end] = weight
    graph[end][start] = weight # 양방향



result = prim() # 출발 정점과 함계 시작
                    추
print(f'최소 비용 = ')