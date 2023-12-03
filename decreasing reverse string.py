a ='amity'
for i in range(len(a)):
    for j in range(len(a)-i):
        print(a[::-1][j], end='')
    print()