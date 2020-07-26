#include<iostream>

using namespace std;

int main()
{
	int n;
	int h[100001];
	int sum1 = 0;
	int sum2 = 0;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> h[i];
		sum1 += h[i];
		sum2 += h[i] / 2;
	}
	if ((sum2 >= sum1 / 3) && (sum1 % 3 == 0)) {
		cout << "YES";
	}
	else {
		cout << "NO";
	}
	
}