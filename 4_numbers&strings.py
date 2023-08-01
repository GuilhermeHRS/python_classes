# Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:

import random
#print(random.randrange(1, 10))

# -------------------------------

#convert from int to float:
x = float(1)

#convert from float to int:
y = int(2.8)

#convert from int to complex:
z = complex(1)

# print(x)
# print(y)
# print(z)

# print(type(x))
# print(type(y))
# print(type(z))

# -------------------------------

# To get the length of a string, use the len() function
a = "Hello, World!"
#print(len(a))

# To check if a streeng is present in the text, we can use "IN"
txt1 = "The best things in life are free!"
# print("free" in txt1) -> it'll be "true" like a conditional

txt2 = "The best things in life are free!"
# if "free" in txt2:
#    print("Yes, 'free' is present.")

# Check if "expensive" is NOT present in the following text:

txt3 = "The best things in life are free!"
# print("expensive" not in txt3)

# -------------------------------

#Slicing Strings

# Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
# print(b[2:5])
# print(b[-5:-2])

# -------------------------------

# The upper() method returns the string in upper case
# The lower() method returns the string in lower case
# The strip() method removes any whitespace from the beginning or the end
# The replace() method replaces a string with another string
# The split() method splits the string into substrings if it finds instances of the separator
# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are

a = "Hello, World!"
# print(a.upper()) 
# print(a.lower())
# print(a.strip())
# print(a.replace("o", "J"))
# print(a.split(",")) # returns ['Hello', ' World!']

#----------------------------------

age = 36
txt = "My name is John, and I am {}"
# print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
# print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
# print(myorder.format(quantity, itemno, price))

#-------------------------------
name = "GuIlHerme"

print(name.center())
"""
# STRING METHODS

capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning
"""