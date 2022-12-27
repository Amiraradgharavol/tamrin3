def f():
    d = (b ** 2) - (4 * a * c)
    return d
a = int(input("a :"))
b = int(input("b :"))
c = int(input("c :"))
result = f()
if result < 0:
    print("no roots")
elif result == 0:
    print("2 rishe mosavi darad")
    result = (-b) / (2 * a)
    print(result)
else:
    x = -b + f() ** 0.5 / 2 * a
    y = -b + f() ** 0.5 / 2 * a
    print("x: " , x, "y:", y)
f()