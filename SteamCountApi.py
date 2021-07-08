#!/usr/bin/env python
# coding=utf-8
import requests
from bs4 import BeautifulSoup
import json
import time

headers = {
    'Connection':'close',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
         AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
}  # 模拟浏览器访问

count = 0

'''
每十分钟请求一次数据，以json格式写入文件中
'''
while(1):
    fp = open('steam_count.json', 'w+', encoding='utf-8')
    r = requests.get('https://store.steampowered.com/stats/', headers=headers)
    r.encoding = 'utf-8'
    soup=BeautifulSoup(r.text.encode('utf8', 'ignore'), "lxml")
    gamelist = []
    gameTr=soup.find_all("tr",{"class":"player_count_row"})
    for tr in gameTr:
        singleGameData={}
        span = tr.find_all("span",{"class":"currentServers"})
        singleGameData['currentcount'] = span[0].string
        singleGameData['mostcount'] = span[1].string
        for a in tr.find_all("a",{"class":"gameLink"}):
            singleGameData['gamename'] = a.string
        gamelist.append(singleGameData)
    result = json.dumps(gamelist, separators=(',', ':'))
    fp.write(result)
    fp.close()
    count += 1
    _time = time.asctime(time.localtime(time.time()))
    print(count,'=>',_time)
    time.sleep(600)
    