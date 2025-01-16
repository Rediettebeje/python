print("My age: " + str(12))

# this method of pulling out a particular element from a string is called subscripting
print("welcome"[0])
# integer = whole number
# type function allow us to check the data type of any piece od data, type checking
print(type("hello"))
# type conversion or type casting
print(len("12345"))

# PEMDAS L to R
# Parentheses, Exponents, Multiplication/Division, Addition/Subtraction

print(3 * 3 + 3 / 3 - 3)

bmi = 84 / 1.65 ** 2

print(bmi)
# flooring, removing all the decimal, flooring it to the lowest decimal
print(int(bmi))
# rounding, round up or down depending on  the first decimal no
print(round(bmi))
# round takes two input. the first one is the number you want to round,
# the second is the digits you want to round it
print(round(bmi,2))