def solution(n, w, num):
    answer = 1
    
    # 전체 n
    
    # 가로 w
    
    # 세로는? n % w == 0 이면 n // w, n % w > 0 면 n // w + 1
    
    # 2차원 배열로 구하자
    
    h = n // w
    if n % w > 0:
        h += 1
    
    two_demend = [[0] * w for i in range(h)]
    
    line = 1 # 첫째줄
    start = 1
    
    for i in range(h, -1, -1):
        print(i)
        if line % 2 == 1:
            # 왼쪽부터
            for j in range(0, w):
                two_demend[i - 1][j] = start
                start += 1
                if (start > n):
                    break
        else:
            # 오른쪽부터
            for j in range(w - 1, -1, -1):
                two_demend[i - 1][j] = start
                start += 1
                if (start > n):
                    break
        line += 1
        if line > h:
            break
    print(two_demend)
    
    for i in range(len(two_demend)):
        for j in range(len(two_demend[0])):
            if two_demend[i][j] == num:
                print(two_demend[i][j])
                if i == 0:
                    break
                for k in range(i - 1, -1, -1):
                    if two_demend[k][j] != 0:
                        print(two_demend[k][j])
                        answer += 1
    
    
    return answer