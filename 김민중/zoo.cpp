#include <iostream>
using namespace std;

int main() {
  int zoo[100001];

  int N;

  cin >> N;
  zoo[1] = 3;
  zoo[2] = 7;
  for(int i = 3; i<=N; i++) {
    zoo[i] = (2*zoo[i-1] + zoo[i-2]) % 9901;
  }
  cout << zoo[N] << endl;
}