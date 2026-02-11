# -----------Extract phone number----------
#  Sentences to use: Call me at 0712345678 tomorrow
#                    Phone: 0723456789 ask for John
#                    No phone number here
sentence1 = "Call me at 0712345678 tomorrow"
sentence2 = "Phone: 0723456789 ask for John"
sentence3 = "No phone number here"

def extract_phone(text):
    parts = text.split(" ")

    # number = None
    

    for part in parts:
        if part.isdigit() and len(part) == 10:
            
            return part
            
    else:
            return "No number Here or invalid number!"

# print(extract_phone(sentence1))   
# print(extract_phone(sentence2))  
# print(extract_phone(sentence3))  


#3 -------Title Case Name-----------------------------------------
name1 =  "John KAMAU"
name2 =   "Mary wanjiku"
name3 =   "david omondi"

def title_case(name):
    name_parts = name.split(" ")

    names = []
    for part in name_parts:
         titled_part = name.title()
         names.append(titled_part)

         return " ".join(names)

    
# print(title_case(name1))
# print(title_case(name2))
# print(title_case(name3))


#4------------Split Full Name---------------------------------------

nameOne = "John Kamau"
nameTwo = "Mary Wanjiku Muthoni"
nameThree = "David"

def split_name(fullname):
    name_parts = fullname.split(" ")

    if len(name_parts) == 1:
         # Only first name provided, no last name
         return (name_parts[0], "")
    
    first_name = name_parts[0]
    last_name = " ".join(name_parts[1:])   # Everything after first name

    return (first_name, last_name)

# print(split_name(nameOne))
# print(split_name(nameTwo))
# print(split_name(nameThree))



#5------------Validate email address-----------------

def is_valid_email(email):
     if "@" and "." in email:
        return email
     else:
          print("This email is not valid")

email1 = "john@gmail.com"
email2 = "mary.wanjiku@hospital.co.ke"
email3 = "invalidemail.com"
# print(is_valid_email(email1))

#  second way
def is_valid_email2(email):
     if '@' not in email:
          return False
     
     email_parts = email.split('@')

     # Check if second part has a dot
     if '.' in email_parts[1]:
          return True
     else:
          return False
     
# print(is_valid_email2(email2))

# Third way
def is_valid_email3(email):
     if '@' not in email:
          return False
     
     email_parts = email.split('@')

     # One-line check
     return '.' in email_parts[1]

# print(is_valid_email3(email3))
          


#6--------------Extract date from a sentence------------------------------------

def extract_date(text):
     words = text.split(' ')

     for word in words:
          # Check if word contains '-'
          if '-' in word:
            # Split by '-'
            parts = word.split('-')

            # Check if we have 3 parts
            if len(parts) == 3:
                 year, month, day = parts

                 # Check if all the parts are digits and have correct length
                 if (year.isdigit() and len(year) == 4 and 
                     month.isdigit() and len(month) == 2 and
                     day.isdigit() and len(day) == 2):
                      
                      return word     # Found the date!
    # if we finish the loop without finding date
            return "No date found"

sentenceOne = "Appointment on 2025-01-15 at 10am"
sentenceTwo = "Visit scheduled for 2025-12-31"

# print(extract_date(sentenceOne))
# print(extract_date(sentenceTwo))
            

#7--------------Count words in a sentence-----------------------------------------------

def count_words(sentence):
     no_of_words = len(sentence.split(' '))

     return no_of_words

# print(count_words("Hello world, this is a sentence"))

# --------------------Remove extra spaces ------------------------------------------------

def remove_extra_spaces(text):
     return " ".join(text.split())
     

# print(remove_extra_spaces("Hello    world"))



#8  Check if the string is numeric

def is_numeric(text):

     try:
          float(text)     # Try to convert to float
          return True     # If it works, it's numerid
     except ValueError:
          return False     # If it fails, it's Not numeric
# print(is_numeric("36.5"))
# print(is_numeric("chop chop"))


#9 -----------Mask phone number (071*****78)------------------------------------
# string slicing refresher/ recap
phone = "0712345678"
phone[0:3]               # First 3 characters: "071"
phone[:3]                # Same thing

phone[-2:]               # Last 2 characters: "78"
phone[8:10]              # Same thing

phone[3:8]               # Middle characters: "23456"
len(phone[3:8])          # 5 characters

# SOLUTION:
def mask_phone(phone):
     first_three = phone[:3]
     last_two = phone[-2:]

     # Calculate how many characters to mask
     middle_length = len(phone) - 3 - 2  # 10 - 3 -2 = 5

     # Create the mask (5 stars)
     mask = "*" * middle_length

     return first_three + mask + last_two

# Test
# print(mask_phone("0712345678"))
# print(mask_phone("0723456789")) 


#10-----------------Extract initials--------------------------------
def get_initials(full_name):
     parts = full_name.split(" ")

     first_name = parts[0]
     second_name = parts[1]

     first_name_letter = first_name[0]
     second_name_letter = second_name[0]

     return first_name_letter + "." + second_name_letter

# print(get_initials("John Walker"))

# Better version which handles more than 2 names
def get_initials2(full_name):
     parts = full_name.split(" ")

     initials = []
     for part in parts:
          initials.append(part[0].upper() + ".")

     return "".join(initials)

print(get_initials2("William Samoei Ruto"))

