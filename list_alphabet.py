s1=input("first string")
s2=input("second string")
lis1=[]
for i in s1:
    if i==" ":
        pass
    else:
        lis1.append(i)
lis2=[]
for j in s2:
    if j==" ":
        pass
    else:
        lis2.append(j)
lis=lis1+lis2
#print(lis)
xyz=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
c=0
for k in xyz:
    if k in lis:
        c=c+1
    else:
        pass
print(c,"letters of english alphabet contain in both string")
if c==26:
    pass
else:
    print(" Hence all letters are not contain")

        
