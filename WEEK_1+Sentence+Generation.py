
# coding: utf-8

# In[214]:


decimal_grammar = """
expression =  operator op operator
operator = num op num
num = 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | num num
op = + | - | * | /
"""


# In[215]:


grammar = """
sentence => noun_phrase verb_phrase 
noun_phrase => Article Adj* noun 
Adj* => null | Adj Adj*
verb_phrase => verb noun_phrase
Article => 一个|这个
noun => 女人 | 篮球 | 桌子 | 小猫
verb => 看着 | 坐在 | 听着 |看见
Adj => 蓝色的 | 好看的 | 小小的
"""


# In[216]:


import random


# In[217]:


def parse_grammar(grammar_str, sep='=>'):
    grammar = {}
    for line in grammar_str.split('\n'): 
        line = line.strip()
        if not line: continue
        
        target, rules = line.split(sep)
        
        grammar[target.strip()] = [r.split() for r in rules.split('|')]
    
    return grammar


# In[218]:


grammar1 = parse_grammar(grammar)


# In[219]:


grammar1


# In[220]:


def gene(grammar_parsed, target = 'sentence'):
    if target not in grammar_parsed: return target
    
    
    rules = random.choice(grammar_parsed[target])
    return ''.join(gene(grammar_parsed,target=r) for r in rules if r!= 'null')


# In[221]:


grammar1['sentence']


# In[222]:


gene(grammar1)


# In[223]:


for i in range(20):
    print (gene(parse_grammar(decimal_grammar, sep= '='), target = 'expression'))

