#include <iostream>
#include <cstdio>

#include <algorithm>
#include <functional>

#include <string>
#include <vector>
#include <queue>
#include <stack>

using namespace std;
const int INF = numeric_limits<int>::max();

int main()
{
	int ans = INF;
	int n;
	cin >> n;
	int arr[21][21];
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> arr[i][j];
		}
	}
	vector<int> v;
	for (int i = 0; i < n / 2; i++) v.push_back(0);
	for (int i = 0; i < n / 2; i++) v.push_back(1);
	do {
		vector<int> start;
		vector<int> link;
		for (int i = 0; i < v.size(); i++) {
			if (v[i]) start.push_back(i);
			else link.push_back(i);
		}
		int ssum = 0;
		int lsum = 0;
		for (int i = 0; i < n / 2; i++) {
			for (int j = i + 1; j < n / 2; j++) {
				ssum += arr[start[i]][start[j]] + arr[start[j]][start[i]];
				lsum += arr[link[i]][link[j]] + arr[link[j]][link[i]];
			}
		}
		ans = min(ans, abs(ssum - lsum));
	} while (next_permutation(v.begin(), v.end()));
	cout << ans;
}