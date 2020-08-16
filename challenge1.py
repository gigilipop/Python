#!/usr/bin/env python
# coding: utf-8

# In[1]:


##challenge 1


# In[2]:


firstname=input("what is your firstname")
print(firstname)


# In[3]:


firstname=input("what is firstname")
surname=input("what is your surname")
print("hello",firstname,surname)


# In[4]:


###Write code that will display the joke 
“What do you call a bear with no teeth?” 
and on the next line display the answer “A gummy bear!”
Try to create it using only one line of code. 


# In[5]:


print("What do you call a bear with no teeth?” \n “A gummy bear!” ")


# In[7]:


##Ask the user to enter three numbers. 
#Add together the first two numbers and
#then multiply this total by the third. 
#Display the answer as The answer is [answer]. 


# In[23]:


num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
answer=num1+num2
print("answer is",answer)


# In[ ]:


##Ask the user to enter three numbers. 
#Add together the first two numbers
#and then multiply this total by the third. 
#Display the answer as The answer is [answer]. 


# In[24]:


num1=int(input("enter 1st number"))  #give int in before so that it takes as values to be added if not it takes and concate the 2 numbers
num2=int(input("enter 2nd number"))
num3=int(input("enter the 3rd number"))
answer=(num1+num2)*num3
print(answer)


# In[ ]:


#Ask how many slices of pizza the user started
with and ask how many slices they have eaten. 
#Work out how many slices they have left and 
#display the answer in a us


# In[26]:


cust=int(input("howmany pizzas you have started with?"))
cust2=int(input("how many slices left"))
cust3=(cust-cust2)
print("total leftover hurray!!!",cust3)


# In[ ]:


###007 
 ##Ask the user for their name and their age.
#Add 1 to their age and display the output [Name] 
#next birthday you will be [new age]. 


# In[10]:


name=input("what is your name")
age=int(input("what is your age"))
find=age+1
print(name,"next birthday you will be",find)


# In[ ]:


#008 
####Ask for the total price of the bill,
#then ask how many diners there are. 
#Divide the total bill by the number of diners and
#show how much each person must pay. 


# In[11]:


billprice=int(input("what is the total price of the bill"))
diners=int(input("how many dinners"))
totalbill=billprice/diners
print("each person have to pay bill of",totalbill)


# In[ ]:


###There are 2,204 pounds in a kilogram.
Ask the user to enter a weight in kilograms 
and convert it to pounds.  


# In[13]:


weight=int(input("enter a weight in kilograms"))
convert=weight*2.204
print(convert)


# In[14]:


##009 
## Write a program that will ask for a number of days
##and then will show how many hours, minutes 
##and seconds are in that number of days. 


# In[18]:


days=int(input("enter the number of days:"))
hours=days*24
minutes=hours*60
seconds=minutes*60
print("In",days,"days there are...")
print(hours,"hours")
print(minutes,"minutes")
print(seconds,"seconds")


# In[17]:


##Task the user to enter a number over 100 
#and then enter a number under 10 and
#tell them how many times the smaller number goes into 
#the larger number 
#in a user-friendly format


# In[27]:


larger=int(input("enter a number over 100"))
smaller=int(input("enter a number under 10"))
answer=larger//smaller
print(smaller," it goes",larger,answer,"times")


# In[ ]:




