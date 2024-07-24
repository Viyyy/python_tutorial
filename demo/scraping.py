import requests
from bs4 import BeautifulSoup
import pandas as pd

''' requirements:
requests
bs4
pandas
lxml
openpyxl
'''

def make_request(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/88.0.4324.146 Safari/537.36',
    }

    try:
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None

def extract_movies_data(soup):
    movie_list = soup.find(class_='indent').find_all('table')

    movies_data = []
    for item in movie_list:
        tds = item.find_all('td')
        
        img = tds[0].find('a').find('img').get('src')
        title = tds[1].find('a').get('title')
        url = tds[1].find('a').get('href')
        pub = tds[1].find(class_='pl').text
        rating_nums = tds[1].find(class_='rating_nums').text
        inq = tds[1].find(class_='inq').text if tds[1].find(class_='inq') is not None else ''

        print(f'爬取书籍：{title}|{pub}|{rating_nums}')

        movies_data.append({
            '名称': title,
            '图片': img,
            '链接': url,
            '出版社': pub,
            '评分': rating_nums,
            '简介': inq
        })

    df = pd.DataFrame(movies_data)
    return df

def fetch_top_movies_data(page_number):
    url = f'https://book.douban.com/top250?start={page_number * 25}&filter='
    # url = f'https://m.weibo.cn/p/106003type=25&t=3&disable_hot=1&filter_type=realtimehot'
    html = make_request(url)
    # 使用 BeautifulSoup 解析 HTML 内容，解析器为 lxml
    soup = BeautifulSoup(html, 'lxml')
    movies_df = extract_movies_data(soup)
    return movies_df

def main():
    results = (fetch_top_movies_data(i) for i in range(10))
    df = pd.concat(results)
    
    df['评分'] = df['评分'].astype('float')
    df = df.sort_values(by='评分', ascending=False)
    
    df.to_excel('豆瓣top250.xlsx', sheet_name='豆瓣书籍Top250', index=False)
    print('ok')
    
if __name__ == '__main__':
    main()
