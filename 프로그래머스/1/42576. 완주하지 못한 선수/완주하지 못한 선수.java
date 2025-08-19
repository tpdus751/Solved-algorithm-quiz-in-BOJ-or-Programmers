import java.util.HashMap;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        
        HashMap<String, Integer> people = new HashMap<>();
        
        for (String person : participant) {
            if (people.get(person) == null) {
                people.put(person, 1);   
            } else {
                people.put(person, people.get(person) + 1);
            }
        }
        
        for (String person : completion) {
            if (people.get(person) != null) {
                people.put(person, people.get(person) - 1);
            }
        }
        
        for (String person : people.keySet()) {
            if (people.get(person) != 0) {
                answer = person;
                break;
            }
        }
        
        return answer;
    }
}