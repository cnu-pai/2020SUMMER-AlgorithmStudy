#include <iostream>
using namespace std;
 
int A, B, C;
 
int left(int n, int k) {
	int result;
	int x;
 
	if (k == 0) {
		return 1;
	}
 
	x = left(n, k / 2);
	result = 1LL * x * x % C;
 
	if (k % 2) {
		result = 1LL * result * n % C;
	}
 
	return result;
}
 
int main(int argc, char *argv[]) 
{
	cin >> A;
	cin >> B;
	cin >> C;
 
	cout << left(A, B) << endl;
}