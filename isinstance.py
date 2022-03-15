#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#PART 1
#Create a function without a parameter that prompts the user to enter their age. 
#The function is to also add 10.25 to the input value and return the calculated result. 
#Afterwards, be sure to call the function and enter a value to show the function’s output.


# In[5]:


def user_age():
    age = float(input("Enter your age please."))
    return (age+10.25)

user_age()


# In[ ]:


#PART 1
#Create a function that returns the first five elements of a list with ten float and integer values. 
#Afterwards, call the function by passing in the list.


# In[37]:


def get_values():
    ls = [1,2,3,4,"a","b","3","d","7",9,10,11]
    for x in ls:
        if isinstance (x,(float,int)):
            return(ls[:10])
get_values()


# In[ ]:


#PART1
#Create a function that returns all string elements 
#in the list to lowercase: [“UNIteD sTATES”, “InDIA”, “BRaZIL”, rUSsIA”, “PERU”].
#Call the function by passing in the list as an argument.
#Hint: you will use a for statement inside your user-defined function to iterate on each item in the list.


# In[49]:


def get_strings():
    
    ls = ["UNIteD sTATES","InDIA","BRaZIL","rUSsIA","PERU"]
    for x in range(len(ls)):
           ls[x] = ls[x].lower()         
    print(ls)


# In[50]:


get_strings()


# PART 2
# Create a function that passes in a list variable as an argument. The user-defined function
# should find the maximum and minimum values using python’s built-in functions, then compute their 
# difference to obtain the range value. The function must display the following:
# The list contains __ elements.
# The maximum value is __.
# The minimum value is __.
# The range value is __.
#  
# Then call the function.
# Note: Do not use the numpy package.

# In[52]:


def get_value(list):
    for x in list:
        print (
            "The list contains", list,
            "The maximum value is", max(list),
            "the minimum value is", min(list),
            "The range value is", max(list)-min(list))

list = [1,2,3,4,5,6,7,8,9,10] 

get_value(list)


# PART 3
# Create a function that prompts the user to enter two exam grades that will return the average exam grade.
# Round the result to two decimal places using the round function. Call the function.
#         
# Notes:
# The function should not have a parameter.
# Exam grades may be continuous values (have decimal points).
# Do not enter a zero for any exam grade when calling the function.

# In[76]:


def get_grade():
    exam_grade1 = float(input("Enter your exam_grade"))
    exam_grade2 = float(input("Enter your exam_grade"))
    result = round((exam_grade1 + exam_grade2),2)
    return(result)

get_grade()


# In[ ]:


PART 4
Create a function that accepts one argument. Specifically, the function 
should iterate on a list argument, and if an element is a numeric data type (integer or float), 
then store its value position to a separate list that stores numeric values only. 
If an element is not a numeric data type, then store the value to a separate list that stores 
non-numeric values but uppercase any string value. Use the pseudocode below to guide you on developing the code.
Pseudocode: 
Initialize a list that will store each numeric values
Initialize a list that will store each non-numeric value
Define a function that will pass in one parameter named iterable  
For each element in the enumerated list of confirmed cases:
        If the element is an integer or float (use isinstance):
                Include the number value to the list for numeric values
        Else
If the element is a string (use isinstance):
                        Include the string value in uppercase format to the non-numeric list
Else include the element in the list for non-numeric types
Display the numeric list values
Display the non-numeric list values
Call the function using variable list as an argument confirmed_cases = ['US', 23.3, 'India', 10.9, 'Russia', 4.1, 'Peru', 1.2, {"12/31/2020" : 39.5}]
Notes:
Call the function passing the confirmed_cases variable as an argument.
If you copy and paste the confirmed_cases list, you’ll need to manually renter the quotation symbols
within Jupyter to avoid an error.


# In[ ]:


#Pseudocode: 
#Initialize a list that will store each numeric values
#Initialize a list that will store each non-numeric value
#Define a function that will pass in one parameter named iterable  
#For each element in the enumerated list of confirmed cases:
        #If the element is an integer or float (use isinstance):
                #Include the number value to the list for numeric values
       # Else
#If the element is a string (use isinstance):
                        #Include the string value in uppercase format to the non-numeric list
#Else include the element in the list for non-numeric types
#Display the numeric list values
#list = ['US', 23.3, 'India', 10.9, 'Russia', 4.1, 'Peru', 1.2, {"12/31/2020" : 39.5}]


# In[3]:


ls = ['US', 23.3, 'India', 10.9, 'Russia', 4.1, 'Peru', 1.2, {"12/31/2020" : 39.5}]
numbers = []
strings = []

def pseudocode(*iterable):
    for x in ls:
        if isinstance(x,(int,float)):
            numbers.append(x)
            
        elif isinstance(x,str):
            map(lambda x:x.upper(), strings)
            
        else :
            strings.append(x)

    print(numbers)
    print(strings)


# In[4]:


pseudocode()

