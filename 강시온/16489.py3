import math
import decimal
a, b, c = map(float, input().split())
a = decimal.Decimal(a)
b = decimal.Decimal(b)
c = decimal.Decimal(c)
s = (a + b + c) / 2;
S = s*(s - a)*(s - b)*(s - c)
S = S.sqrt()
R = (a*b*c) / (4 * S);
r = (2 * S) / (a + b + c);
d = max(decimal.Decimal(0),R * (R - 2 * r))
d = d.sqrt()
k = r + R;
print(S, R, r, d, k);
