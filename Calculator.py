def add(x,y):
	return x+y
def subract(x,y):
	return x-y
def multiply(x,y):
	return x*y
def divide(x,y):
    if y == 0:
        return "zero Division Error"
    return x/y

print("__Calculator__")
print("Choose The Operation :")
print("1. Add (+) ")
print("2. Subract (-) ")
print("3. Multiply (*) ")
print("4. Divide (/) ")

op = input("Enter the operation (+,-,*,/) : ")
a = float(input("Enter the first number : "))
b = float(input("Enter the second number : "))

if op == '+':
	result = add(a,b)
elif op == '-':
	result = subract(a,b)
elif op == '*':
	result = multiply(a,b)
elif op == '/':
	result = divide(a,b)
else : 
	result = "invalid operation"

print ("Result : " , result)