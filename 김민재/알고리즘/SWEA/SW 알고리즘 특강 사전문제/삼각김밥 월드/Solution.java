import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        for (int test_number = 1; test_number <= T; test_number++) {
            int s = sc.nextInt();
            int e = sc.nextInt();
            int sy = 0, sx = 0, ey = 0, ex = 0;

            double sK = (Math.sqrt(8 * s + 1) - 1) / 2;
            double eK = (Math.sqrt(8 * e + 1) - 1) / 2;

            int sKInt = (int) Math.ceil(sK);
            int eKInt = (int) Math.ceil(eK);

            sy = sKInt - 1;
            sx = sKInt - 1 - (sKInt * (sKInt + 1) / 2 - s);

            ey = eKInt - 1;
            ex = eKInt - 1 - (eKInt * (eKInt + 1) / 2 - e);

            int answer = 0;
            if (Math.signum(ey - sy) == Math.signum(ex - sx)) {
                answer = Math.max(Math.abs(sy-ey), Math.abs(sx-ex));
            } else {
                answer = Math.abs(sy-ey) + Math.abs(sx-ex);
            }
            System.out.println("#" + test_number + " " + answer);
        }
        sc.close();
    }
}
