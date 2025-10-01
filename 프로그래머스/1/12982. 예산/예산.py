def solution(d, budget):
    answer = 0
    
    sum = 0
    
    for i in range(len(d)):
        d_min = min(d)
        d.remove(d_min)
        sum += d_min
        if sum > budget:
            return answer
        answer += 1
    
    return answer