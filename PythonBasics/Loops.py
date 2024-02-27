# -------------------------------------------- IF-ELSE condition ---------------------------------------------------
# IF is not a loop, it is a condition.

print("**************************************** IF-ELSE condition **********************************************")

greeting = "Good Morning"
a = 4

if greeting == "Good Morning":
    print("Condition matches.")
else:
    print("Condition do not match.")

print("if else condition code is completed.")

# In the above code condition matches.

print("*************************************************")

if a > 5:
    print("Condition matches.")
else:
    print("Condition do not match.")

print("if else condition code is completed.")

# In the above code condition doesn't matches.

# ----------------------------------------------- FOR LOOP ------------------------------------------------------

print("******************************************* FOR LOOP ****************************************************")

obj = [2, 3, 5, 7, 9]

# Iterate over each and every value and print it.
for i in obj:
    print(i) # Output is 2  3  5  7  9

print("*************************************************")

# Print the first five Natural Numbers.
# range(i, j) -> i to j-1.
for j in range(1, 6):
    print(j) # Output is 1  2  3  4  5

print("*************************************************")

# Print the sum of first five natural numbers when print is inside for loop.
summation = 0
for k in range(1, 6):
    summation = summation + k
    print(summation) # Output is 1  3  6  10  15.

print("*************************************************")

# Print the sum of first five natural numbers when print is outside for loop.
summing = 0
for m in range(1, 6):
    summing = summing + m

print(summing) # Output is 15.

print("*************************************************")

# Print the values upto range 10 with index difference is 2.
for n in range(1, 10, 2):
    print(n) # Output is 1  3  5  7  9

print("*************************************************")

# Print the values upto range 10 without first argument.
# It starts range by-default from 0.
for o in range(10):
    print(o) # Output is 0  1  2  3  4  5  6  7  8  9

# ----------------------------------------------- WHILE LOOP ------------------------------------------------------

print("******************************************* WHILE LOOP ****************************************************")

# Print the values in infinite loop.

it = 4
#while it > 1:
   # print(it) # Output is 4 in infinite loop.

print("*************************************************")

# Print the values from 4 to 2 in decrement order.

a = 4
while a > 1:
    print(a)
    a = a - 1 # Output is 4  3  2.

print("*************************************************")

# Print the values from 4 to 2 in decrement order and 3 is not printing in the output.

b = 4
while b > 1:
    if b != 3:
        print(b)
    b = b - 1 # Output is 4  2.

print("*************************************************")

# Printing only 4 in the output and then breaks the loop.

c = 4
while c > 1:
    if c == 3:
        break
    print(c)
    c = c - 1

print("*************************************************")

# Printing values from 10 to 4 in decrement order and then breaks the loop.

d = 10
while d > 1:
    if d == 3:
        break
    print(d)
    d = d - 1

print("*************************************************")

# Printing 10 only and then it goes to infinite loop.

#e = 10

#while e > 1:
#    if e == 9:
#        continue
#    if e == 3:
#        break
#    print(e)
#    e = e - 1

print("*************************************************")

# Printing 10 to 4 in the output with skipping 9 and then breaks the loop.

f = 10

while f > 1:
    if f == 9:
        f = f - 1
        continue
    if f == 3:
        break
    print(f)
    f = f - 1