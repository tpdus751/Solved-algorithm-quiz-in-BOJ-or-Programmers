def solution(bandage, health, attacks):
    answer = 0
    
    # 초기 카운트 초기화
    count = 1
    
    # 현재 공격 인덱스 초기화
    attack_cur = 0
    
    #초기 체력 변수 초기화
    first_health = health
    
    # 마지막 공격 시간 초기화
    last_attack_time = attacks[-1][0]
    
    # 연속 힐 횟수 초기화
    continuos_heal_time = 0
    
    # 최대 힐 시간 초기화
    max_heal_time = bandage[0]
    # 초당 힐량 초기화
    heal_amount = bandage[1]
    # 최대 힐 시간에 도달 했을 때 보너스 힐량 초기화
    if_heal_time_max_added_heal_amount = bandage[2]
    
    # 체력이 0이하가 되거나 현재 시간이 마지막 공격시간보다 높다면(모든 공격 직후) 끝내기
    while (health > 0) and (count <= last_attack_time) and (attack_cur <= len(attacks) - 1):
        
        # 다음 공격 시간
        next_attack_time = attacks[attack_cur][0]
        # 다음 공격량
        next_attack_demage = attacks[attack_cur][1]
        # 만약 현재 시간이 다음 공격 시간이라면
        if count == next_attack_time:
            # 체력에서 다음 공격력을 뺀다
            health -= next_attack_demage
            # 연속 힐 횟수 0으로 초기화
            continuos_heal_time = 0
            # 현재 공격 인덱스를 증가
            attack_cur += 1
        # 만약 현재 시간이 다음 공격 시간이 아니라면
        else:
            # 연속 힐 시간을 1 증가
            continuos_heal_time += 1
            # 체력에 초당 힐량 증가
            health += heal_amount
            # 만약 체력이 체력 초기값보다 높거나 같아진다면
            if health >= first_health:
                # 체력을 체력 초기값으로 초기화
                health = first_health
            # 만약 연속 힐 시간이 최대 힐 시간에 도달하면
            if continuos_heal_time == max_heal_time:
                # 체력에 보너스 힐량을 더한다
                health += if_heal_time_max_added_heal_amount
                # 만약 체력이 체력 초기값보다 높거나 같아진다면
                if health >= first_health:
                    # 체력을 체력 초기값으로 초기화
                    health = first_health
                # 연속 힐 시간이 최대 힐 시간에 도달했으니 연속 힐 시간을 0으로 초기화
                continuos_heal_time = 0
        # 다음 스텝을 위해 현재 시간 1 증가
        count += 1
        
        if health <= 0:
            return -1
        
    return health