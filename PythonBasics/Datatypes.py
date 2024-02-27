# ----------------------------------------------- LIST ----------------------------------------------------------------
# List is Datatype that allows multiple values and can be different Datatypes.
# List is same as array which we used in other programming languages.
# List is written using square brackets "[]" and commas ",".
print("****************************************** LIST *****************************************************")

values = [1, 2 , "Ankit", 4, 5.7]

# Printing the values of list using indexes.
print(values[0]) # Output is 1.
print(values[2]) # Output is Ankit.

# Printing the last value of the list.
print(values[-1]) # Output is 5.7

# Printing the sub-list values of list.
# We use [1:3] but it prints only the value of index 1 and 2 but not 3 which is exclusive.
print(values[1:3]) # Output is 2 and Ankit.

# To insert the values in the list.
values.insert(3, "Singh")
print(values) # Output is [1, 2, "Ankit", "Singh", 4, 5.7].

# To insert the values at the end of the list.
values.append("End")
print(values) # Output is [1, 2, "Ankit", "Singh", 4, 5.7, "End"].

# To update an existing value of the list.
values[2] = "ANKIT"
print(values) # Output is [1, 2, "ANKIT", "Singh", 4, 5.7, "End"].

# To delete a value in the list.
del values[0]
print(values) # Output is [2, "ANKIT", "Singh", 4, 5.7, "End"].

# --------------------------------------------------- TUPLE -----------------------------------------------------------
# Tuple - Same as List Datatype but immutable.
# Immutable means we cannot update tuple after declaring it and it is protected.
# Tuple is written using parentheses "()" and commas ",".

print("****************************************** TUPLE *****************************************************")

val = (1, 2, "Ankit", 4, 5.7)

# Printing the values of tuple using indexes.
print(val[1]) # Output is 2.
print(val[3]) # Output is 4.

# Try to add new value in tuple - Not working.
# val[2] = "ANKIT"       # It gives TypeError: 'tuple' object does not support item assignment.


# ------------------------------------------------ DICTIONARY --------------------------------------------------------
# Dictionary is like Hashmap in Java.
# It is present in key-value pair.
# Dictionary is written using curly braces "{}".

print("**************************************** DICTIONARY **************************************************")

dic = {1: "A", "First_name": "Ankit", "Last_name": "Singh", "Age": 24}

# Printing the values of Dictionary.

print(dic[1]) # Output is A.
print(dic["First_name"]) # Output is Ankit.
print(dic["Age"]) # Output is 24.

# Create Dicstionaries at runtime.
Dictionary = {}

# Add values in Dictionary at runtime.
Dictionary["First_name"] = "Ankit"
Dictionary["Last_name"] = "Singh"
Dictionary["Age"] = 24
print(Dictionary)
