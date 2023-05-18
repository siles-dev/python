# While loop
max = float(input("Enter a positive number to print up to, starting from 0: "))
cnt = 0

# while {condition}:
#   {statements}
# `:` opens execution block and is based on `   ` tabbed space to group execution statements

while cnt <= max:
    # String multiplication
    print(cnt * "-")
    cnt += 1
