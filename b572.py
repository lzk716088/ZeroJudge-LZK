n= int(input())
for i in range(n):
    data = input().split()
    HM1=[int(data[0]),int(data[1])]
    HM2=[int(data[2]),int(data[3])]
    M3=int(data[4])
    time1 = HM1[0]*60+HM1[1]
    time2 = HM2[0]*60+HM2[1]
    if time2-time1 >=M3:
        print("Yes")
    else:
        print("No")