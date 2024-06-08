
# user input
num=int(input("Enter number: "))

# Define a function to calculate the sum of the current number and its previous number
def Sum(n):
    previous_num=n-1
    total_sum=(n)+(previous_num)
    return total_sum

## Call the function and store the result
new_sum=Sum(num)

# Display the current number, its previous number, and their sum
print("Current number is",num ,"previous num is",num-1,"Sum is",new_sum)



# Sum of the first 10 current and previous number

print("Sum of the first 10 numbers")
previous_num=0

for i in range(1,11):
    tot_sum=previous_num+i
    print("current number is",i,"and previous number is",previous_num,",Sum of these two number is",tot_sum,)
    previous_num = i
