
# coding: utf-8

# In[297]:


BEIJING, CHANGCHUN, ULUMUQI, WUHAN, GUNAGHZOU, SHENZHEN, BANGKOK, SHANGHAI, NEWYORK = """
BEIJING CHANGCHUN ULUMUQI WUHAN GUANGZHOU SHENZHEN BANGKOK SHANGHAI NEWYORK
""".split()


# In[298]:


dictionary ={}


# In[299]:



connection = {
    CHANGCHUN: [BEIJING],
    ULUMUQI: [BEIJING], 
    BEIJING: [ULUMUQI, CHANGCHUN, WUHAN, SHENZHEN, NEWYORK],
    NEWYORK: [BEIJING, SHANGHAI],
    SHANGHAI: [NEWYORK, WUHAN],
    WUHAN: [SHANGHAI, BEIJING, GUNAGHZOU],
    GUNAGHZOU: [WUHAN, BANGKOK],
    SHENZHEN: [WUHAN, BANGKOK],
    BANGKOK: [SHENZHEN, GUNAGHZOU]
}


# In[300]:


import networkx as nx


# In[301]:


get_ipython().magic('matplotlib inline')


# In[302]:


graph = connection


# In[303]:


g = nx.Graph(graph)


# In[304]:


nx.draw(g)


# In[305]:


def nagivator_dfs(start, destination, connection_graph):
    pathes = [start ]
    seen = set()
    
    while pathes:
        froniter = pathes.pop(0)
        
         
        if froniter in seen: continue
            
        successors = connection_graph[froniter]
        print('Standing at {} Looking forward to {}'.format(froniter,successors))
        pathes = successors + pathes
        
        seen.add(froniter)


# In[306]:


nagivator_dfs(0,7,connection_2)


# In[307]:


def nagivator_bfs(start, destination, connection_graph):
    pathes = [start ]
    seen = set()
    
    while pathes:
        froniter = pathes.pop(0)
        
         
        if froniter in seen: continue
            
        successors = connection_graph[froniter]
        print('Standing at {} Looking forward to {}'.format(froniter,successors))
        pathes = pathes + successors
        
        seen.add(froniter)


# In[308]:


nagivator_bfs(BEIJING,SHENZHEN,connection)


# In[309]:


connection_2 = {
    0: [1,5],
    1: [0,2],
    2: [1,3],
    3: [2,4],
    4: [3],
    5: [0,6],
    6: [5,7],
    7: [6]    
}


# In[310]:


nx.draw(nx.Graph(connection_2))


# In[311]:


nagivator_bfs(0,7, connection_2)

