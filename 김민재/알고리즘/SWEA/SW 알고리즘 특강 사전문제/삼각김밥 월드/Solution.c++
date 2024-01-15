#include <iostream>
#include <cmath>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL); 
    cout.tie(NULL);

    int T;
    cin >> T;

    for (int test_number = 1; test_number <= T; test_number++) {
        int s, e, sy = 0, sx = 0, ey = 0, ex = 0;
        cin >> s >> e;

        int sKInt = ceil((sqrt(8 * s + 1) - 1) / 2);
        int eKInt = ceil((sqrt(8 * e + 1) - 1) / 2);

        sy = sKInt - 1;
        sx = sKInt - 1 - (sKInt * (sKInt + 1) / 2 - s);

        ey = eKInt - 1;
        ex = eKInt - 1 - (eKInt * (eKInt + 1) / 2 - e);

        int answer = 0;
        if ((ey - sy > 0 && ex - sx > 0) || (ey - sy < 0 && ex - sx < 0)) {
            answer = max(abs(sy-ey), abs(sx-ex));
        } else {
            answer = abs(sy-ey) + abs(sx-ex);
        }
        cout << "#" << test_number << " " << answer << "\n";
    }
    return 0;
}
