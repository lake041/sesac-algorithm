package CodingTestPrac;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;

public class Clothes {
    public static void main(String[] args) {
        String[] a = new String[]{"yellow_hat", "headgear"};
        String[] b = new String[]{"blue_sunglasses", "eyewear"};
        String[] c = new String[]{"green_turban", "headgear"};
        String[][] d = new String[][]{a,b,c};
        System.out.println("solution(d) = " + solution(d));
    }

    public static int solution(String[][] clothes) {
        int ans = 1;

        HashMap<String, Integer> map = new HashMap<>();

        for (String[] clothe : clothes) {
            if (map.containsKey(clothe[1])) {
                int val = map.get(clothe[1]);
                map.put(clothe[1], val + 1);
            } else {
                map.put(clothe[1], 2);
            }
        }

        for (String s : map.keySet()) {
            ans *= map.get(s);
        }
        ans -=1;
        return ans;
    }

}
