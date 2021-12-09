num = int(input("input\n"))
print("output")
for i in range(num):
    print(" "*(num-1),"*"*(((i+1)*2)-1))
    num-=1
    i+=1