#include<iostream>
#include<cstdio>

#include<algorithm>
#include<functional>

#include<string>
#include<vector>
#include<queue>
#include<stack>

using namespace std;
const int INF = numeric_limits<int>::max();

int main()
{
	int n;
	int arr[200][2];
	int dp[200] = { 0, };
	int ans = 0;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> arr[i][0] >> arr[i][1];
		dp[i] = arr[i][1];
	}
	
	for (int i = 1; i < n; i++) {
		for (int j = 0; j < i; j++) {
			if (i - j >= arr[j][0]) {
				dp[i] = max(arr[i][1] + dp[j], dp[i]);
			}
		}
	}

	for (int i = 0; i < n; i++) {
		if (i + arr[i][0] <= n) {
			ans = max(ans, dp[i]);
		}
	}
	cout << ans;
}