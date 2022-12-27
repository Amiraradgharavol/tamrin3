x = int(input("plz enter rows: "))
y =  int(input("plz enter cols: "))
n = 1
for i in range(1 , x + 1):
    for j in range(1 , y + 1):
        if n == 1:
            print(end=("*"))
        else:
            print(end=("#"))

        n = -n 
    if y % 2 == 0:
        n*= -1
        print()
