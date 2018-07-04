clear();

#system parameters

M = 0.3;  # 台車の質量 kg
m = 0.2;  # 振子の質量 kg
l = 0.3;  # 振子長の2分の1 m
J = 1/12*m*l^2;  # 振子の慣性モーメント kg・m^2
g = 9.8;  # 重力加速度 m/s^2

alp = (M + m) * (J + m * l^2) - m^2*l^2;

A = [0  0  1  0;
     0  0  0  1;
     0  -m^2*l^2*g/alp  0  0;
     0 (m+M)*m*l*g/alp 0  0];

B = [0;  0; (m*l^2+J)/alp; -(m*l)/alp];

C = [1  0  0  1];

D = 0;

Q = [1000 0 0 0; 0 1 0 0; 0 0 100 0; 0 0 0 100];

R = 1;

[F, X, e] = lqr(A, B, Q, R);

Mo = [C; C*A; C*A^2; C*A^3];
det(Mo);

L = place(A',C',e)';#'

L
F

x = [0.1; 0.1; 0.1; 0.1];
xh= [0; 0; 0; 0];

xb0 = [x; xh];
Ab = [A -B*F; L*C A-B*F-L*C];

dt = 0.01;
t = 0:dt:10;
i = 0;

for n = t
  i = i + 1;
  xb = expm(Ab * n) * xb0;

  x1(i) = xb(1);
  x2(i) = xb(2);
  x3(i) = xb(3);
  x4(i) = xb(4);
  xh1(i) = xb(5);
  xh2(i) = xb(6);
  xh3(i) = xb(7);
  xh4(i) = xb(8);
endfor

plot(t, x1, t, x2, t, x3, t, x4, t, xh1, t, xh2, t, xh3, t, xh4 );
