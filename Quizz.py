name=input("Enter Your Name:")
print("Welcome {} to the python Quizz".format(name))
s=0
q1='''Who Developed Python??
A-aaa
B-bbb
C-ccc
D-ddd'''
q2='''Who Developed Python??
A-aaa
B-bbb
C-ccc
D-ddd'''
q3='''Who Developed Python??
A-aaa
B-bbb
C-ccc
D-ddd'''
q4='''Who Developed Python??
A-aaa
B-bbb
C-ccc
D-ddd'''
q5='''Who Developed Python??
A-aaa
B-bbb
C-ccc
D-ddd'''
d={q1:'b',q2:'a',q3:'c',q4:'d',q5:'a'}
for i in d:
    print(i)
    skip=input("Do You Want to Skip this ques:(Y/N)")
    if skip=='y':
        continue
    ans=input("Enter the answer(a,b,c,d):")
    print(ans)
    if ans==d[i]:
        s+=1
        print(s)
    else:
        s-=1
print(s)
print(f"{name} your Total Score={s}")
