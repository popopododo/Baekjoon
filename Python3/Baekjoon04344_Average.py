T=int(input())

while(T<0):
    scorelist=list(map(int,input().split()))
    subject=scorelist.pop()
    total=0
    for x in scorelist:
        total+=x
    print('{}%'.format(round(total/subject,3)),end="\n")
    t=-1
