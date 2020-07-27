#include<iostream>
#include<algorithm>
#include<vector>
#include<cstdio>

using namespace std;

int main() {
	int n;
	cin >> n;
	vector<int> a(n);
	vector<int> b(n);
	vector<int > a2(n);
	for (int i = 0; i < n; i++) {
		scanf("%1d", &a[i]);
	}
	a2 = a;
	for (int i = 0; i < n; i++) {
		scanf("%1d", &b[i]);
	}
	vector<int> swit(n);
	int cnt0 = 0;
	swit[0] = 0;
	for (int i = 1; i < n; i++) {
		if (a[i - 1] == b[i - 1]) {
			swit[i] = 0;
		}
		else {
			a[i - 1] = 1 - a[i - 1];
			a[i] = 1 - a[i];
			if (i + 1 < n) {
				a[i + 1] = 1 - a[i + 1];
			}
			cnt0++;
		}
	}
	if (a[n - 1] != b[n - 1])cnt0 = n+1;

	int cnt1 = 1;
	a2[0] = 1 - a2[0];
	a2[1] = 1 - a2[1];
	for (int i = 1; i < n; i++) {
		if (a2[i - 1] == b[i - 1]) {
			swit[i] = 0;
		}
		else {
			a2[i - 1] = 1 - a2[i - 1];
			a2[i] = 1 - a2[i];
			if (i + 1 < n) {
				a2[i + 1] = 1 - a2[i + 1];
			}
			cnt1++;
		}
	}
	if (a2[n - 1] != b[n - 1])cnt1 = n+1;

	int ans = min(cnt0, cnt1);
	if (ans == n + 1)ans = -1;

	cout << ans;

	

}