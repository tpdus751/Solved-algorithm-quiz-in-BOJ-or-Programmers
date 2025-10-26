def solution(mats, park):
    answer = 0
    
    mats.sort(reverse=True)
    
    cur_mats_idx = 0
    
    is_all_ok = False
    
    for mat in mats:
        for i in range(len(park)):
            for j in range(len(park[i])):
                if park[i][j] == "-1":
                     if i + mat <= (len(park)) and j + mat <= (len(park[i])):
                        is_ok = True
                        for row in range(i, i + mat):
                            for col in range(j, j + mat):
                                if park[row][col] != "-1":
                                    is_ok = False
                                    break
                            if is_ok == False:
                                break
                        if is_ok == True:
                            is_all_ok = True
                            return mat
    return -1
   