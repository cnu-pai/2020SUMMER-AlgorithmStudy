#include <vector>
#include <math.h>
#include <iostream>

using namespace std;

int main()
{
	vector<bool> arr(1000 + 1);
	vector<int> prime;
	for (int i = 2; i <= sqrt(1000); i++) {
		if (arr[i] == true)
			continue;
		for (int j = i + i; j <= 1000; j += i) {
			arr[j] = true;
		}
	}
	for (int i = 2; i <= 1000; i++) {
		if (arr[i] == false)
			prime.push_back(i);
	}
	int n;
	cin >> n;
	while (n--) {
		bool check = false;
		int a;
		cin >> a;
		for (int i = 0; i < prime.size(); i++) {
			for (int j = i; j < prime.size(); j++) {
				for (int k = j; k < prime.size(); k++) {
					if (prime[i] + prime[j] + prime[k] == a) {
						cout << prime[i] << " " << prime[j] << " " << prime[k] << "\n";
						check = true;
					}
					if (check)break;
				}
				if (check)break;
			}
			if (check)break;
		}
		if (!check) {
			cout << "0";
		}
	}
}