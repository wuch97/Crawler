#导入requests库
import requests
#导入 re 库
import re
#导入相应的库文件
from urllib.request import urlretrieve
#定义请求头，请求头可以使爬虫伪装成浏览器
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
#定义连接网络的url
url = 'https://www.zhihu.com/question/285321190'
#保存文件的路径
path = 'D:/知乎2/新建文件夹/'
 
#函数主体
html = requests.get(url,headers = headers)
imgs = re.findall('''<img class="BDE_Image" src="(.*?)"''',html.text,re.S)
with open('D:/知乎2/新建文件夹/', 'w') as f:
    for img in imgs:
        urlretrieve(img,path+img[-15:])
        f.write(img)
