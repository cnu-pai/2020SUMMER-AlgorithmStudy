#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>
#include<cstdio>
#include<string>

using namespace std;
const int INF = numeric_limits<int>::max();

vector<int> V;
int n, m;

void dfs(int idx, int cnt)
{
	if (cnt == m) {
		for (int i = 0; i < V.size(); i++) {
			cout << V[i] << " ";
		}
		cout << "\n";
		return;
	}

	for (int i = idx; i < n; i++) {
		V.push_back(i + 1);
		dfs(i, cnt + 1);
		V.pop_back();
	}

}

int main()
{
	cin >> n >> m;
	dfs(0, 0);
}