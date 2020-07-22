#include<iostream>
#include<algorithm>

using namespace std;

bool b[10];

int possible(int c) {
	if (c == 0) {
		return b[0] ? 0 : 1;
	}
	int len = 0;
	while (c) {
		if (b[c % 10]) return false;
		len += 1;
		c /= 10;
	}
	return len;
}

int main()
{
	int n, m;
	cin >> n;
	cin >> m;
	for (int i = 0; i < m; i++) {
		int x;
		cin >> x;
		b[x] = true;
	}
	int ans = n - 100;
	if (ans < 0) {
		ans = -ans;
	}
	for (int i = 0; i <= 1000000; i++) {
		int c = i;
		int len = possible(c);
		if (len > 0) {
			int press = c - n;
			if (press < 0) {
				press = -press;
			}
			ans = min(ans, len + press);
		}
	}
	cout << ans;
}