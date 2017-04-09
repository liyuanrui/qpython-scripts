#coding=utf-8
#qpy:console
#qpy:2

'''
Python2
by LR
2017-04-09
QPython交流群: 540717901

'''

import urllib
import urllib2
import re
import os


downdir='/sdcard'


hosturl='http://www.560xs.com'



def search(title):
    '''搜索书名'''
    h=urllib2.urlopen('http://lr.cool/pinyin/?ch=%s'%urllib.quote(title))
    title=h.read()
    h.close()
    url=hosturl+'/'+title+'/'
    body=urllib2.urlopen(url)
    read=body.read()
    body.close()
    if '<img src="./images/woody-404.png"/>' in read:
        print '查无此书...'
        exit()
    titlename=re.findall('<meta property="og:title" content="(.*?)"/>',read,re.S)[0]
    author=re.findall('<meta property="og:novel:author" content="(.*?)"/>',read,re.S)[0]
    updatetime=re.findall('<meta property="og:novel:update_time" content="(.*?)"/>',read,re.S)[0]
    latestname=re.findall(' <meta property="og:novel:latest_chapter_name" content="(.*?)"/>',read,re.S)[0]
    description=re.findall('<meta property="og:description" content="(.*?)"/>',read,re.S)[0]
    outer='书名: %s\n作者: %s\n最后更新: %s\n最新章节: %s\n简介: %s\n下载路径: %s\n'%(titlename,author,updatetime,latestname,description,downdir)
    print outer
    if '下载' in msg:raw_input('确认请回车，否则请挂机:)')
    return url


def getchapter(url):
    '''查找章节列表'''
    print msg
    body=urllib2.urlopen(url)
    read=body.read()
    body.close()
    chapterList=re.findall('<dd><a style="" href="(.*?)">(.*?)</a></dd>',read)
    chapterList=[i[0] for i in chapterList if i[1] not in rload]
    return chapterList



def gettext(url):
    '''查找正文'''
    url=hosturl+url
    body=urllib2.urlopen(url)
    read=body.read()
    body.close()
    texttitle=re.findall('<h1>(.*?)</h1>',read)[0]
    text=re.findall('<div id="content">(.*?)<div class="bottem2">',read,re.S)[0]
    text=text.replace('<br/>','\n')
    text=text.replace('\r\n','\n')
    text=text.replace('&nbsp;',' ')
    text=text.replace('\t',' ')
    text=text.replace('<script>chaptererror();</script>','')
    text=text.replace('</div>','')
    print texttitle
    
    return texttitle,text



def writetext(Text):
    '''写入文本'''
    title,text=Text[0],Text[1]
    #with open('%s/%s.txt'%(downdir,tname),'a+') as f:
    #f=open('%s/%s.txt'%(downdir,tname),'a+')
    f4.write('%s\n\n%s\n\n\n'%(title,text))
    f4.flush()



if __name__ == '__main__':
    tname=raw_input('请输入书名: ')
    #tname='遮天'
    if os.path.exists('%s/%s.txt'%(downdir,tname)):
        msg='正在更新%s/%s.txt...'%(downdir,tname)
        with open('%s/%s.txt'%(downdir,tname)) as f:rload=f.read()
        
    else:
        msg='正在下载%s/%s.txt...'%(downdir,tname)
        rload=''

    f4=open('%s/%s.txt'%(downdir,tname),'a+')

    try:
        chapterList=getchapter(search(tname))
        for i in chapterList:
            writetext(gettext(i))
    except Exception,e:
        print '\n发生异常:\n%s\n已保存进度，请重新运行'%e        
    finally:
        f4.close()
        exit()

