# Question: Print numbers from 1 to 5

i = 1

while i <= 5:
    print(i)
    i = i + 1


# Q. Write a Program to  Print All even number between  1 to  50 using a while  loop ? 

i=2
while(i%2==0):
    print(i, end=" ")
    i= i + 2 
    if(i==50):

        break

#Q. Write a program to print sum of 1st  5  natural  number ? 

n = 5 
sum = 0
while (n >=0):
    sum = sum + n
    n = n-1
print("Current sum:", sum , end=" " )

#Q. Write a program to print the table of user input 


table = int(input("Enter the number to print its multiplication table: "))
n=1
while (n <= 10):
    print(table, "*", n, "=", table * n)
    n = n + 1
