#include <cstdio>
using namespace std;

int main() {

    int i, j, n, k;
    int dp[10001] = {0, };
    dp[0] = 1;
    scanf("%d %d", &n, &k);

    int coin[n];

    for (i = 0; i < n; i++) scanf("%d", &coin[i]);
    
    
    for (i = 0; i < n; i++) for (j = coin[i]; j <= k; j++) if (j - coin[i] >= 0) dp[j] += dp[j - coin[i]];

    printf("%d\n", dp[k]);
    return 0;
}