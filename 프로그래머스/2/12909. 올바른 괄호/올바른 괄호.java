class Solution {
    boolean solution(String s) {
        boolean answer = true;

        int after = 0;
        int before = 0;
        
        char[] chars = s.toCharArray();
        
        for (int i = 0; i < chars.length; i++) {
            if (chars[i] == ')') {
                after += 1;
                if (before == 0) {
                    answer = false;
                } else {
                    if (after == before) {
                        after = 0;
                        before = 0;
                    } else if (after > before) {
                        answer = false;
                    } else {
                        continue;
                    }
                }
            } else {
                before += 1;
                continue;
            }
        }
        
        if (before != after) {
            answer = false;
        }
        
        return answer;
    }
}