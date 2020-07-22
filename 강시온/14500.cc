#include<iostream>
#include<algorithm>

using namespace std;

int n, m;
int map[501][501];
bool check[501][501];
int dx[4] = { 0,0,-1,1 };
int dy[4] = { -1,1,0,0 };
int ans = 0;

void dfs(int x, int y, int sum, int length)
{
	if (length >= 4) {
		ans = max(ans, sum);
		return;
	}
	for (int i = 0; i < 4; i++) {
		int nx = x + dx[i];
		int ny = y + dy[i];

		if (nx < 0 || nx >= n || ny < 0 || ny >= m)continue;

		if (!check[nx][ny]) {
			check[nx][ny] = true;
			dfs(nx, ny, sum + map[nx][ny], length + 1);
			check[nx][ny] = false;
		}
	}
}

void shape(int x, int y)
{
	int wing = 4;
	int minnum = 987654321;
	int sum = map[x][y];
	for (int i = 0; i < 4; i++) {
		int nx = x + dx[i];
		int ny = y + dy[i];

		if (wing <= 2) {
			return;
		}

		if (nx < 0 || nx >= n || ny < 0 || ny >= m) {
			wing--;
			continue;
		}
		minnum = min(minnum, map[nx][ny]);
		sum = sum + map[nx][ny];
	}

	if (wing == 4) {
		sum -= minnum;
	}
	ans = max(ans, sum);
}

int main()
{
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> map[i][j];
		}
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			dfs(i, j, 0, 0);
			shape(i, j);
		}
	}
	cout << ans;
}