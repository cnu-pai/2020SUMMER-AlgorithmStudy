#include<iostream>
#include<algorithm>

using namespace std;

char candy[51][51];
int ans = 0;
int cnt, n;

void check()
{
	for (int i = 0; i < n; i++) {
		cnt = 1;
		for (int j = 0; j < n - 1; j++) {
			if (candy[i][j] == candy[i][j + 1])
			{
				cnt++;
			}
			else {
				ans = max(ans, cnt);
				cnt = 1;
			}
		}
		ans = max(ans, cnt);
	}

	for (int i = 0; i < n; i++) {
		cnt = 1;
		for (int j = 0; j < n - 1; j++) {
			if (candy[j][i] == candy[j + 1][i])
			{
				cnt++;
			}
			else {
				ans = max(ans, cnt);
				cnt = 1;
			}
		}
		ans = max(ans, cnt);
	}
}

int main()
{
	cin >> n;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> candy[i][j];
		}
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (j < n - 1) {
				swap(candy[i][j], candy[i][j + 1]);
				check();
				swap(candy[i][j], candy[i][j + 1]);
			}
			if (i < n - 1) {
				swap(candy[i][j], candy[i + 1][j]);
				check();
				swap(candy[i][j], candy[i + 1][j]);
			}
		}
	}

	cout << ans;
}