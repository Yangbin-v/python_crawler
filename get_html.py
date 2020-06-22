import requests
# encoding:utf-8  #默认格式utf-8

def get_html(url): #爬取源码函数
    headers = {
        'User-Agent': 'Mozilla/5.0(Macintosh; Intel Mac OS X 10_11_4)\
        AppleWebKit/537.36(KHTML, like Gecko) Chrome/52 .0.2743. 116 Safari/537.36'

    }  # 模拟浏览器访问
    response = requests.get(url, headers=headers)  # 请求访问网站
    response.encoding = response.apparent_encoding #设置字符编码格式
    html = response.text  # 获取网页源码
    return html  # 返回网页源码

r = get_html('https://www.baidu.com/')
print(r) #打印网页源码