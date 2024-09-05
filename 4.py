n=int(input("Enter A number = "))
l=[]
count=1
sum1,sum2,stop_point,diff,digit=0,0,0,0,0
org_num=n
for i in range(1,10):
    sum1=sum1+(i)*9*pow(10,i-1)
    digit+=1
    if(sum1>=org_num):
        stop_point+=1
    if(stop_point==1):
        break
val=((digit)*9*pow(10,digit-1))

sum2=sum1-val

n1 = pow(10, digit - 1) + (n - sum2 - 1) // digit
print(n1)

for i in range(n1):
    l.append(count)
    count+=1
print(l)

count_of_mod=n%digit

def mod(n):
    n=n%10

def div(n):
    n=n//10

for i in range(count_of_mod):
    main_mod=mod(l[n1-1])
    l[n1-1]=div(l[n1-1])
print(main_mod)