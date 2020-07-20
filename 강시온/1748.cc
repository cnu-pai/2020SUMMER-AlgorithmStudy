#include<iostream>

using namespace std;

int main()
{
	int n;
	int sum = 0;
	cin >> n;
	int check = 1;
	while (check <= n) {
		sum += (n - check + 1);
		check *= 10;
	}
	cout << sum;
}