#include<iostream>

using namespace std;

int main()
{
	int n;
	
	int a[100001][3];
	a[1][0] = 1;
	a[1][1] = 1;
	a[1][2] = 1;
	for (int i = 2; i < 100001; i++) {
		a[i][0] = (a[i - 1][0] + a[i - 1][1] + a[i - 1][2]) % 9901;
		a[i][1] = (a[i - 1][0] + a[i - 1][2]) % 9901;
		a[i][2] = (a[i - 1][0] + a[i - 1][1]) % 9901;
	}
	cin >> n;
	cout << (a[n][0] + a[n][1] + a[n][2]) % 9901;
}