#practicing operators Arithmetic operators
a=20
b=6
print("Addition:", a+b)
print("subtraction", a-b)
print("multiplication:",a*b)
print("Division:", a/b)
print("floor division:",a//b)
print("module:", a%b)
print("exponentiation:", a**b)

a=17
b=5
print(a%b)
#practicing comparision operators
a=15
b=10
print('greater value:', a>b)
print('lesser value:', a<b)
print('equal:', a==b)
print('Not equal:', a!=b)
print('greater or equal:', a>=b)
print('less or equal to:', a<=b)
#practicing logical operators
a=17
print(a>15 and a<20)
b=17
print(b>18 or b==17)
is_student=True
print(not is_student)
#assignment operators
x=10
x+=5
print(x)
x=10
x-=3
print(x)
x=10
x*=2
print(x)
x=20
x/=4
print(x)
x=17
x%=5
print(x)
x=17
x//=5
print(x)
x=2
x**=3
print(x)
#combining multiple assignment operators
points=10
points+=5
points*=2
points-=4
print(points)
#Bitwise operators
#AND
a=5
b=3
print(a & b)
#OR
a=5
b=3
print(a|b)
#XOR
a=5
b=3
print(a^b)
#NOT
a=5
print(~a)
a=5
print(a<<1)
a=8
print(a>>1)
a=6
b=3
print(a&b)
#membership operators ,in
fruits=['apple', 'banana', 'mango',]
print('apple' in fruits)
#membership operators , not in
fruits=['apple', 'banana', 'mango',]
print('orange' not in fruits)
# Identity operators , is
a=[10, 20, 30]
b=a
print(a is b)
#identity opertor is not
a=[10, 20, 30]
b=[10, 20, 30]
print(a is not b)
name="python"
print('p' in name)
print('z' not in name)
a=[1,2,3]
b=a
print(a is b)
#operastor precedence order
#exponentiation
a=2
b=3
print(2**3)
a=5
b=2
print(5**2)
x=2
y=3
z=2
print(2+3**2)
#unary negative, unary positive, bitwise negative or bitwise not
a=10
b=-a
print(b)
print(-5)
print(-(-8))
print(-(3+2))
#multiplication
a=5
b=4
print(a*b)
print(10+5*2)
print(3*2**3)
#division
a=20
b=4
print(a/b)
x=10
y=3
print(x/y)
#floor division
a=20
b=3
print(20//3)
#modulus
a=17
b=5
print(a%b)
#addition
a=10
b=5
print(a+b)
first= "Hello"
second= "Maya"
print(first +" "+ second)
#subtraction
a=20
b=8
print(a-b)
#left shift(<<)
print(5<<1)
#right shift(>>)
print(8>>1)
#bitwise AND
print(5&3)
#bitwise  XOR
print(5^3)
#comparison operators
a=20
b=10
print(a>b)
print(a==b)
print(a!=b)
#Identity operators
a=[10,20,30]
b=[10,20,30]
c=a
print(a==b)
print(a is b)
print(a is not b)
#boolean not
a=True
b=False
print(not a)
print(not b)
age=17
print(not age>18)
#boolean AND
age=20
has_id=True
print(age >= 18 and has_id==True)
#boolean OR
day="sunday"
print(day=="sunday" or day=="saturday")
print(10+5*2-3)
print(2**3+4*2)
a=10
b=20
print(a>5 and b<15 or a==10)
x=5+3*2**2
print(x)
