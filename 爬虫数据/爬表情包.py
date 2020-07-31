__author__ = '_liky'
 
import requests
from bs4 import BeautifulSoup
import os
 
def getHTMLText(url):
    try:
        kw = {'user-agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=kw, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print('Get HTML Message Successfully')
        return r.text
    except:
        return 'Get HTML Message Error'
 
def ProcessText(text, root):
    soup = BeautifulSoup(text, 'html.parser')
    for link in soup.find_all('img'):
        if str(link['src']).split('.')[-1] == 'jpg' or str(link['src']).split('.')[-1] == 'gif':
            path = root + str(link['src']).split('/')[-1]
            try:
                if not os.path.exists(root):
                    os.mkdir(root)
                if not os.path.exists(path):
                    with open(path, 'wb') as f:
                        f.write(requests.get(link['src']).content) #以二进制的形式写入
                        print('the file ' + str(link['src']).split('/')[-1] + ' has been crawled successfully')
                else:
                    print('the file ' + str(link['src']).split('/')[-1] + ' has existed')
            except:
                print('Process Error')
 
def main():
    print('请勿用于商业用途')
    url = input('URL (exa: https://www.zhihu.com/question/302378021 ')
    root = input('PATH (exa: D://知乎2/新建文件夹): ')
    text = getHTMLText(url)
    ProcessText(text, root)
 
if __name__ == '__main__':
    main()
