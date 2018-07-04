clear();
A = [0 1; -5 -6]
B = [0; 1]
C = [1 0]

Mc = [B, A*B];
det(Mc)

K = place(A,B,[-2,-3]);
K

t = 0:0.01:5;
i = 0;
x0 = [1; 0];
for n = t
 i = i + 1;
 x = expm(A * n) * x0;
 x1(i) = x(1);
 x2(i) = x(2);
 xa = expm((A-B*K) * n) * x0;
 xa1(i) = xa(1);
 xa2(i) = xa(2);
endfor
plot(t, x1, '.', t, x2, '.', t, xa1, t, xa2) 
