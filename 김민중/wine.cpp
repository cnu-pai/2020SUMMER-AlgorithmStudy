#include <cstdio>
#include <vector>
#include <iostream>
using namespace std;

int max(int a, int b, int c) {
    return a > b ? (a > c) ? a : c : (b > c) ? b : c;
}

int main()
{
    int n;
    cin >> n;
    vector<int> c(n+1, 0);
    vector<int> d(n+1, 0);

    for (int i = 1; i <= n; i++) {
        cin >> c[i];
    }

    d[1] = c[1];
    if (n > 1) {
        d[2] = c[1] + c[2];
    }
    if (n > 2) {
        for (int i = 3; i <= n; i++) {
            d[i] = max(d[i - 1], d[i - 2] + c[i], d[i - 3] + c[i - 1] + c[i]);
        }
    }
    
    cout << d[n] << endl;

    return 0;
}