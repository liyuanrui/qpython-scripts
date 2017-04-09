#coding=utf-8
#qpy:console
#qpy:2

'''
Power By LR
2017-01-28
'''

import os
import re
import urllib2

hosturl='http://m.biqudao.com'


#搜索小说
def searchtitle(title):
    url='http://zhannei.baidu.com/cse/search?s=3654077655350271938&q=%s'%title
    h=urllib2.urlopen(url)
    r=h.read()
    h.close()
    a=re.findall('<a cpos="title" href="(.*?)" title=".*?" class="result-game-item-title-link" target="_blank">',r)[0]
    return a+'all.html'

#获取章节列表
def getlist(html):
    al=[]
    a=re.findall('<p> <a.*?</a></p>',html)
    for i in a:
        i2=i.replace('<p> <a style="" href="','')
        i3=i2.replace('</a></p>','')
        i4=i3.split('">')
        if '第' in i4[1] and '章' in i4[1]:al.append(i4)
    return al

#获取章节正文
def getbody(url):
    url=hosturl+'/'+url
    h=urllib2.urlopen(url)
    r=h.read()
    h.close()
    a=re.findall('</a></p>.*?\n<p ',r)[0]
    a2=a.replace('</a></p>','')
    a3=a2.replace('<p ','')
    a4=a3.replace('<br/>','\n')
    a5=a4.replace('&nbsp;',' ')
    return a5

if __name__=='__main__':
    title=raw_input('请输入书名: ')
    t2=searchtitle(title)
    url=t2.replace('www','m')
    print '正在下载/sdcard/%s.txt'%title
    h=urllib2.urlopen(url)
    r=h.read()
    h.close()
    l=getlist(r)
    f=open('/sdcard/%s.txt'%title,'w')
    for i in l:
        text=getbody(i[0])
        f.write(i[1]+'\n')
        f.write(text+'\n\n\n\n')
        f.flush()
        print i[1]
    f.close()
        