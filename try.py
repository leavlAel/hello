import streamlit as st

# 设置页面标题
st.title("我的第一个 Streamlit 应用")

# 添加文本
st.text("欢迎使用 Streamlit！")

st.title("Web爬虫")
st.text_area('', value='在本章中，我们将探索使用 Python 进行网页抓取的基础知识。 Web 抓取是从网站中提取数据的过程。 Python 是一种流行的网络抓取语言，因为它有许多用于此目的的有用库。到本章结束时，您将对使用 Python 进行网页抓取有基本的了解，并能够自己从网站中提取数据', max_chars=None)
st.subheader("基础用法")
st.text("我们用 Requests 和 Beautiful Soup 爬取百度首页的标题和正文内容。")
st.code("""
     import requests
from bs4 import BeautifulSoup

url = 'https://www.baidu.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

title = soup.title.string
content = soup.get_text()

print('Title:', title)
print('Content:', content)



        """)

st.subheader("查找所有标签")
st.code("""
        # 下面语句在Jupyter Notebook环境中运行
!pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup

# 定义URL
url = 'https://www.baidu.com/'

# 发送GET请求并获取响应
response = requests.get(url)

# 根据文本的内容来推测它的编码方式，防止中文乱码输出。
response.encoding = response.apparent_encoding

# 使用BeautifulSoup解析响应文本
soup = BeautifulSoup(response.text, 'html.parser')

# 查找所有段落元素
paragraphs = soup.find_all('p')

# 输出所有段落元素
print(paragraphs)


        """)

st.subheader("案例分析")
st.subheader("爬取二十大正文")
st.code("""
        import requests
from bs4 import BeautifulSoup

# 定义URL
url = 'https://www.gov.cn/xinwen/2022-10/25/content_5721685.htm'

# 发送GET请求并获取响应
response = requests.get(url)

# 确定编码
encoding = response.encoding if 'charset' in response.headers.get('content-type', '').lower() else None

# 使用BeautifulSoup解析响应文本
soup = BeautifulSoup(response.content, 'html.parser', from_encoding=encoding)

# 查找ID为"UCAP-CONTENT"的DIV
div = soup.find('div', {'id': 'UCAP-CONTENT'})

# 获取DIV中的文本内容
content = div.text
# print(content)
# 将内容保存为文本文件
with open('content.txt', 'w', encoding='utf-8') as f:
    f.write(content)

        """)