# Tuples
# Immutable list
# Declaration
immutable_list_tuple = (1,2,3,4,5,5)

# Can't change it's values : `immutable_list_tuple[0] = 9` will fail

# Count method
# Count the number of times an object value exist in the tuple
print("How many times does `5` apper in the tuple: ", immutable_list_tuple.count(5))

# Index method
# Returns the index of the first occurrence an object value exist in the tuple, -1 if not found
print("The index of the first `5` is: ", immutable_list_tuple.index(5))
