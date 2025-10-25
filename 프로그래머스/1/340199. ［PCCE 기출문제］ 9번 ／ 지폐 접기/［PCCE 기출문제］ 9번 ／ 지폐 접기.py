
    

def solution(wallet, bill):
    answer = 0
    
    bill_small = min(bill[0], bill[1])
    bill_big = max(bill[0], bill[1])
    wallet_small = min(wallet[0], wallet[1])
    wallet_big = max(wallet[0], wallet[1])
        
    print("bill_small :", bill_small, "bill_big", bill_big)
    print("wallet_small :", wallet_small, "wallet_big", wallet_big)
    
    while bill_small > wallet_small or bill_big > wallet_big:
        bill_small = min(bill_small, bill_big)
        bill_big = max(bill_small, bill_big)
        
        bill_big = bill_big // 2
        
        if bill_big < bill_small:
            bill_small, bill_big = bill_big, bill_small
        
        answer += 1
        
        print("bill_small :", bill_small, "bill_big", bill_big)
    return answer
    
    # 함수 : 지갑 사이즈보다 지폐 사이즈가 큰 지, 작은 지 확인(True면 큼, False면 작음)
    
    # True일 경우 : 큰 값을 반으로 나눔
    
    # False일 경우 : 그냥 횟수 반환
    
