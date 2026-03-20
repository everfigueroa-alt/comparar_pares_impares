cant_par = 0
cant_imp = 0

for i in range(1, 21) :
    n = int(input("Digite el numero"+ str(i)+ ":"))
    
    m = n%2

    if(m == 0) :
        cant_par = cant_par + 1
    else:
        cant_imp = cant_imp + 1

print("números pares: " , cant_par)
print("números impares: " , cant_imp)