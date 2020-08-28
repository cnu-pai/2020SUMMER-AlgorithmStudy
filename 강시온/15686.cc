#include<iostream>
#include<cstdio>

#include<algorithm>
#include<functional>

#include<string>
#include<vector>
#include<queue>
#include<stack>

using namespace std;
const int INF = numeric_limits<int>::max();

int selec[20];
int map;
vector<int> V;
vector<pair<int, int>> house;
vector<pair<int, int>> chicken;
int n, m;
int ans = INF;

void dfs(int idx, int cnt)
{
	if (cnt == m) {
		int sum = 0;
		for (int i = 0; i < house.size(); i++) {
			int dist = INF;
			for (int j = 0; j < chicken.size(); j++) {
				if (selec[j]) {
					dist = min(dist, abs(house[i].first - chicken[j].first) + abs(house[i].second - chicken[j].second));
				}
			}
			sum += dist;
		}
		ans = min(ans, sum);
		return;
	}

	for (int i = idx; i < chicken.size(); i++) {
		if (selec[i] == true)continue;
		selec[i] = true;
		dfs(i + 1, cnt + 1);
		selec[i] = false;
	}

}

int main()
{
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> map;
			if (map == 1) {
				house.push_back({ i, j });
			}
			else if (map == 2) {
				chicken.push_back({ i,j });
			}
		}
	}
	dfs(0, 0);
	cout << ans;
}