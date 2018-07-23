number = int(input("enter the number:"))
for i in range(2,number):
    if (number%i)==0:
        print("{} is not Prime".format(i))
        break
    else:
        print("{} is Prime".format(i))