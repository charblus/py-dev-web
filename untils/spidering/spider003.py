#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from datetime import datetime
from bs4 import BeautifulSoup


def getNewsDetail(newsurl):
    result = {}
    res = requests.get(newsurl)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    # print('政府网站 网站源码',soup)
    result['title']=soup.select('#artibodyTitle')
    result['source']=soup.select('.time-source span a')[0].text
    result['article']=' '.join([p.text.strip() for p in soup.select('#artibody p')[:-1]])

    print(result)


newsUrl = 'http://news.sina.com.cn/c/nd/2017-04-05/doc-ifycwymx3892472.shtml'
getNewsDetail(newsUrl)
