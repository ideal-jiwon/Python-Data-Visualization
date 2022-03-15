#!/usr/bin/env python
# coding: utf-8

# $\alpha = \beta$
# 

# x1:N

# In[ ]:





# In[22]:


import numpy as np
import matplotlib.pylab as plt

from sklearn.datasets import load_digits
digits = load_digits()
samples = [0,1,2,3,4,5,6,7]
d = []
for i in range(8):
    d.append(digits.images[samples[i]])
    
plt.figure(figsize=(8,2))
for i in range(8):
    plt.subplot(1,8, i+1)
    plt.imshow(d[i], interpolation='nearest', cmap=plt.cm.bone_r)
    plt.grid(False); plt.xticks([]); plt.yticks([])
    plt.title("image{}".format(i+1))
plt.suptitle("숫자0과 이미지")
plt.tight_layout()
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




