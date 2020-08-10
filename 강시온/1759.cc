#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int selec[16];
vector<char> input;
vector<char> V;
int check=0;
int n, m;

void dfs(int idx, int cnt)
{
    if (cnt == n) {
        if(check && n-check > 1){
            for (int i = 0; i < V.size(); i++) {
                cout << V[i];
            }
            cout << "\n";
        }
        return;
    }
    
    for (int i = idx; i < m; i++) {
        if (selec[i] == true)continue;
        selec[i] = true;
        V.push_back(input[i]);
        if(input[i] == 'a' || input[i] == 'e' || input[i] == 'i' || input[i] == 'o' || input[i] == 'u')check++;
        dfs(i + 1, cnt + 1);
        V.pop_back();
        if(input[i] == 'a' || input[i] == 'e' || input[i] == 'i' || input[i] == 'o' || input[i] == 'u')check--;
        selec[i] = false;
    }
    
}

int main()
{
    cin >> n >> m;
    for (int i = 0; i < m; i++) {
        char x;
        scanf(" %c",&x);
        input.push_back(x);
    }
    sort(input.begin(), input.end());
    dfs(0, 0);
}
