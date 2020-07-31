import re
import requests
import os
import random
hd={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) 98 Safari/537.36'
}
adr='D://知乎2/新建文件夹'
def dowload(i,url):#下载表情包，并命名
     global adr
     if url==None:
         return
     res=requests.get(url,headers=hd)
     if url.find('jpg')!=-1:
         with open(adr+'/zhihu'+str(i)+'.jpg','wb') as f:
             f.write(res.content)
     elif url.find('gif')!=-1:
         with open(adr+'/zhihu'+str(i)+'.gif','wb') as f:
             f.write(res.content)
     else:
         print('error',url)
def gethtml():#解析html信息
     page=requests.get(url='https://www.zhihu.com/question/46508954',headers=hd)
     page.encoding='utf-8'
     pattern=re.compile(r'<figure>.*?(https.*?(?:jpg|gif)).*?</figure>')
     res=pattern.findall(page.text)
     global adr
     if os.path.exists(adr)==False:
         os.mkdir(adr)
     else:
         adr=adr+str(random.randint(1,1000))
     pre,tot=0,len(res)
     for i,url in enumerate(res):
         dowload(i,url)
         rate=int((i+1)/tot*100)
         if rate!=pre:
             pre=rate
             print(str(rate)+'%')
gethtml()
print('图片已保存在'+adr+'目录！')