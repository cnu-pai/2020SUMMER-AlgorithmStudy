#include <stdio.h>
int a, b, c, d;
int gcd(int a, int b) { return b ? gcd(b, a%b) : a; }
int main() {
	scanf("%d %d %d %d", &a, &b, &c, &d);
	a = a*d + b*c, c = b*d, b = gcd(a, c);
	printf("%d %d", a/b, c/b);
	return 0;
}