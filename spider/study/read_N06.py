
import urllib3
from bs4 import BeautifulSoup

import excel

# 定义要获取值的id集合
id_list = ('username','password','email','website','date','time','number','range','color','search','interest',
           'textarea','gender','country','items')

pool = urllib3.PoolManager()

result = []
def get_data(soup):
    data = []
    for id in id_list:
        try:
            if id == 'interest':
                interest_list = soup.find_all('input',{'type':'checkbox','checked':True})
                value = [x['value'] for x in interest_list]
                ','.join(value)
            elif id == 'country':
                value = soup.select('#country option[selected]')[0].getText()
            elif id == 'gender':
                value = soup.find('input',{'type':'radio','checked':True})['value']
            elif id == 'textarea':
                value = soup.select('#textarea')[0].getText()
            elif id == 'search':
                value = soup.select_one('#search')['value']
            elif id == 'range':
                value = soup.select_one('#range')['value']
            elif id == 'color':
                value = soup.select_one('#color')['value']
            elif id == 'items':
                value = soup.select('.items a[class="item active"]')[0].getText()
            else:
                value = soup.select_one(f'#{id}')['value']
            data.append(value)
        except Exception as e:
            data.append(' ')
            print(f'id:{id}发生未知错误！',e)
    result.append(data)
    return result

def ask_url(base_url):
    # file_path = 'n06.html'
    # with open(file_path,'r',encoding='utf-8') as file:
    #     html = file.read()
    # soup = BeautifulSoup(html,"html.parser")

    html = pool.request('GET',base_url,headers={"User-Agent": 'Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 80.0.3987.122  Safari / 537.36'})
    if html.status == 200:
        soup = BeautifulSoup(html.data.decode('utf-8'),'html.parser')
        return soup
    return None

if __name__ == '__main__':
    base_url = 'https://spiderbuf.cn/playground/n06'
    soup = ask_url(base_url)
    data = get_data(soup)
    col = ('username','password','email','website','date','time','number','range','color','search','interest',
           'textarea','gender','country','items')
    excel.to_excel(data,col)
