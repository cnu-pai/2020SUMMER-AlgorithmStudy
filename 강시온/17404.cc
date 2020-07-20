#include<iostream>
#include<algorithm>
using namespace std;

int main()
{
    int n;
    int input[1000][3];
    int data[1000][3];
    int ans = 1000*1000+1;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
        scanf("%d %d %d", &input[i][0], &input[i][1], &input[i][2]);
    
    for(int k=0;k<3;k++){
        
        for (int i = 0; i < 3; i++){
            if(i == k){
                data[0][i] = input[0][i];
            }
            else{
                data[0][i] = 1000*1000+1;
            }
        }
        
        for (int i = 1; i < n; i++)
        {
            data[i][0] = min(data[i - 1][1], data[i - 1][2]) + input[i][0];
            data[i][1] = min(data[i - 1][0], data[i - 1][2]) + input[i][1];
            data[i][2] = min(data[i - 1][0], data[i - 1][1]) + input[i][2];
        }
        
        for(int i=0;i<3;i++){
            if(i==k)continue;
            ans = min(ans, data[n-1][i]);
        }
    }
    cout << ans;
}
