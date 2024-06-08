# # First Method
name=input("Enter a name: ")
print("Name you've entered is",name)

size=len(name)

for i in range(0,size-1,2):
    print(name[i])


# second method
name=input("Enter Name: ")
print("The name you've entered is",name)

for i in range(len(name)):
    if i%2==0:
        print(name[i])