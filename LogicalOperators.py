# Logical operators
value = 10

# And
# All expressions must be true to get a true value
print('Returns `true` if `value` is gt 5 & lt 20, where value =', value, ': ' + str(value > 5 and value < 20))

# Or
# Any expressions must be true to get a true value
print('Returns `true` if `value` is gt 5 | lt 20, where value =', value, ': ' + str(value > 5 or value < 20))

# Not
# Negates(switches) the result value
print('Returns the opposite of: is ` value` gt 5, where value =', value, ': ' + str(not value > 5))
