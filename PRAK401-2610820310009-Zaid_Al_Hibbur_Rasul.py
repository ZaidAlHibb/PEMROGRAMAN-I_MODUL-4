inputs = input("").strip().split()

angka = int(inputs[0])
simbol = inputs[1]

for i in range(1, 51, 1):
    if i % angka == 0 :
        print(simbol, end=" ")
    else :
        print(i, end=" ")