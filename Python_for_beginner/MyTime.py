#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def GetTime (args):
    import time
    t = time.localtime(time.time())
    Y = t.tm_year
    m = t.tm_mon
    d = t.tm_mday
    H = t.tm_hour
    M = t.tm_min
    S = t.tm_sec
    return Y,m,d,H,M,S

