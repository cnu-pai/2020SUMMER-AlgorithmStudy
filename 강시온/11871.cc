#include <iostream>
using namespace std;
int main() {
    int n;
    cin >> n;
    int ans = 0;
    for (int i=0; i<n; i++) {
        int x;
        cin >> x;
        if (x % 2 == 0) {
            x = (x/2)-1;
        } else {
            x = (x+1)/2;
        }
        ans ^= x;
    }
    if (ans == 0) {
        cout << "cubelover\n";
    } else {
        cout << "koosaga\n";
    }
    return 0;
}