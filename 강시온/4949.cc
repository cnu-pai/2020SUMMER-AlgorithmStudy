#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<stack>

using namespace std;

int main()
{
	string s;
	while (1) {
		stack<char> t;
		bool ans=true;
		getline(cin, s);
		if (s == ".")break;
		for (int i = 0; i < s.size(); i++) {
			if (s[i] == '(' || s[i] == '[') {
				t.push(s[i]);
			}
			else if (s[i] == ')') {
				{
					if (!t.empty()) {
						if (t.top() == '(') {
							t.pop();
						}
						else {
							ans = false;
						}
					}
					else {
						ans = false;
					}
				}
			}
			else if (s[i] == ']') {
				{
					if (!t.empty()) {
						if (t.top() == '[') {
							t.pop();
						}
						else {
							ans = false;
						}
					}
					else {
						ans = false;
					}
				}
			}
		}
		if (t.empty() && ans==true) {
			cout << "yes\n";
		}
		else {
			cout << "no\n";
		}
	}
}