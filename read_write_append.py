with open("example.txt", "w") as file:
    file.write(input("Write something: "))
with open("example.txt", "a") as file:
    file.write(input("write data to append:"))
with open("example.txt", "r") as file:
    contents = file.read()
    print("File Contents:")
    print(contents)
