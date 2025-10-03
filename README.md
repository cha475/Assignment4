# Assignment4

Task1.py
-------

Code used
-------
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



Execution
---------
python Task1.py

Ouput
-----
# Reading a file sample.txt which exists
Reading file content
Line1: I love my country
Line2: I love my Mom

# Reading a file sample1,txt which does not exist to demonstrate exception handling

The file was not found.
The file sample1.txt was not found




Task2.py
------
Code used
-------

Capital = input("What is the capital of India ?")


with open("output.txt","w") as file:
    file.write(Capital + "\n")

with open("output.txt","a") as file:
    file.write(f"{Capital} city is the most populous city in India.\n")

with open("output.txt","r") as file:
    content = file.read()
    print(content)


Execeution:
--------

 python Task2.py



 Output
 ----

What is the capital of India ?India
India
India city is the most populous city in India.
