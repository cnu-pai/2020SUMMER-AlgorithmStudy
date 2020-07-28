#include <iostream>

using namespace std;

int a[100];

int gcd(int a, int b) {
  return a % b ? gcd(b,a%b) : b;
}

int main() {
  int n;
  cin >> n;
  cin >> a[0];
  int temp;
  for(int i = 1; i < n; i++) {
    cin >> a[i];
    temp = gcd(a[0], a[i]);
    cout << a[0] / temp << "/" << a[i] / temp << endl;
  }
}