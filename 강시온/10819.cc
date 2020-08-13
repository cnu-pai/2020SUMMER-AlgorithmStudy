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

vector<int> arr;

int main()
{
	int ans = 0;
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		int x;
		cin >> x;
		arr.push_back(x);
	}
	sort(arr.begin(), arr.end());

	while (next_permutation(arr.begin(), arr.end()))
	{
		int sum = 0;
		for (int i = 0; i < n - 1; i++) {
			sum += abs(arr[i] - arr[i + 1]);
		}
		ans = max(ans, sum);
	}
	cout << ans;
}