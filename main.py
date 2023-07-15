def findLeaders(arr):
    max=0
    leaderList=[]
    for i in arr[::-1]:
        if i>max:
            max=i
            leaderList.append(i)
    return leaderList
print(findLeaders(list(map(int,input().split()))))