# Type conversion
# String to int
some_string = input("Enter a number: ")
# The below statement will fail because of incompatible types, the sum can't be performed
# print('5 + the entered number = ', 5 + some_string)
# Below the above issue is fixed because the input string is correctly converted to perform the sum
print('5 + the entered number = ', 5 + int(some_string))
# String to boolean
some_string_to_be_bool = input("Enter a boolean(True or False) and note that capitalization matters : ")
print(bool(some_string_to_be_bool))
# String to float
# Notice type conversion can be nested with input to store the desired variable type
some_string_to_be_float = float(input("Enter a decimal number : "))
print(some_string_to_be_float)
# Boolean/int/float to String
age = 5
age_1 = str(5.1)
age_bool = False
print('Age is: ' + str(age) + ', ' +age_1 + ', ' + str(age_bool))
