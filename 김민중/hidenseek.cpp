#include<iostream>
#include<queue>
using namespace std;
#define MAX_VALUE 100001 
bool visit[MAX_VALUE];
int subin, sis;        
 
int bfs(int n, int m) {
    int t = 0;      
    queue<int> q;
    q.push(n);
 
    while(1) {
        int size = q.size();
 
        for(int i=0; i<size; i++) {
            n = q.front();
            q.pop();
            if(n == m)
                return t;        
            if(n > 0 && visit[n-1] == 0) {
                q.push(n-1);
                visit[n-1] = 1;
            }
            if(n < 100000 && visit[n+1] == 0) {
                q.push(n+1);
                visit[n+1] = 1;
            }
            if(n*2 <= 100000 && visit[n*2] == 0) {
                q.push(n*2);    
                visit[n*2] = 1;
            }
        }
        t++;
    }
}
 
int main() {
    cin >> subin >> sis;
    cout << bfs(subin, sis);
    return 0;
}