#include<iostream>
#include<algorithm>

using namespace std;

int main()
{
	int n;
	int input[100001];
	int dp[100001][2];
	int result = 0;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &input[i]);
	}
	dp[0][0] = input[0];
	dp[0][1] = input[0];
	result = input[0];
	for (int i = 1; i < n; i++) {
		dp[i][0] = max(dp[i - 1][0] + input[i], input[i]);
		dp[i][1] = max(dp[i - 1][0], dp[i - 1][1] + input[i]);
		result = max(dp[i][0], result);
		result = max(dp[i][1], result);
	}
	printf("%d", result);

}