# -*- coding:utf-8 -*-
import urllib2,re,requests,HTMLParser

url='http://daily.zhihu.com/'

def GetHTML(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'}
    # request=urllib2.Request(url,headers=headers)
    # response=urllib2.urlopen(request)
    # return response.read()
    return requests.get(url,headers=headers).text

def GetUrls(html):
    pattern=re.compile('<a href="/story/(.*?)"',re.S)
    items=re.findall(pattern,html)
    urls = [];
    for item in items:
        urls.append(url + 'story/' + item)
        # print urls[-1]
    return urls

def GetContent(url):
    html=GetHTML(url)
    pattern=re.compile('<h1 class="headline-title">(.*?)</h1>')
    titles=re.findall(pattern,html)
    print '***********************'+titles[0]+'*******************************'
    pattern=re.compile(r'<div class="content">\n<p>(.*?)</div>',re.S)
    content=re.findall(pattern,html)
    print content[0]



html=GetHTML(url);
urls=GetUrls(html)
for url in urls:
    try:
        print GetContent(url)
    except Exception,ex:
        print ex
