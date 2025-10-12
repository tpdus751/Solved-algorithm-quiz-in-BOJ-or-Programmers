def solution(schedules, timelogs, startday):
    answer = 0
    
    day = ["월", "화", "수", "목", "금", "토", "일"] # 만약 startday가 5라면 금요일 5번째 인덱스
    
    count = len(schedules) # 총 인원 초기화
    
    start_day = startday
    
    for person_idx in range(len(schedules)):
        startday = start_day
        limit_time = schedules[person_idx] + 10
        if limit_time % 100 >= 60:
            limit_time += 40
        for yoil_idx in range(7):
            startday = start_day + yoil_idx
            current_day = startday
            if current_day >= 8:
                current_day = current_day - 7
            if 6 <= current_day <= 7:
                # 주말
                if timelogs[person_idx][yoil_idx] > limit_time:
                    continue
            else:
                # 평일
                if timelogs[person_idx][yoil_idx] > limit_time:
                    count -= 1
                    break
            
    
    
    return count