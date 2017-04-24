# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 13:06:34 2017

@author: Administrator
"""

import urllib

import re

i = 0

title = []

author = []

evaluation = []

count = []

link = urllib.parse.quote('悬疑')

while(i<1000):

    page = urllib.request.urlopen('https://book.douban.com/tag/%s?start=%d&type=S' % (link,i))
    
    p = page.read().decode('utf-8')
    
    m1 = re.compile('''a href="https://book.douban.com/subject/\d*/" title="(.*)"''')
    
    t = m1.findall(p)
    
    title.extend(t)
    

    
    m2 = re.compile('''(?s)<div class="pub">([\s\S]+?)</div>''')
    
    a = m2.findall(p)
    
    for j in range(20):
        
        a[j] = a[j].strip().split('/')[0]
    
    author.extend(a)

    
    
    m3 = re.compile('''<span class="rating_nums">(.*)</span>''')
    
    e = m3.findall(p)
    
    evaluation.extend(e)
    
    
    
    m4 = re.compile('''(?s)<span class="pl">(.+?)</span>''')
    
    num = m4.findall(p)
    
    for k in range(20):
        
        num[k] = num[k].strip()
        
    c = num[:20]
    
    count.extend(c)
    
    i += 20


print(len(title),len(author),len(evaluation),len(count))

f = open('suspense.txt','w')

for l in range(1000):

    f.write('%s  %s  %s  %s\n' % (title[l].encode('utf-8'),author[l].encode('utf-8'),evaluation[l].encode('utf-8'),count[l].encode('utf-8')))

f.close()    
    


