A = int(input("Masukan bilangan a : "))
B = int(input("Masukan bilangan b : "))
C = int(input("Masukan bilangan c : "))

print("a = ", A)
print("b = ", B)
print("c = ", C)

if A > B and A > C:
    maks = A
    print("Bilangan terbesar adalah a = ", maks)
elif B > A and B > C:
    maks = B
    print("Bilangan terbesar adalah b = ", maks)
else:
    maks = C
    print("Bilangan terbesar adalah c = ", maks)
