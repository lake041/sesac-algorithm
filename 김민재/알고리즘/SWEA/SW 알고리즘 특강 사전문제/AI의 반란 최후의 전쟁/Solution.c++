#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); 
    cout.tie(NULL);

    int T;
    cin >> T;

    for (int test_number = 1; test_number <= T; ++test_number) {
        int N;
        cin >> N;

        vector<vector<int>> agents(N, vector<int>(3));
        vector<int> mins(N);
        int stand = 0;

        for (int i = 0; i < N; ++i) {
            int a, b, c;
            cin >> a >> b >> c;

            int s0 = b + c;
            int s1 = a + c;
            int s2 = a + b;

            agents[i] = {s0, s1, s2};
            mins[i] = min({s0, s1, s2});
            stand += mins[i];
        }

        if (N <= 2) {
            cout << "#" << test_number << " -1\n";
            continue;
        }

        int ans = INT_MAX;

        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                if (j == i) continue;
                for (int k = 0; k < N; ++k) {
                    if (k == i || k == j) continue;
                    int part = stand - (mins[i] + mins[j] + mins[k])
                            + agents[i][0] + agents[j][1] + agents[k][2];
                    ans = min(ans, part);
                }
            }
        }

        cout << "#" << test_number << " " << ans << "\n";
    }

    return 0;
}
