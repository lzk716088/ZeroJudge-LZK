box=[]
while True:
    try:
        m,c = input().split()
        m,c = int(m),int(c)
        box.append([m,c,m*c])
    except EOFError:
        break

box.sort(key=lambda x:x[0],reverse=True)
total =0
for i in box:
    print(f"{i[0]}元鈔票共有{i[1]}張")
    total+=i[-1]
print(f"總共有{total}元")

