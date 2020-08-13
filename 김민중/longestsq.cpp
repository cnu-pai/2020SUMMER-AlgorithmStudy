#include <iostream>

using namespace std;

int main() {
  int dp[1001];
  int a[1001];

  int N;
  int result = 0;
  cin >> N;
  for(int i = 1; i <= N; i++) {
    cin>>a[i];
  }
  for(int i =1; i <=N; i++) {
    for(int j = 0; j <=i; j++) {
      if(a[j]<a[i]) {
        dp[i] = max(dp[i], dp[j]+1);
      }
    }
    result = max(dp[i], result);
  }
  cout<<result;

  return 0;
}