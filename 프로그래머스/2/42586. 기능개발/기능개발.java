import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        
        ArrayList<Integer> dayList = new ArrayList<>();
        
        for (int i = 0; i < progresses.length; i++) {
            int currentProgress = progresses[i];
            int speed = speeds[i];
            
            int completeDay = 0;
            if (((100 - currentProgress) % speed) != 0) {
                completeDay = (100 - currentProgress) / speed + 1;
            } else {
                completeDay = (100 - currentProgress) / speed;
            }
            
            dayList.add(completeDay);        
            
        }
        
        int start = 0;
            
        ArrayList<Integer> answerList = new ArrayList<>();
            
        int cnt = 0;
        
        int baseDay = dayList.get(0);
            
        while(start <= dayList.size() - 1) {
            if (dayList.get(start) <= baseDay) {
                cnt++;
            } else {
                answerList.add(cnt);
                baseDay = dayList.get(start);
                cnt = 1;
            }
            start += 1;
        }
        
        answerList.add(cnt);
        
        int[] answer = new int[answerList.size()];
        
        int startNum = 0;
        
        for (Integer num : answerList) {
            answer[startNum++] = (int)num;
        }
        
        return answer;
    }
}