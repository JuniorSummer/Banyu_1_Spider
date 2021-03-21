# -*- coding:UTF-8 -*-
import re
import requests
from bs4 import BeautifulSoup
if __name__ == '__main__':
    #以smalltalk这个单元为例
    #前9个网页用这个
    f = open('D:/伴鱼/spider/eslfast/eslfast_result_1.txt', 'a')
    f.write('Part' + str(1) + '   Small Talk')
    f.write('\n')
    f.close()
    for i in range(1,10):
        base_url='https://www.eslfast.com/robot/topics/smalltalk/smalltalk0'
        #记录这是第几个网页
        f = open('D:/伴鱼/spider/eslfast/eslfast_result_1.txt', 'a')
        f.write('Coversation'+str(i))
        f.write('\n')
        f.write('\n')
        f.close()
        target = base_url+str(i)+'.htm'
        #req中保存了我们获取到信息
        req = requests.get(url=target)
        content=req.text
        #print(content)
        bf = BeautifulSoup(content, 'lxml')
        #使用select，找到对应地址
        data=bf.select('body > div > font > p')
        #print(data)
        data=str(data)
        #去除html符号
        pattern = re.compile(r'<[^>]+>', re.S)
        data = pattern.sub('', data)
        #分别找到A说的话和B说的话
        #*？表示匹配到一个\n就结束，三个括号就代表返回多个括号分别匹配到的结果
        data1 = re.findall(r"(A:)([\s\S]*?)(\n)", data, re.S)  #A说的话
        data2 = re.findall(r"(B:)([\s\S]*?)(\n)", data, re.S)  #B说的话
        #print(data1)
        #print(data2)
        f=open('D:/伴鱼/spider/eslfast/eslfast_result_1.txt','a')
        #因为A可能会多说一句，所以这边直接选择min，只保留对话
        for j in range(min(len(data1),len(data2))):
            f.write(data1[j][1])
            f.write('\t')
            f.write(data2[j][1])
            f.write('\n')
        f.write('\n')
        f.close()

    #后面的网页用这个（由网址格式决定）
    for m in range(10,25):
        base_url='https://www.eslfast.com/robot/topics/smalltalk/smalltalk'
        #记录这是第几个网页
        f = open('D:/伴鱼/spider/eslfast/eslfast_result_1.txt', 'a')
        f.write('Coversation'+str(m))
        f.write('\n')
        f.write('\n')
        f.close()
        target = base_url+str(m)+'.htm'
        #req中保存了我们获取到信息
        req = requests.get(url=target)
        content=req.text
        #print(content)
        bf = BeautifulSoup(content, 'lxml')
        data=bf.select('body > div > font > p')
        #print(data)
        data=str(data)
        #去除html符号
        pattern = re.compile(r'<[^>]+>', re.S)
        data = pattern.sub('', data)
        #分别找到A说的话和B说的话
        #*？表示匹配到一个\n就结束，三个括号就代表返回多个括号分别匹配到的结果
        data1 = re.findall(r"(A:)([\s\S]*?)(\n)", data, re.S)  #A说的话
        data2 = re.findall(r"(B:)([\s\S]*?)(\n)", data, re.S)  #B说的话
        #print(data1)
        #print(data2)
        f=open('D:/伴鱼/spider/eslfast/eslfast_result_1.txt','a')
        for n in range(min(len(data1),len(data2))):
            f.write(data1[n][1])
            f.write('\t')
            f.write(data2[n][1])
            f.write('\n')
        f.write('\n')
        f.close()
        



