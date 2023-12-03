a = [[2,8], [3,3], [5,5]]
b=[]

for i in range(len(a)):
    
    for j in range(len(a[i])):
        c = []
        c.append(a[i][j])
        b.append(c)

print(b) 