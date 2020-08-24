#include<iostream>
#include<string>
#include<vector>
#include<algorithm>

using namespace std;

int main()
{
    int n;
    cin >> n;
    int x;
    vector<pair<int,int>> arr;
    int ans[51];
    for(int i=0;i<n;i++){
        cin >> x;
        arr.push_back(make_pair(x,i));
    }
    sort(arr.begin(),arr.end());
    for(int i=0;i<n;i++){
        ans[arr[i].second] = i;
    }
    for(int i=0;i<n;i++){
        cout << ans[i] << " ";
    }
}
