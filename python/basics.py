name = 'Mango'
count = 23
price = 500.00
print(name, count, price)
print("Fruit name is :",name)
print("Fruit count is :",count)
print("Fruit price is :",price)
count1 = count
print(count1)
print(type(name))
print(type(count))
print(type(price))
old = False
a = None
print(type(old))
print(type(a))
b = 5
c = 4
sum = c + b
diff = b - c
print(sum, diff)

# # Arithmatic operator

a = 5
b = 3
sum = a + b
diff = a - b
multiply = a * b
division = a / b
integer_division = a // b
remainder = a % b
power = a ** b
print(sum)
print(diff)
print(multiply)
print(division)
print(integer_division)
print(remainder)
print(power)


# # Relational operator

'''a = 50
b = 20'''

print(a == b)#False
print(a != b)#True
print(a < b)#False
print(a > b)#True
print(a <= b)#False
print(a >= b)#True


# #Assignment operator
a += 10
print(a)#60
a -= 10
print(a)#50
a *= 2
print(a)#100
a /= 2
print(a)#50
a **= 2
print(a)#2500
a %= 10
print(a)#0

# #logical operator
print(not False)
print(not True)
print(not(a > b))#False
print(not(a < b))#True

val1 = False
val2 = True

print("AND Operator :",val1 and val2)
print("OR Operator :",(a == b) or (a > b))


# # Type Conversion 
a,b = 1.5,4
sum1 = a+b
print(sum1)


# # Type Casting

a,b = 1,int('2')
sum2 = a+b
print(sum2)


# Input Statement
name = input("enter fruit name :")
count = int(input('enter count  :'))
price = float(input('enter price :'))
print(type(name),name)
print(type(count),count)
print(type(price),price)


# # Practice Question : WAP to input 2 numbers & print thier sum
a = float(input('First number :'))
b = float(input('Second number :'))
sum = a + b
print(sum)


# # # Practice Question : WAP to input side of a square & print its area
a = float(input('Side of square :'))
print('Area of Square : ',a * a)

# # Practice Question : WAP to input 2 floating point numbers & print thier average.
a = float(input('First number :'))
b = float(input('Second number :'))
print('Average = ',(a + b)/2)


# # # Practice Question : WAP to input 2 numbers a & b.
# # #  print True if a is greater than or equal to b.If not print False.
a = float(input('First number :'))
b = float(input('Second number :'))
print(a>=b)

print("hello world")