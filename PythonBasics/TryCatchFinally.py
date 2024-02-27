# In the below code, it executes the except block.
try:
    with open('filelog.txt','r') as reader:
        reader.read()

except:
    print("Given text file in try block doesn't exist. So, control comes on except block.")

# In the below code, it executes the try block.
try:
    with open('test.txt','r') as reader1:
        print(reader1.read())

except:
    print("Given text file is present in try block. So, control will not execute except block.")

# In the below code, it gives error in console output what Python gives us.
try:
    with open('filelog.txt','r') as reader2:
        reader2.read()

except Exception as e:
    print(e)

# In the below code, it executes the except block and also executes finally keyword..
try:
    with open('filelog.txt','r') as reader3:
        reader3.read()

except Exception as e:
    print("Given text file in try block doesn't exist. So, control comes on except block.")
    print(e)

finally:
    print("It executes the finally block also.")

try:
    with open('test.txt','r') as reader4:
        print(reader4.read())

except:
    print("Given text file is present in try block. So, control will not execute except block.")

finally:
    print("It executes the finally block also.")