#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main()
{
	int n;
	cin >> n;
	vector<int> v;
	v.push_back(-1);
	int x;
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
	cout << ans << " ";
}