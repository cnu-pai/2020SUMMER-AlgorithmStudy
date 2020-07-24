#include<iostream>
#include<vector>

using namespace std;

int selec[10];
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
		V.push_back(i + 1);
		dfs(cnt + 1);
		V.pop_back();
		selec[i] = false;
	}

}

int main()
{
	cin >> n >> m;
	dfs(0);
}