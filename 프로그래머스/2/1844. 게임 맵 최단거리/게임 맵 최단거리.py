from collections import deque

def solution(maps):
    
    n = len(maps)
    m = len(maps[0])
    
    # 상하좌우
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque()
    queue.append((0, 0, 1))
    
    # 방문 초기화
    
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    
    while queue:
        x, y, dist = queue.popleft()
        
        # 도착 지점 도달 시
        if x == n - 1 and y == m - 1:
            return dist
        
        # 4방향 탐색
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            # 유효 범위 and 벽아님 and 미방문
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))
    
    return -1