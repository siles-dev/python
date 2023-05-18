# Arithmetic Operations
# Follow PEMDAS order of operation
x = 3
y = 9

# Addition: +
print('Addition of x:', x, 'plus y:', y, 'is: ', x + y)

# Subtraction: -
print('Subtraction of x:', x, 'minus y:', y, 'is: ', x - y)

# Multiplication: *
print('Multiplication of x:', x, 'times y:', y, 'is: ', x * y)

# Division: /
print('Division of x:', x, 'divide y:', y, 'is: ', x / y)

# Special case for division - `//` return the integer value of the operation
print('Int return of result for of x:', x, 'divide y:', y, 'is: ', x // y)

# Mod - `%` returns remainder of the division
print('Mod of x:', x, 'mod y:', y, 'is: ', x % y)

# Exponent - `**`
print('Exponential powers of x:', x, 'to the power of y:', y, 'is: ', x ** y)

# Augmented expression
# Normal:  x = x + 3
# Can be used with all operators
# Augmented statement
x += y
print('Augmented addition of x + y expressed as `x += y`, makes x equal', x)
