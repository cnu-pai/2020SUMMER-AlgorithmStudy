#include<iostream>
#include<algorithm>
#include<string>
#include<vector>

using namespace std;

bool cmp(int a, int b) {
	string newa;
	string newb;
	newa += to_string(a) + to_string(b);
	newb += to_string(b) + to_string(a);
	return newa < newb;
}

int main()
{
	int k, n;
	int arr[1001];
	vector<int> a;
	cin >> k >> n;
	for (int i = 0; i < k; i++) {
		cin >> arr[i];
		a.push_back(arr[i]);
	}
	sort(arr, arr + k);
	for (int i = 0; i < n - k; i++) {
		a.push_back(arr[k - 1]);
	}
	sort(a.begin(), a.end(), cmp);
	for (int i = a.size()-1; i >= 0; i--) {
		cout << a[i];
	}
}
