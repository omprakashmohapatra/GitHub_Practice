a=int(input("Enter the first number"))
b=int(input("Enter the first number"))

search= int(input("Enter the search value"))

print("searching for {}".format(search))
for i in range(a,b):
    if i == search:
        print("{} found".format(i))
        break
    else:
        print("{} not found".format(search))