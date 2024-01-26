data = input().split()
a,b,c = int(data[0]),int(data[1]),int(data[2])

code = 0
for i in range(1,c+1):
    if i%a==0 or i%b==0:
        code+=i
code= code%26

print(chr(64+code))

