#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


#1.Use the print function to display your full name.
print("Ji won Mok")


# In[ ]:


#2.Create a variable named continent that contains the value “North America”. Print the variable.
continent = "North America"


# In[ ]:


#3.Create a variable named country that contains the value “United States”. Print the variable.
country = "United States"


# In[22]:


#4.Create a variable that contains the US population size: 331,002,651. Print the variable. Next use the type() function on the variable to show its data type.
US_population_size = 331002651
type(US_population_size)
print(type(US_population_size))


# In[24]:


#5.Create a list variable that consists of three US states. Print the variable.
Three_US_states = ["virginia","California","Georgia"]
print(Three_US_states)
#6.Update the list using the append() method to include an additional state. Then print the variable.
Three_US_states.append("Washington")
print(Three_US_states)
#7.Use the list method, sort(), to order the list with four US states. Then print the variable.
Three_US_states.sort()
print(Three_US_states)
#8.Retrieve the third element of the list through indexing.
Three_US_states[2]


# In[12]:


#9.Create a new variable and assigned it the first two elements of the list using the slicing technique and indexing. Then print the variable. 
animals = ["cat" , "dog","deer","fox"]
animals[:2]


# In[15]:


#10.Create a dictionary variable where the key is 'United States' as a string , and the value is a list of four states from problem 6's output. 
#Then print the variable.

United_states = {'Virginia','California','Georgia','Washington'}
United_states


# In[16]:


#11.Create a dictionary variable where the key is a string variable containing the country name from problem 3, 
#and the value is a list variable containing a list of states from problem 5. Then print variable. Note: Since these variables exist, 
#you can refer to them for this problem.

country = {"United States" : ["virgnia","california","georgia","washington"] }
country


# In[21]:


#12.Update the dictionary to include an additional key-value pair where the key is “Name”, and the value is your name. 
#(note: there are two ways to add new items to a dictionary). Then print the variable.

country["Name"] = "Jiwon" 
country


# In[ ]:




