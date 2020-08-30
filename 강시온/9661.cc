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
	long long n;
	cin >> n;
	if (n % 5 == 0 || n % 5 == 2) {
		cout << "CY";
	}
	else {
		cout << "SK";
	}
}