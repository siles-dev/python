# If statements
# Make decisions

awesomeness = float(input("Enter your awesomeness lvl: "))

# `:` opens execution block and is based on `   ` tabbed space to group execution statements
if awesomeness > 99:
    print("WOW you're AWESOME!!!")  # Notice the double quotes ;)
    print("You alright")
# `else` statement
elif 99 > awesomeness > 55:  # lvl is between (55, 98] - notice ex/inclusion parenthesis
    print("You OK?")
else:
    print("Believe in yourself, or not. You do you \\m/")  # Notice how characters are escaped

# The following statement is always execute since it is not indented
print("We're over it")
