from math import sqrt
g=9.80665 #m/s
h0=1000 #m
m=80 #kg
ak=sqrt(2*g*h0)
print(f'{ak} m/s')
f=m*ak
print(f'{f} N')
m=f/ak
print(f'{m} kg')