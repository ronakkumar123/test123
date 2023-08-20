#!/usr/bin/env python
# coding: utf-8

# # 1. Declare two variables, x and y, and assign them integer values. Swap the values of these variables ut using any temporary variable.

# In[1]:


#beore swap
x = 400
Y = 500

#after swap
x = 500
Y = 400


# In[4]:


x = 400
y = 500
print("x=", y)
print("y=", x)


# # 2. Create a program that calculates the area of a rectangle. Take the length and width as inputs from the user and store them in variables. Calculate and display the area.

# In[22]:


# Get user input for length and width

l = float(input(" Enter the l of the rectangle: "))
b = float(input(" Enter the b of the rectangle: "))

# Calculate the area
a = l * b
# Display and calculated area
print(" The area of the rectangle is:", a)


# # 3. Write a Python program that converts temperatures from Celsius to Fahrenheit. Take the temperature in Celsius as input, store it in a variable, convert it to Fahrenheit, and display the result.

# In[21]:


# Get user input for temperature in Celsius

c = float(input(" Enter the temperature in C: "))

# Convert Celsius to Fahrenheit

f = (c * 9/5) + 32

# Display the converted temperature in Fahrenheit

print("The temperature in Fahrenheit is:", f)


# # 1. Write a Python program that takes a string as input and prints the length of the string.

# In[18]:


# Get user input for a string

d = input("Enter a string: ")

# Calculate and print the length of the string

length = len(d)

print("The length of the string is", length)


# # 2. Create a program that takes a sentence from the user and counts the number of vowels (a, e, i, o, u) in the string.

# In[17]:


# Get user input for a sentence
sentence = input("Enter a sentence: ")

# Initialize a variable to count vowels
g = 0

# Define the set of vowels
vowels = 'aeiouAEIOU'

# Iterate through each character in the sentence
for char in sentence:
    if char in vowels:
        g += 1

# Display the vowel count
print("The number of vowels in the sentence is:", g)


# # 3. Given a string, reverse the order of characters using string slicing and print the reversed string.

# In[3]:


# Get user input for a string

h = input("Enter a string: ")

# Reverse the string using string slicing

i = h[::-1]

# Display the reversed string
print("Reversed string:", i)


# # 4. Write a program that takes a string as input and checks if it is a palindrome (reads the same forwards and backwards).

# In[8]:


# Get user input for a string
input_string = input("Enter a string: ")

# Remove spaces and convert to lowercase for case-insensitive comparison
cleaned_string = input_string.replace(" ", "").lower()

# Reverse the string using string slicing
reversed_string = cleaned_string[::-1]

# Check if the reversed string is the same as the original cleaned string
if cleaned_string == reversed_string:
    print("The input string is a palindrome.")
else:
    print("The input string is not a palindrome.")


# # 5. Create a program that takes a string as input and removes all the spaces from it. Print the modified string without spaces.

# In[9]:


# Get user input for a string
input_string = input("Enter a string: ")

# Remove spaces from the string
modified_string = input_string.replace(" ", "")

# Display the modified string without spaces
print("Modified string:", modified_string)

