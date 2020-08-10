#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>
#include<cstdio>
#include<string>

using namespace std;
const int INF = numeric_limits<int>::max();

int main()
{
	int n, m, b;
	int map[501][501];
	cin >> n >> m >> b;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> map[i][j];
		}
	}

	int h;
	int ans = INF;

	for (int k = 0; k <= 256; k++) {
		int sum = 0;
		int cnt = b;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (k > map[i][j]) {
					sum += k - map[i][j];
					cnt -= k - map[i][j];
				}
				else if (k < map[i][j]) {
					sum += (map[i][j] - k) * 2;
					cnt += map[i][j] - k;
				}
			}
		}
		if (cnt>=0) {
			if (sum <= ans) {
				ans = sum;
				h = k;
			}
		}
	}

	cout << ans << " " << h;
}