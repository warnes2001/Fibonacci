#Fibonacci Folge mit Rekursion

#User-Input
i = int(input("Wie lang soll die Fibonacci-Folge sein?: "))

n1,n2 = 0, 1
count = 0

#Testen nach gültiger Zahl
if i <= 0:
    print("Bitte geben Sie eine gültige Zahl ein.")
elif i == 1:
    print(n1)
else:
    while count < i:
        print(n1)
        x = n1 + n2
        n1 = n2
        n2 = x
        count +=1

