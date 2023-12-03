a= [-5, 8, -87]
min_e = 0
for i in range(len(a)):
    if a[i] < min_e:
        min_e = a[i]
    else:
        min_e= min_e
print(min_e)