N = int(input())

x_y_list = []

for i in range(N) :
    x, y = map(int, input().split())
    x_y_list.append([x, y])

x_y_list.sort(key=lambda point: (point[1], point[0]))

point = 0

cnt = 0

for x, y in x_y_list :
    if x >= point :
        point = y
        cnt += 1
print(cnt)


    
