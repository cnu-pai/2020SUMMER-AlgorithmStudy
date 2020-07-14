#include<iostream>

using namespace std;

int main()
{
	long long d[100001][4] = { 0, };
	d[1][1] = 1;
	d[2][2] = 1;
	d[3][1] = 1;
	d[3][2] = 1;
	d[3][3] = 1;
	for (int i = 4; i < 100001; i++)
	{
		d[i][1] = (d[i - 1][2] + d[i - 1][3]) % 1000000009;
		d[i][2] = (d[i - 2][1] + d[i - 2][3]) % 1000000009;
		d[i][3] = (d[i - 3][1] + d[i - 3][2]) % 1000000009;
	}
	int t;
	cin >> t;
	while (t--)
	{
		int a;
		cin >> a;
		cout << (d[a][1] + d[a][2] + d[a][3]) % 1000000009 << "\n";
	}
}