T=int(input())

while(1):
    scorelist=list(map(int,input().split()))
    subject=scorelist.pop(0)
    total=0
    count=0
    for x in scorelist:
        total+=x
    average=round(total/subject,3)
    for x in scorelist:
        if x>average:
            count+=1
    print('{}%'.format(round(count/subject*100,3)),end="\n")
    T=-1
