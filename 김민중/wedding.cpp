#include <iostream>
using namespace std;

int main() {
  int map[501][501];
  int visit[501];

  int N, M, a, b;
  int cnt = 0;
  
  cin >> N >> M;
  for(int i = 0; i < M; i++) {
    cin >> a >> b;
    map[a][b] = 1;
    map[b][a] = 1;
  }
  for(int i = 2; i <= N; i++) {
    if(map[1][i]) {
      visit[i] = 1;
      for(int j = 2; j<=N; j++) {
        if(map[i][j] == 1) {
          visit[j] = 1;
        }
      }
    }
  }
  for(int i =2; i <=N; i++) {
    if(visit[i] == 1) {
      cnt++;
    }
  }
  cout << cnt << endl;

  return 0;
}