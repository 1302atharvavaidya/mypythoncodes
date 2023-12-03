a ='amity'
for i in range(len(a)):
    for j in range(i+1):
        print(a[::-1][j], end='')
    print()
for i in range(len(a)):
    for j in range(len(a)-i-1):
        print(a[::-1][j], end='')
    print()