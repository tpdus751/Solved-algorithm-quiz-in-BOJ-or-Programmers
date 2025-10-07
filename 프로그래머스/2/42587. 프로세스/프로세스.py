def solution(priorities, location):
    answer = 0
    
    priorities_order_by_desc = priorities.copy()
    priorities_order_by_desc.sort(reverse=True)
    
    print(priorities)
    print(priorities_order_by_desc)
    
    cur_max_idx = 0
    cur_execute_rank = 1
    
    result = [0] * len(priorities)
    
    start_idx = 0
    
    while True:
        if priorities[start_idx] == priorities_order_by_desc[cur_max_idx]:
            result[start_idx] = cur_execute_rank
            if start_idx == location:
                break
            cur_max_idx += 1
            cur_execute_rank += 1
        start_idx += 1
        if (start_idx >= len(priorities)):
            start_idx = 0
        
    print(result)    
    
    return result[location]