a='<abcdefg>'
A=[]
for i in range(0,len(a)):
    if a[i]=='<':
        while i!='>':
            a=a.replace(a[i],"")
            print(a)
    else:
        A.append(a[i])

print(A,'ㅁㅁㅁ')