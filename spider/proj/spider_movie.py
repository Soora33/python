
import re

import pandas as pd
import urllib3
from bs4 import BeautifulSoup

findTitle = re.compile(r'<span class="title">(.*)</span>')
findOther = re.compile(r'<span class="other">(.*)</span>')
findNews = re.compile(r'<p class="">(.*?)</p>', re.S)
findPoint = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
findPeopleNumber = re.compile(r'<span>(.*)</span>')
findGoods = re.compile(r'<span class="inq">(.*)</span>')


url = 'https://movie.douban.com/top250'
finalList = []



def run():
    result = getUrlData(url)
    soup = BeautifulSoup(result, "html.parser")
    movie = soup.find_all('div',class_='item')
    for source in movie:
        data = []
        source = str(source)
        # name
        name = re.findall(findTitle,source)
        if (len(name) == 2):
            data.append(name[0])
            data.append(name[1].replace('/','').strip())
        else:
            data.append(name[0])
            data.append('')

        # other
        other = re.findall(findOther,source)
        data.append(other[0].replace('/','').strip())

        # news
        news = re.findall(findNews,source)[0]
        news = re.sub('<br(\s+)?/>(\s+)?','',news)
        news = re.sub('/','',news)
        data.append(news.replace(u'\xa0',u'').strip())

        # point
        point = re.findall(findPoint,source)
        data.append(point[0])

        # people number
        peopleNumber = re.findall(findPeopleNumber,source)
        data.append(peopleNumber[0])

        # goods
        goods = re.findall(findGoods,source)
        data.append(goods[0])

        finalList.append(data)

    for i in finalList:
        print(i)

    toExcel()

def toExcel():
    col = ('电影名','英文名','其他信息','导演及主演','得分','评价人数','推荐言')
    # pands
    df = pd.DataFrame(finalList)
    df.to_excel('pandas.xlsx',sheet_name= 'SHEET1', index=False, header=col)
    print('pands操作xlsx success')


def getUrlData(url):
    header = createHeaders()
    http = urllib3.PoolManager()
    result = http.request('GET',url,headers=header)
    if result.status != 200:
        return None
    return result.data.decode('utf-8')

def createHeaders():
    header = {"User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 80.0.3987.122  Safari / 537.36"}
    return header

if __name__ == '__main__':
    # 解决显示列行以及自动换行的情况
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_row', None)
    pd.set_option('display.width', None)
    run()
