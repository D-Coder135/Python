query=input()
lsit=[i for i in input().split(' ')]
answer=[]
for i in lsit:
    if (i[:len(query)]==query):
        answer.append(i)
print(answer)
