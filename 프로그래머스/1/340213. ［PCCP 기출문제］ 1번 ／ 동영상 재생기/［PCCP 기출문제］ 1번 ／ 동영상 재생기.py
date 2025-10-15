def time_cal_next(second, minute, how):
    second += how
    if second >= 60:
        second = second - 60
        minute += 1
    return second, minute

def time_cal_prev(second, minute, how):
    second -= how
    if second < 0:
        second = 60 + second
        minute -= 1
    return second, minute

def str_one(str):
    if len(str) == 1:
        str = "0" + str
    return str

def is_opening_time(op_start_minute, op_start_second, pos_minute, pos_second, op_end_minute, op_end_second):
    op_start_full = int(str_one(str(op_start_minute)) + str_one(str(op_start_second)))
    pos_full = int(str_one(str(pos_minute)) + str_one(str(pos_second)))
    op_end_full = int(str_one(str(op_end_minute)) + str_one(str(op_end_second)))
    if op_start_full <= pos_full <= op_end_full:
        return True
    return False


def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    
    video_len_minute, video_len_second = map(int, video_len.split(":"))
    
    pos_minute, pos_second = map(int, pos.split(":"))
    
    op_start_minute, op_start_second = map(int, op_start.split(":"))
    
    op_end_minute, op_end_second = map(int, op_end.split(":"))
    
    for command in commands:
        if is_opening_time(op_start_minute, op_start_second, pos_minute, pos_second, op_end_minute, op_end_second):
            pos_minute, pos_second = op_end_minute, op_end_second
        
        if command == "next":
            pos_second, pos_minute = time_cal_next(pos_second, pos_minute, 10)
            if int((str_one(str(pos_minute)) + str_one(str(pos_second)))) >= int((str_one(str(video_len_minute)) + str_one(str(video_len_second)))):
                pos_minute, pos_second = video_len_minute, video_len_second
            if is_opening_time(op_start_minute, op_start_second, pos_minute, pos_second, op_end_minute, op_end_second):
                    pos_minute, pos_second = op_end_minute, op_end_second
        else:
            if pos_minute == 0 and pos_second <= 10:
                pos_second = 0
            else:
                pos_second, pos_minute = time_cal_prev(pos_second, pos_minute, 10)
                if is_opening_time(op_start_minute, op_start_second, pos_minute, pos_second, op_end_minute, op_end_second):
                    pos_minute, pos_second = op_end_minute, op_end_second
                
    pos_minute_str = ""
    pos_second_str = ""
    if len(str(pos_minute)) == 1:
        pos_minute_str = "0" + str(pos_minute)
    else:
        pos_minute_str = str(pos_minute)
    if len(str(pos_second)) == 1:
        pos_second_str = "0" + str(pos_second)
    else:
        pos_second_str = str(pos_second)
    
    return pos_minute_str + ":" + pos_second_str