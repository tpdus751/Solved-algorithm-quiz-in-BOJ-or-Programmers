import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        List<Integer> list = new ArrayList<>();
        
        int currentInt = 0;
        
        for (int i = 0; i < arr.length; i++) {
            if (i == 0) {
                currentInt = arr[i];   
                list.add(arr[i]);
            } else {
                if (arr[i] == arr[i - 1]) {
                    continue;
                } else {
                    list.add(arr[i]);
                }
            }
        }
        
        int[] answer = new int[list.size()];
        
        int startNum = 0;
        for (Integer num : list) {
            answer[startNum++] = (int)num;
        }

        return answer;
    }
}