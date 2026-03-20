multiplos_7 = 0
multiplos_9 = 0

for número in range(1000, 5000):
    n = int(input("digite el número" + str(número)+":"))
    if número % 7 == 0:
        multiplos_7 + 1
    if número % 9  == 0:
        multiplos_9 + 1

print("multiplos de 7:", multiplos_7)
print("multiplos de 9:", multiplos_9)