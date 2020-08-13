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
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	priority_queue<int, vector<int>, less<int>> maxheap;
	priority_queue<int, vector<int>, greater<int>> minheap;

	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		int x;
		cin >> x;
		minheap.push(x);
	}
	int ans = 0;
	int sum = 0;
	while (!minheap.empty()) {
		if (minheap.size() == 1) {
			break;
		}
		if (minheap.size() > 2) {
			int a = minheap.top();
			minheap.pop();
			int b = minheap.top();
			minheap.pop();
			ans += a + b;
			minheap.push(a + b);
		}
		else {
			int a = minheap.top();
			minheap.pop();
			int b = minheap.top();
			minheap.pop();
			ans += a + b;
		}
		
	}
	cout << ans;

}