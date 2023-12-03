a = 'atharva'
b = ['a', 'e', 'i', 'o', 'u']
v=0
c=0
for i in range(len(a)):
    
   if a[i] in b:
    v= v+1
    
   else:
      c=c+1
      
print(v,c) 