str=input("Enter a string = ")
x=len(str)
count=0
for i in range(x//2):
    if(str[i]==str[x-i-1]): 
        count+=1
for i in range(count,x-count):
    print(str[i])