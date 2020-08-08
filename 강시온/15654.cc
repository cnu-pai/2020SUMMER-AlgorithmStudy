#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int selec[10];
vector<int> input;
vector<int> V;
int n, m;

void dfs(int cnt)
{
	if (cnt == m) {
		for (int i = 0; i < V.size(); i++) {
			cout << V[i] << " ";
		}
		cout << "\n";
		return;
	}

	for (int i = 0; i < n; i++) {
		if (selec[i] == true)continue;
		selec[i] = true;
		V.push_back(input[i]);
		dfs(cnt + 1);
		V.pop_back();
		selec[i] = false;
	}

}

int main()
{
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		int x;
		cin >> x;
		input.push_back(x);
	}
	sort(input.begin(), input.end());
	dfs(0);
}