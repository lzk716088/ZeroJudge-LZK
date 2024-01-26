def isIvalid(N):
    index1=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    index2=["10","11","12","13","14","15","16","17","34","18","19","20","21","22","35","23","24","25","26","27","28","29","32","30","31","33"]
    if ord(N[0]) <=90 and ord(N[0]) >=65 and (N[1]=="1" or N[1] =="2"):
        index3=[]
        index4=[1,9,8,7,6,5,4,3,2,1,1]
        numpos=index1.index(N[0])
        x,y = int(index2[numpos][0]) , int(index2[numpos][1]) 
        index3.append(x)
        index3.append(y)
        for i in range(1,len(N)):
            index3.append(int(N[i]))
        check=0
        for i in range(len(index3)):
            check+=(index3[i]*index4[i])
        if check%10==0:
            return False
        else:
            return True
    else:
        return True

try:
    while True:
        try:
            n=int(input())
        except ValueError:
            n=int(input())
        data=[]
        T=[]
        O=[]
        F=[]
        for i in range(n):
            data.append(input())
        for i in data:
            if isIvalid(i):
                F.append(i)
            else:
                if i in T:
                    O.append(i)
                else:
                    T.append(i)
        print(f"{len(T)},{len(O)},{len(F)}")
except EOFError:
    pass