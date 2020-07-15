#include<iostream>

using namespace std;

int main()
{
	long long d[1000001];
	d[0] = 0;
	d[1] = 1;
	d[2] = 2;
	d[3] = 4;
	for (int i = 4; i < 1000001; i++)
	{
		d[i] = (d[i - 1] + d[i - 2] + d[i - 3]) % 1000000009;
	}
	int t;
	cin >> t;
	while (t--)
	{
		int a;
		cin >> a;
		cout << d[a] << "\n";
	}
}