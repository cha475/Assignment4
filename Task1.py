# Reading a file sample.txt which exists
with open("sample.txt","r") as file:
    content = file.read()
    print(content)

# Reading a file sample1,txt which does not exist to demonstrate exception handling
try:
    with open("sample1.txt","r") as file:
     content = file.read()
     print(content)
except FileNotFoundError:
    print("The file was not found.")
finally:
    print("The file sample1.txt was not found")




