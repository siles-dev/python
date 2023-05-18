# List
# Basic list declaration
ppl = ["you", "me", "them"]

print("The original list: " + str(ppl))
# List are 0-Indexed
print("The first element in ppl is: " + ppl[0])

# List support range access - excludes last index
print("Get a range 0-1 :" + str(ppl[0:2]))

# List allow negative indexes
# -1 is the last item, -2 is second to last, etc.
print("The last element in ppl is: " + ppl[-1])

# Changing a value
ppl[-1] = "us"
print("Changing the last element gives: " + str(ppl))

# Updating a list - since List are objects they contain methods
# Adding a value at the end
ppl.append("they")
print(ppl)

# Adding a value at an index
ppl.insert(-2, "them")
print(ppl)

# Removing an object value
ppl.remove("them")
print(ppl)

# Removing all items
ppl.clear()
print(ppl)

# Checking if a value exist
ppl.append("I")  # Adding a value for the example
print("i" in ppl)

# Get the length of a list
print(len(ppl))
