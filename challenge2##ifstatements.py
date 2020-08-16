#!/usr/bin/env python
# coding: utf-8

# In[1]:


###GENERAL SYNTAX OFIF STATREMENTS


# In[2]:


num1=1
if num1>10:
    print("this is over 10")
elif num1==10:
    print("this is equal to 10")
else:
    print("this is under 10")
    


# In[3]:


num=50
if num<=10:
    if num>=100:
        print("this is between 10 and 100")
    else:
        print("this is over 100")
else:
        print("this is under 10")


# In[4]:


text=priyana
te=str.lower(text)
print(te)


# In[ ]:


num=int(input("enter a number between 10 and 20:"))
if num>=10 and num <=20:
    print("thankyou")
else:
    print("out of range")


# In[ ]:


###012 
 Ask for two numbers. 
    If the first one is larger than the second, 
    display the second number first and 
    then the first number, otherwise show the first number first 
    and then the second


# In[ ]:


num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
if num1>num2:
    print(num2,num1)
else:
    print(num1,num2)


# In[ ]:


##013 
 Ask the user to enter a number that is under 20.
    
If they enter a number that is 20 or more, 
display the message “Too high”, 
otherwise display “Thank you”. 


# In[ ]:


num=int(input("entera number that is under 20"))
if num>=20:
    print("to high")
else:
    print("thankyouo")


# In[ ]:


###014 
 Ask the user to enter a number between 10 and 20 
(inclusive). 
If they enter a number within this range, 
display the message “Thank you”, otherwise 
display the message “Incorrect answer”. 


# In[ ]:


numb=int(input("enter the number between 10 and 20"))
if num>=10 and num<=20:
    print("thankyou")
else:
    print("incorrect answer")


# In[ ]:


####015 
 Ask the user to enter their favourite colour.
    If they enter “red”, “RED” or “Red”
    display the message “I like red too”, 
    otherwise display the message 
    “I don’t like [colour],
    I prefer red”. 


# In[ ]:


color=input("enter the favorite colour")
if color=="RED" or color=="red" or color=="Red":
    print("i like red too")
Else:
print("i dont like color,i prefer red")


# In[ ]:


color=input("enter the favorite colour")
if color=="RED" or color=="red" or color=="Red":
    print("i like red too")
else:
    print("i dont like color,i prefer red")


# In[ ]:


##Ask the user if it is raining and 
#convert their answer to lower case 
#so it doesn’t matter what case they type it in.
#If they answer “yes”, ask if it is windy. 
#If they answer “yes” to this second question,
#display the answer “It is too windy for an umbrella”, 
#otherwise display the message “Take an umbrella”.
#If they did not answer yes to the first question,
#display the answer “Enjoy your day”. 


# In[ ]:


user=input("is it raining?")


# In[ ]:


user=str.lower(user)
print(user)


# In[ ]:


user=input("is it raining?")
user=str.lower(user)
if user=="yes":
    windy=input("isit windy")
    if windy=="yes":
        print("it is too windy for an umbrella")
    else:
        print("take your umberalla")
else:
    print("enjoy yor day")


# In[ ]:


##Ask the user’s age. If they are 18 or over, 
display the message “You can vote”, 
if they are aged 17,
display the message “You can learn to drive”, 
if they are 16, display the message 
“You can buy a lottery ticket”, if they are under 16,
display the message “You can go Trickor-Treating


# In[6]:


age=int(input("what is your age?"))
if age>=18:
    print("you can vote")
elif age==17:
    print("you can learn to drive")
elif age==16:
    print("you can buy lottery")
else:
    print("you can go trickor-treatin")


# In[ ]:


#Ask the user to enter a number. 
If it is under 10, display the message “Too low”
if("their", "number", "is", "between", "10", "and", "20,")
display “Correct”, otherwise display “Too high”.


# In[9]:


user=int(input("enter a number"))
if user<10:
    print("to low")
if user>=10 and user<=20:
    print("correct")
else:
    print("too high")


# In[ ]:


###Ask the user to enter 1, 2 or 3.
If they enter a 1, display the message “Thank you”, 
if they enter a 2, display “Well done”, 
if they enter a 3, display “Correct”.
If they enter anything else, display “Error message”.


# In[10]:


user=int(input("enter number 1 or 2 or 3"))
if user==1:
    print("thankyou")
elif user==2:
    print("welldone")
elif user==3:
    print("correct")
else:
    print("error message")


# In[ ]:




