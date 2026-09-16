# Loops in Python


 while loop
i = 1
while i <= 5 :
    print('Hello World !',i)
    i += 1


print(i)

# # Print numbers from 5 to 1
i = 5
while i>=1:
    print(i)
    i -= 1

print("Loop ended")


# Practice question :# Print numbers from 1 to 100
i = 1
while i<=100:
    print(i)
    i += 1

print("Loop ended")


# Practice question :# Print numbers from 100 to 1
i = 100
while i>=1:
    print(i)
    i -= 1

print("Loop ended")


# # Practice question :# Print the multiplication table of a  number n.
n = int(input("Enter the table number :"))
i = 1
while i<=10:
    print(n, " x ", i, "=",n*i)
    i += 1

print("Loop ended")

# Practice question :# Print the elements of the  following list using a loop.
list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# traverse
i = 0
while i < len(list):
    print(list[i])
    i += 1

# Search for a number x in this tuple using loop :
# (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36)
x = int(input("enter the number : "))

i = 0 
while i < len(num) :
    if ( num[i] == x) :
        print("FOUND at idx ", i)
        break # break statement is used  to terminate the loop
    else :
        print("finding ..... ")
    i += 1


# break statement
i = 1
while i <= 5 :
    print(i)
    if( i == 3):
        break
    i += 1

#  contiue statement 
# print only odd numbers
i = 1
while i <= 10 :
    if( i%2 == 0):
        i += 1
        continue  # Skip the element
    print(i)
    i += 1



# # print only even numbers
i = 1
while i <= 10 :
    if( i%2 != 0):
        i += 1
        continue  # Skip the element
    print(i)
    i += 1





#  for loop 

# for in lis & tuples 
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for val in num :
    print(val)


# for in string 
str = "appnacollege"
for char in str :
    if ( char == 'o'): 
        print('o found ')
        break
    print(char)
else:
    print("End")


# Print the elements of the following list using a loop :
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for val in list :
    print(val)


# Search for a number x in this tuple using loop : 
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

x = int(input('enter the number : '))

list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 0
for val in list :
    if ( val == x) : 
        print('found x  = ', val, "at index ",idx)
        break
#     else:
#         print("Not Found in the list ",val , "at index ", idx)
#     idx += 1
# else:
#     print("END")
linear search ( this type of searching  called )



# range 
print(range(0, 5))# output : range(0, 5)
seq = range(10)
print(seq[0]) # 0
print(seq[1]) # 1
print(seq[2]) # 2
print(seq[3]) # 3

for i in seq :
    print(i)


for i in range(10): # range(stop)
    print(i)


for i in range(2, 10): # range(start, stop)
    print(i)

# # Print even numbers 
for i in range(2, 10, 2): # range(start, stop, step)
    print(i)


# # Print odd numbers 
for i in range(1, 10, 2): # range(start, stop, step)
    print(i)

# Practice Quesjtion : Print numbers from 1 to 100.
for i in range(1, 101):
    print(i)



# Practice Quesjtion : Print numbers from 100 to 1.
for i in range(100, 0, -1):
    print(i)


# Practice Quesjtion : Print the multiplication table of a number n.
#  by own 
n = int(input('Enter the of table : '))
x = n
i = 1
for n in range(n, n*11, n):
    print(x,"x",i,"=",n)
    i += 1 


#  or by video
n = int(input('Enter the of table : '))

for i in range(1, 11):
    print(n,"x",i,"=",n*i)


pass statement 
for i in range(5):
    pass
print("some useful work")


#  Practice Question : WAP to find the sum of first n numbers. (using while)


# # using while loop :
n = int(input("Enter the number : "))
sum = 0
i = 1
while i <= n :
    sum += i
    i += 1
print("Sum of",n,"number is :",sum)


# # using for loop :
n = int(input("Enter the number : "))
sum = 0

for i in range(1, n+1):
    sum += i

print("Sum of",n,"number is :",sum)


#  Practice Question : WAP to find the factorial of first n numbers. (using for)

# # using while loop :
n = int(input("Enter the number : "))
fact = 1
i = 1
while i <= n :
    fact *= i
    i += 1
print("Factorial of",n,"number is :",fact)


# # using for loop :
n = int(input("Enter the number : "))
fact = 1

for i in range(1, n+1):
    fact *= i

print("Factorial of",n,"number is :",fact)
