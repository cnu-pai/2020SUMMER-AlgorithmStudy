#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;
const int INF = numeric_limits<int>::max();

int main()
{
	long long n;
	cin >> n;
	vector<long long> v;
	v.push_back(-INF);
	long long x;
	int ans=0;
	for (int i = 0; i < n; i++) {
		cin >> x;
		if (v.back() < x) {
			v.push_back(x);
			ans++;
		}
		else {
			auto it = lower_bound(v.begin(), v.end(), x);
			*it = x;
		}
	}
	cout << ans << "\n";
}