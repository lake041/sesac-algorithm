package CodingTestPrac;

import java.util.HashMap;

public class Marathon {
    public static void main(String[] args) {

    }

    public static String solution(String[] participant, String[] completion) {
        String answer = "";

        HashMap<String, Integer> map = new HashMap<>();
        for (String s : participant) {
            if (map.containsKey(s)) {
                int val = map.get(s);
                map.put(s, val + 1);
            } else {
                map.put(s, 1);
            }
        }

        for (String s : completion) {
            int val = map.get(s);
            map.put(s, val-1);
        }

        for (String s : map.keySet()) {
            if (map.get(s) > 0) {
                return s;
            }
        }


        return answer;
    }
}



