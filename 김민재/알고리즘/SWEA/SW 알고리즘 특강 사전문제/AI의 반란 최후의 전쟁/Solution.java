import java.io.*;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int test_number = 1; test_number <= T; ++test_number) {
            int N = Integer.parseInt(br.readLine());

            int[][] agents = new int[N][3];
            int[] mins = new int[N];

            int stand = 0;

            for (int i = 0; i < N; ++i) {
                String[] input = br.readLine().split(" ");
                int a = Integer.parseInt(input[0]);
                int b = Integer.parseInt(input[1]);
                int c = Integer.parseInt(input[2]);

                int s0 = b + c;
                int s1 = a + c;
                int s2 = a + b;

                agents[i] = new int[]{s0, s1, s2};
                mins[i] = Math.min(Math.min(s0, s1), s2);
                stand += mins[i];
            }

            if (N <= 2) {
                System.out.println("#" + test_number + " -1");
                continue;
            }

            int ans = Integer.MAX_VALUE;

            for (int i = 0; i < N; ++i) {
                for (int j = 0; j < N; ++j) {
                    if (j == i) continue;
                    for (int k = 0; k < N; ++k) {
                        if (k == i || k == j) continue;
                        int part = stand - (mins[i] + mins[j] + mins[k])
                                + agents[i][0] + agents[j][1] + agents[k][2];
                        ans = Math.min(ans, part);
                    }
                }
            }

            System.out.println("#" + test_number + " " + ans);
        }
    }
}
