#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import json
import requests

commentURL = 'http://comment5.news.sina.com.cn/page/info?version=1&format=js&\
channel=gn&newsid=comos-{}&\
group=&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=20&jsvar=loader_1491395188566_53913700'

def getCommentCounts(newsurl):

    m = re.search('doc-i(.+).shtml', newsurl)
    newsid = m.group(1)
    comments = requests.get(commentURL.format(newsid))
    jd = json.loads(comments.text.strip('var loader_1491395188566_53913 700='))
    print(jd['result']['count']['total'])
    return jd['result']['count']['total']

news='http://news.sina.com.cn/c/nd/2017-04-05/doc-ifycwymx3892472.shtml'
getCommentCounts(news)