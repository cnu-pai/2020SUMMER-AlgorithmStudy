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
		V.push_back(i + 1);
		dfs(cnt + 1);
		V.pop_back();
	}

}

int main()
{
	cin >> n >> m;
	dfs(0);
}