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
	long long ans = 0;
	int check = false;
	int one = 0;
	long long arr[1001];
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
		if (arr[i] != 1) {
			check = true;
		}
		else {
			one++;
		}
		ans ^= arr[i];
	}
	if (!check) {
		if (ans == 1) {
			cout << "cubelover";
		}
		else {
			cout << "koosaga";
		}
		return 0;
	}

	if (one == 0) {
		if (ans == 0) {
			cout << "cubelover";
		}
		else {
			cout << "koosaga";
		}
	}
	else {
		if (one % 2 == 1) {
			if (ans == 0) {
				cout << "cubelover";
			}
			else {
				cout << "koosaga";
			}
		}
		else {
			for (int i = 0; i < n; i++) {
				if (arr[i] != 1) {
					arr[i] = 1;
					break;
				}
			}

			ans = 0;
			for (int i = 0; i < n; i++) {
				ans ^= arr[i];
			}

			if (ans == 0) {
				cout << "cubelover";
			}
			else {
				cout << "koosaga";
			}
		}
		
	}


	
}