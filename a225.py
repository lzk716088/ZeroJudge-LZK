def sortnum(s):
    return s%10
while True:
    try:
        N= int(input())
        data = input().split()
        num=[int(i) for i in data]
        num.sort(reverse=True)
        num.sort(key=sortnum)
        num =[str(i) for i in num]
        print(" ".join(num))
    except:
        break