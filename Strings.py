# Strings
# String are objects which means they contain methods
# Strings are immutable
manipulation_string = 'Python for noobs'

# Make all upper case - NOTE this returns a new string
print('Thr string in all upper case: ' + manipulation_string.upper())

# Finds the location of the first occurrence of the character
# Note strings are 0-Indexed & returns -1 if not found
print('The location of "Py" ', manipulation_string.find('Py'))

# Replace stings
print('Replaced "for": ' + manipulation_string.replace('for', '4'))

# Use of `in` reserved keyword - returns a bool
print('Py' in manipulation_string)
