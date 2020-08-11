#include<iostream>
#include<cstdio>

#include<algorithm>
#include<functional>
#include<cmath>

#include<string>
#include<vector>
#include<queue>
#include<stack>


using namespace std;
const int INF = numeric_limits<int>::max();
const long long LINF = numeric_limits<long long>::max();

bool check[1000001];

int main()
{
	long long minnum, maxnum;
	int cnt = 0;
	vector<long long> arr;
	cin >> minnum >> maxnum;
	long long maxnn = sqrt(maxnum);
	for (long long i = 1; i <= maxnn; i++) {
		arr.push_back(i*i);
	}
	
	for (int i = 1; i < arr.size(); i++) {

		long long minnn = minnum;
		if (minnum % arr[i] != 0) {
			minnn = (minnum / arr[i] + 1) * arr[i];
		}
		for (long long j = minnn; j <= maxnum; j += arr[i]) {
			if (!check[j - minnum]) {
				check[j - minnum] = true;
				cnt++;
			}
		}
	}
	cout << maxnum-minnum+1-cnt;
}