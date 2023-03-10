print("ingresa el primer numero: ")
a = int(input())
print("ingresa el segundo numero: ")
b = int(input())
print("ingresa el tercer numero: ")
c = int(input())


if a > b and b > c :
    print( "",a , "-", b, "-", c)
elif b > a and a > c:
    print( "",b , "-", a, "-", c)
elif c > a and a > b:
    print( "",a , "-", b, "-", c)
elif c > b and b > a :
    print( "",c, "-", a, "-", b)
elif a > c and c > b:
    print( "",a , "-", c, "-", b)
elif b > c and c > a:
    print( "",c , "-", b, "-", a)
else :
    print("se ingresaron numeros iguales")