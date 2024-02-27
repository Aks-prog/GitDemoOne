# Print all the contents of the text file.
file1 = open('test.txt')
print(file1.read())
file1.close()

# Read n number of characters by passing number.
# Prints only the first 5 characters of the text file.
file2 = open('test.txt')
print(file2.read(5))
file2.close()

# Prints only the first 15 characters of the text file.
file3 = open('test.txt')
print(file3.read(15))
file3.close()

# readline() read one single line at a time.
# Prints the single line of text file because we used readline() method.
file4 = open('test.txt')
print(file4.readline())
file4.close()

# Prints the two lines of text file because we used readline() method two times.
file5 = open('test.txt')
print(file5.readline())
print(file5.readline())
file5.close()

# Prints till read(13) and then continue to print a single line on next line using readline() method.
file6 = open('test.txt')
print(file6.read(13))
print(file6.readline())
file6.close()

# Print all the lines of the text file using readline() method.
file7 = open('test.txt')
line = file7.readline()
while line != "":
    print(line)
    line = file7.readline()
file7.close()

print("-------------------------------------readlines method------------------------------------------------")
file8 = open('test.txt')
for line1 in file8.readlines():
    print(line1)
file8.close()