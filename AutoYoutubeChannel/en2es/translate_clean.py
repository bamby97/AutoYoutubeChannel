#!/usr/bin/env python
# coding: utf-8

# In[2]:


import translators as ts

# In[3]:


def translateToSpanish(text):
    result = ts.google(text,'en','es')
    return result


# In[ ]:


def separateByLines(text, charsInLine):
    clearLines=[]
    index=0
    if(text.find('\n')!=-1):
        lines=text.split('\n')
        for line in lines:
            if(len(line)<charsInLine):
                clearLines.append(line)
            else:
                line.replace('\n','')
                sublines=[line[i:i+charsInLine] for i in range(0, len(line), charsInLine)]
                clearLines.extend(sublines)
        index+=1
    else:
        clearLines=[text[i:i+charsInLine] for i in range(0, len(text), charsInLine)]
    return clearLines
    

