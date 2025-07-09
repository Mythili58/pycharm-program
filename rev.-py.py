l=[]
for i in range(5):
    num=int(input('Enter a number: '))
    l.append(num)
print(l[::-1])
print(sum(l))
print(sum(l)//len(l))