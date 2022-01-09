#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().set_next_input('1.What are the two values of the Boolean data type? How do you write them');get_ipython().run_line_magic('pinfo', 'them')
Ans: True 
    False
    it can be interchangable into integer
    we write in int as 0 for False
    1 for True


# In[ ]:


get_ipython().set_next_input('2. What are the three different types of Boolean operators');get_ipython().run_line_magic('pinfo', 'operators')
Ans: three types of Boolean opearators:
        AND , OR , NOT


# In[ ]:


3. Make a list of each Boolean operator's truth tables 
(i.e. every possible combination of Boolean values for the operator and what it evaluate ).

combinations:                                     evaluation
True or True                                       True
True or False                                      True
False or True                                      True
False or False                                     False
True and True                                      True
True and False                                     False
False and True                                     False
False and False                                    False
not(True)                                          False
not(False)                                         True


# In[ ]:


get_ipython().set_next_input('4. What are the values of the following expressions');get_ipython().run_line_magic('pinfo', 'expressions')
(5 > 4) and (3 == 5)    False
not (5 > 4)             False
(5 > 4) or (3 == 5)     True
not ((5 > 4) or (3 == 5)) False
(True and True) and (True == False) False
(not False) or (not True)  True


# In[ ]:


get_ipython().set_next_input('5. What are the six comparison operators');get_ipython().run_line_magic('pinfo', 'operators')
>
<
==
>=
<=
get_ipython().system('=')


# In[ ]:


6. How do you tell the difference between the equal to and assignment operators?Describe a
condition and when you would use one.
Ans: The '=' is the so-called assignment operator and is used to assign the value to the variable on the right side 
    of the operator to the variable on the left side.
    The '==' is the so-called equality comparison operator
    and is used to check whether the two expressions on both sides are equal or not.


# In[ ]:


7. Identify the three blocks in this code:
spam = 0
if spam == 10:
    print('eggs')
    if spam > 5:
        print('bacon')
    else:
        print('ham')
    print('spam')
print('spam')
 the three blocks are:
        print('eggs')
    if spam > 5:
        print('bacon')
    else:
        print('ham')
    print('spam')
        


# In[ ]:


8. Write code that prints Hello if 1 is stored in spam,
prints Howdy if 2 is stored in spam, 
and prints Greetings! if anything else is stored in spam.
Ans:
    spam = int(input())
    if spam == 1:
        print("Hello")
    elif spam == 2:
        print("Howdy")
    else:
        print("Greetings!")


# In[ ]:


get_ipython().set_next_input('9.If your programme is stuck in an endless loop, what keys you’ll press');get_ipython().run_line_magic('pinfo', 'press')
Ans: Ctrl+C


# In[ ]:


get_ipython().set_next_input('10. How can you tell the difference between break and continue');get_ipython().run_line_magic('pinfo', 'continue')
Ans:  break terminates the loop and causes execution to resume after the loop
      continue causes the next iteration of the loop to run immediately


# In[ ]:


11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?
Ans: No difference it just way writing in a different way


# In[ ]:


12. Write a short program that prints the numbers 1 to 10 using a for loop.
Then write an equivalent program that prints the numbers 1 to 10 using a while loop.
Ans: for i in range(0, 11):
        print(i)
        
    x = 1
while x<=10:
    print(x)
    x = x+1


# In[ ]:


13. If you had a function named bacon() inside a module named spam, 
get_ipython().set_next_input('how would you call it after importing spam');get_ipython().run_line_magic('pinfo', 'spam')
spam.bacon()

