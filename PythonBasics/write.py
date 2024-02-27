# read the file and store all the lines in the list.
# reverse the list.
# write the list back to the file.

with open('test2.txt','r') as reader:
    content = reader.readlines()
    print(content) # [anaconda, bat, cat, dog, elephant]
    reversed(content) # [elephant, dog, cat, bat, anaconda]
    with open('test2.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)