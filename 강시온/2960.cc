#include <vector>
#include <cmath>
#include <cstdio>
#include<iostream>

using namespace std;

int main() {
	int N,k;
	int cnt = 0;
	cin >> N >> k;
	int ans = 0;
	vector<bool> arr(N + 1);
	for (int i = 2; i <= N; i++) {
		if (arr[i] == true)
			continue;
		for (int j = i; j <= N; j += i) {
			if (arr[j] == true)
				continue;
			arr[j] = true;
			cnt++;
			if (cnt == k) {
				ans = j;
			}
		}
	}
	cout << ans;
	
	return 0;
}