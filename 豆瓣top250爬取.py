import re
from urllib.request import urlopen,Request
from bs4 import BeautifulSoup
num=0
for page in range(10):
    headrs = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' }
    Re = Request('https://movie.douban.com/top250?start={}&filter='.format(page*25),headers=headrs)
    html = urlopen(Re)
    bsobj = BeautifulSoup(html.read(),'lxml')
    titlelist = re.findall('<span class="title">([^\/a-zA-Z]+)</span>',str(bsobj))
    gradeslist = re.findall('<span class="rating_num" property="v:average">(\\d+\.\\d+)</span>',str(bsobj))
    discusslist = re.findall('<span>(\\d+人评价)</span>',str(bsobj))
    goodtalk = re.findall('<span class="inq">(.*?)</span>',str(bsobj))
    for title,grade,discuss,good in zip(titlelist,gradeslist,discusslist,goodtalk):
        num += 1
        with open('C:/users/asus/desktop/电影信息.txt','a',encoding='utf-8') as f:#将信息写入到文件对应路径
            f.write('{}:'.format(num)+'《{}》'.format(title)+' '+'得分:{}'.format(grade)+' '+'评价人数:{}'.format(discuss)+' '+'名句:{}'.format(good)+'\n')
            print("正在爬取第{}部电影信息...".format(num))
