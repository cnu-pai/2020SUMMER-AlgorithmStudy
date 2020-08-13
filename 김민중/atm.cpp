#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
 int N = 0;
 int result = 0;
 cin >> N;
 
 vector<int> vec(N,0);
 for(int i = 0; i < N; i++) {
   cin >> vec[i];
 }
 sort(vec.begin(),vec.end());
 for(int i = 0; i < N; i++) {
   result += vec[i]*(N-i);
 }
 cout << result << endl;
}