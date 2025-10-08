import heapq

def solution(scoville, K):
#     answer = 0
    
#     # 최소 힙으로 구성
    
#     # 가장 낮은 스코빌을 뽑는다
    
#     # 두번째로 낮은 스코빌을 뽑는다
    
#     # 가장 낮은 스코빌 + (두번쨰로 낮은 스코빌 * 2) 하여 다시 스코빌 리스트에 넣는다
    
#     # 전체가 K 이상이 될 때까지 반복한다
    
#     appended_list = []
    
#     scoville.sort()
    
#     scoville = [None] + scoville
        
#     # --- 초기 세팅 ---
    
#     # 스코빌 리스트의 1번째가 K 미만일 때 까지 반복 (정렬되있으니 가장 처음 인덱스만 보면 됨)
#     while scoville[1] < K:
        
#         min_scoville_list = []
        
#         # 2번 반복 (1번은 스코빌 리스트에서 가장 낮은 스코빌, -> 정렬 -> 2번은 스코빌에서 2번째로 낮은 스코빌 뽑음 -> 정렬)
#         for _ in range(2):

#             cur_index = 1
            
#             scoville[cur_index], scoville[-1] = scoville[-1], scoville[cur_index]

#             min_scoville = scoville.pop() # 1이 뽑힘
            
#             min_scoville_list.append(min_scoville) # [1, ]
            
#             if len(min_scoville_list) < 2 and len(scoville) == 1:
#                 return -1
            
#             #print("min_scoville_list", min_scoville_list)

#             # 정렬 
#             while cur_index <= len(scoville) - 1:
#                 min_index = cur_index
#                 left_index = cur_index * 2
#                 right_index = cur_index * 2 + 1
                
#                 if left_index <= len(scoville) - 1 and scoville[min_index] > scoville[left_index]: # 12 < 2
#                     min_index = left_index
#                 if right_index <= len(scoville) - 1 and scoville[min_index] > scoville[right_index]:
#                     min_index = right_index

#                 if min_index == cur_index:
#                     break

#                 scoville[cur_index], scoville[min_index] = scoville[min_index], scoville[cur_index]
                
#                 cur_index = min_index # cur_index = 2
                
#             #print("정렬된 scoville", scoville)
        
#         scoville.append(min_scoville_list[0] + (min_scoville_list[1] * 2))
        
#         if len(scoville) <= 2 and scoville[1] < K:
#             return -1
        
#         #print("추가된 섞은 scoville", scoville)
        
#         cur_index = len(scoville) - 1
        
#         while cur_index > 1:
#             if scoville[cur_index] < scoville[cur_index // 2]:
#                 scoville[cur_index], scoville[cur_index // 2] = scoville[cur_index // 2], scoville[cur_index]
#                 cur_index = cur_index // 2
#             else:
#                 break
                
#         #print("추가되어 정렬된 scoville", scoville)
        
#         answer += 1
    
    heapq.heapify(scoville)          # O(n)
    answer = 0

    while len(scoville) >= 2 and scoville[0] < K:
        a = heapq.heappop(scoville)  # O(log n)
        b = heapq.heappop(scoville)  # O(log n)
        heapq.heappush(scoville, a + 2*b)
        answer += 1

    return answer if scoville and scoville[0] >= K else -1

