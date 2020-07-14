#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int main()
{
	int d[1000];
	int a[1000];
	vector<int> num[1000];
	int n;
	int result = 0;
	vector<int> rnum;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &a[i]);
	}
	for (int i = 0; i < n; i++) {
		d[i] = 1;
		num[i].push_back(i);
		for (int j = 0; j < i; j++) {
			if (a[j] < a[i] && d[i] < d[j] + 1) {
				d[i] = d[j] + 1;
				vector<int> temp = num[j];
				temp.push_back(i);
				num[i] = temp;
			}
		}
		if (result < d[i]) {
			result = d[i];
			rnum = num[i];
		}
		result = max(result, d[i]);
	}
	cout << result << "\n";
	for (int i = 0; i < rnum.size(); i++) {
		cout << a[rnum[i]] << " ";
	}
}