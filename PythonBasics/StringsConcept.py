str = "RahulShettyAcademy.com "
str1 = "Consulting Firm"
str2 = "RahulShetty"
str3 = "RaahulSetty"
str4 = " Great "

# To check character in string using indexes.
print(str[1]) # a

# To get substring in Python.
print(str[0:5])  # Rahul

# Concatenate two strings.
print(str + str1) # RahulShettyAcademy.com Consulting Firm

# To check one string is present in another string or not.
print(str2 in str) # True
print(str3 in str) # False

# Split the string
var = str.split(".")
print(var)
print(var[0])

# Trim or Strip the string
print(str4.strip()) # Removes whitespaces from both left and right.
print(str4.lstrip()) # Removes whitespace from left side only.
print(str4.rstrip()) # Removes whitespace from right side only.
