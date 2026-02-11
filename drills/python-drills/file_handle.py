# This is a way to do multiple file actions at a time through practice

file_path = "C:/Users/Administrator/Desktop/names.txt"

# try:
#     with open(file_path, 'r') as f:
#         content = f.read()
#         names_list = content.split('\n')  #Splits by new line
#         names_list = sorted(set(names_list))  #Sort and remove duplicates
#         print(names_list)
# except:
#     print("something went wrong!")


with open(file_path, 'r') as f:
    names_dict = {}
    for line in f:
        line = line.strip()            #Remove whitespace
        name, age = line.split(',')    #Split by a comma
        names_dict[name] = int(age)      # or int(age) if you want age as a number
    
print(names_dict)

with open(r'C:\\Users\\Administrator\\Desktop\\reportONE.txt', 'w') as f:
    for name, age in names_dict.items():
        f.write(f"{name} is {age} years old. \n")

