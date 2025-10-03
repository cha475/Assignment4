Capital = input("What is the capital of India ?")


with open("output.txt","w") as file:
    file.write(Capital + "\n")

with open("output.txt","a") as file:
    file.write(f"{Capital} city is the most populous city in India.\n")

with open("output.txt","r") as file:
    content = file.read()
    print(content)
    



  