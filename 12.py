print("Multiplication Table")

num = int(input("Enter a number between 1 to 15:"))

if num>15 and num<1:
    print("Invalid number....")
else:
    for i in range(1,13,1):
        print ( str(num)+" * "+str(i)+ " = " +str(num*i))
