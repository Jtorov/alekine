#!/usr/bin/env python
# coding: utf-8

# ### Conditionals

# In[ ]:


sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
fh = float(sh)
fr = float(sr)
# print(fh, fr)
if fh > 40 :
    # print("Overtime")
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)
    xp = reg + otp
    print(xp)
else:
    # print("Regular")
    xp = fh * fr
    print("Pay: ",xp)


# In[ ]:




