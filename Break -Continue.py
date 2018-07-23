<<<<<<< HEAD
a=int(input("Enter the first number"))
b=int(input("Enter the first number"))

search= int(input("Enter the search value"))

print("searching for {}".format(search))
for i in range(a,b):
    if i == search:
        print("{} found".format(i))
        break
    else:
=======
a=int(input("Enter the first number"))
b=int(input("Enter the first number"))

search= int(input("Enter the search value"))

print("searching for {}".format(search))
for i in range(a,b):
    if i == search:
        print("{} found".format(i))
        break
    else:
>>>>>>> e8b3798fd86a9f0903ca6b760947418d8938e322
        print("{} not found".format(search))