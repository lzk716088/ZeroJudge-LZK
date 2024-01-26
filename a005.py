n=int(input())
for i in range(n):
    data = input().split()
    data = [int(x) for x in data]
    if data[1]-data[0] == data[2]-data[1]:
        d=data[1]-data[0]
        data.append(data[3]+d)
        data = [str(x) for x in data]
        print(" ".join(data))
    else:
        r=data[1]//data[0]
        data.append(data[3]*r)
        data = [str(x) for x in data]
        print(" ".join(data))

        
