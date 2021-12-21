#!/usr/bin/env python
# coding: utf-8

# ## FUNCTIONS

# In[7]:


def computepay(hours,rate):
    # print("In computepay", hours, rate)
    if hours > 40 :
        reg = hours * rate
        otp = (hours - 40.0) * (rate * 0.5)
        pay = reg + otp
    else:
        pay = hours * rate
        # print("Returning",pay)
        return pay
xh = input("Enter Hours: ")
xt = input("Enter Rate: ")
fh = float(xh)
fr = float(xt)

xp = computepay(fh,fr)
print("pay",xp)


# In[ ]:




