# Welcome to the simple to do list.

todostuff = []
time = []
items = 0

while True:
    todos = input("Enter something you want to do. (q to quit): ")
    if todos == "" or todos == "q":
     print("Please Enter something to do!")
    todos = input("Enter something you want to do. (q to quit): ")
    break
todostuff.append(todos)
print("You want to {todos}")

    