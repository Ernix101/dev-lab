# python file detection

import os

print("current working directory", os.getcwd())
print("Script location: ", os.path.dirname(os.path.abspath(__file__)))


file_path ="test.txt"

# if os.path.exists(file_path):
#     print(f"The location '{file_path}' exists")
# else:
#     print("That location doesn't exist")



# Get the directory where THIS script lives 
script_dir = os.path.dirname(os.path.abspath(__file__))

#Build path to test.txt in the same folder as the script
file_path = os.path.join(script_dir, "test.txt")

print(f"Looking for file at: {file_path}")

if os.path.exists(file_path):
    print("✅File exists!")

    # Try reading it
    with open(file_path, 'r') as f:
        content = f.read()
        print(f"Content: {content}")
else:
    print("❌File doesn't exist")
    print("\nFiles in this folder: ")
    for item in os.listdir(script_dir):
        print(f"  - {item}")