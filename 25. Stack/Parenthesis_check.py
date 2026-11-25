a=input("Enter the expression")
c=0
# print(len(a))
for i in range(len(a)):
    if(a[i]=='('):
        c+=1
    elif(a[i]==')'):
        c-=1
    else:
        continue
if(len(a)==0):
    print("Please enter the expression")
elif (c==0 and len(a)>0):
    print("Valid parenthesis")
else:
    print("Invalid parenthesis")
