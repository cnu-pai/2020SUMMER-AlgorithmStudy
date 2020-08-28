#define _USE_MATH_DEFINES

#include<iostream>
#include<cstdio>
#include<cmath>

#include<algorithm>
#include<functional>

#include<string>
#include<vector>
#include<queue>
#include<stack>

using namespace std;
const int INF = numeric_limits<int>::max();
const double pi = M_PI;

int main()
{
	int n;
	cin >> n;
	vector<bool> arr(n + 1);
	vector<int> prime;
	for (int i = 2; i <= sqrt(n); i++) {
		if (arr[i] == true)
			continue;
		for (int j = i + i; j <= n; j += i) {
			arr[j] = true;
		}
	}
	for (int i = 2; i <= n; i++) {
		if (arr[i] == false)
			prime.push_back(i);
	}

	int cnt = 0;
	for (int i = 0; i < prime.size(); i++) {
		
		int sum = 0;
		int j = 0;
		for(int j=i;j<prime.size();j++) {
			sum += prime[j];
			if (sum == n) {
				cnt++;
				break;
			}
			if (sum > n)break;
		}
	}
	cout << cnt;

}