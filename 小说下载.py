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
import urllib
import time
#from multiprocessing.dummy import Pool


hosturl='http://m.biqudao.com'
downdir='/sdcard'
#poolnum=10

#搜索小说
def searchtitle(title):
    url='http://zhannei.baidu.com/cse/search?s=3654077655350271938&q=%s'%urllib.quote(title)
    try:
        h=urllib2.urlopen(url)
        r=h.read()
        h.close()
    except:
        time.sleep(3)
        h=urllib2.urlopen(url)
        r=h.read()
        h.close()
    a=re.findall('<a cpos="title" href="(.*?)" title="(.*?)" class="result-game-item-title-link" target="_blank">',r)[0]
    titleurl=a[0]
    titlename=a[1]
    description=re.findall('<p class="result-game-item-desc">(.*?)</p>',r,re.S)[0]
    author=re.findall('作者：</span>.*?<span>(.*?)</span>',r,re.S)[0].strip()
    updatetime=re.findall('更新时间：.*?<span class="result-game-item-info-tag-title">(.*?)</span>',r,re.S)[0].strip()
    lastchapter=re.findall('最新章节：.*?class="result-game-item-info-tag-item" target="_blank">(.*?)</a>',r,re.S)[0].strip()
    if status:
        print '正在更新%s/%s.txt...'%(downdir,title)
    else:
        print description
        print '\n书名: %s\n作者: %s\n更新时间: %s\n最新章节: %s\n'%(titlename,author,updatetime,lastchapter)
        raw_input('确认请回车，否则请挂机:)')
        print '正在下载%s/%s.txt...'%(downdir,title)
    chapterurl=titleurl.replace('www','m')+'all.html'
    return chapterurl

#获取章节列表
def getlist(url):
    h=urllib2.urlopen(url)
    html=h.read()
    h.close()
    al=[]
    a=re.findall('<p> <a style="" href="(.*?)">(.*?)</a></p>',html)
    for i in a:
        if i[1] not in rload:
            al.append(i)
    return al

#获取章节正文
def getbody(i):
    url,chapter=i
    url=hosturl+'/'+url
    h=urllib2.urlopen(url)
    r=h.read()
    h.close()
    a=re.findall('</a></p>.*?\n<p ',r)[0]
    a2=a.replace('</a></p>','')
    a3=a2.replace('<p ','')
    a4=a3.replace('<br/>','\n')
    a5=a4.replace('&nbsp;',' ')
    dwrite(chapter,a5)

#写入文本
def dwrite(chapter,text):
    f.write('%s\n%s\n\n\n\n'%(chapter,text))
    f.flush()
    print chapter

if __name__=='__main__':
    title=raw_input('请输入书名: ')
    #title='遮天'
    status=os.path.exists('%s/%s.txt'%(downdir,title))
    if status:
        with open('%s/%s.txt'%(downdir,title)) as f1:
            rload=f1.read()
    else:
        rload=''
    #pool=Pool(poolnum)
    f=open('/sdcard/%s.txt'%title,'a+')
    try:
        l=getlist(searchtitle(title))
        map(getbody,l)
    except Exception as e:
        print '\n发生异常:\n%s\n已保存进度，请重新运行'%e
        exit()
    finally:
        f.close()
        