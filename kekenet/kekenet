# -*- coding:UTF-8 -*-
import re
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    for i in range(1,28):
        f = open('D:/伴鱼/spider/kekenet/kekenet_result.txt', 'a')
        f.write('Part' + str(i))
        f.write('\n')
        f.write('\n')
        f.close()
        url = ['http://m.kekenet.com/menu/200811/57050.shtml',#1
               'http://m.kekenet.com/menu/201206/187884.shtml',#2
               'http://m.kekenet.com/menu/201206/187885.shtml',#3
               'http://m.kekenet.com/menu/201206/187893.shtml',#4
               'http://m.kekenet.com/menu/201206/187894.shtml',#5
               'http://m.kekenet.com/menu/201206/187895.shtml',#6
               'http://m.kekenet.com/menu/201206/187896.shtml',#7
               'http://m.kekenet.com/menu/201206/187898.shtml',#8
               'http://m.kekenet.com/menu/201206/188424.shtml',#9
               'http://m.kekenet.com/menu/201206/188425.shtml',#10
               'http://m.kekenet.com/menu/201206/188426.shtml',#11
               'http://m.kekenet.com/menu/201206/188429.shtml',#13
               'http://m.kekenet.com/menu/201206/188434.shtml',#14
               'http://m.kekenet.com/menu/201206/188435.shtml',#15
               'http://m.kekenet.com/menu/201207/189082.shtml',#16
               'http://m.kekenet.com/menu/201207/189085.shtml',#17
               'http://m.kekenet.com/menu/201207/189086.shtml',#18
               'http://m.kekenet.com/menu/201207/189896.shtml',#20
               'http://m.kekenet.com/menu/201207/189900.shtml',#21
               'http://m.kekenet.com/menu/201207/189902.shtml',#22
               'http://m.kekenet.com/menu/201207/189903.shtml',#23
               'http://m.kekenet.com/menu/201207/189904.shtml',#24
               'http://m.kekenet.com/menu/201207/189906.shtml',#25
               'http://m.kekenet.com/menu/201207/189907.shtml',#26
               'http://m.kekenet.com/menu/201207/189909.shtml',#27
               'http://m.kekenet.com/menu/201207/189918.shtml',#28
               'http://m.kekenet.com/menu/201207/189929.shtml',#29
               ]
        # 记录这是第几个网页
        # req中保存了我们获取到信息
        req = requests.get(url[i-1])
        content = req.text
        content = content.replace('\xe2', '')
        content = content.replace('\x80', '')
        content = content.replace('\x99', '')
        content = content.replace('\xa6', '')
        # print(content)
        bf = BeautifulSoup(content, 'lxml')
        divs = bf.find_all(class_='f-y w hauto')
        #print(divs)
        data = str(divs)
        # 去除html符号
        pattern = re.compile(r'<[^>]+>', re.S)
        data = pattern.sub('', data)
        #print(data)
        data1 = re.findall(r"(A: )([\s\S]*?)(B: )", data, re.S)  # 对话A
        data2 = re.findall(r"(B: )([\s\S]*?)(C: )", data, re.S)  # 对话B
        data3 = re.findall(r"(C: )([\s\S]*?)(D: )", data, re.S)  # 对话C
        data4 = re.findall(r"(D: )([\s\S]*?)(\n)", data, re.S)  # 对话D
        #异常情况1
        if data1==[]:
            data1=re.findall(r"(a: )([\s\S]*?)(b: )", data, re.S)  # 对话a
        if data2==[]:
            data2=re.findall(r"(b: )([\s\S]*?)(c: )", data, re.S)  # 对话b
        if data3==[]:
            data3=re.findall(r"(c: )([\s\S]*?)(d: )", data, re.S)  # 对话c
        if data4==[]:
            data4=re.findall(r"(d: )([\s\S]*?)(\n)", data, re.S)  # 对话d
        # 异常情况2
        if data2==[]:
            data2=re.findall(r"(b: )([\s\S]*?)(c; )", data, re.S)  # 对话b
        if data3==[]:
            data3=re.findall(r"(c; )([\s\S]*?)(d: )", data, re.S)  # 对话c
        #print(data1,data2,data3,data4)
        #print(data1[0][1])
        #data_tuning1= re.findall(r"()([\s\S]*?)[^.?!]+ ?", data1[0][1], re.S)  # 对话A
        #匹配标点符号https://bbs.csdn.net/topics/390737228,第30个网页就是因为是‘a.’所以爬不下来‘.’这个符号不好搞啊
        #print(data_tuning1)
        f = open('D:/伴鱼/spider/kekenet/kekenet_result.txt', 'a')
        f.write(data1[0][1])
        f.write('\n')
        f.write(data2[0][1])
        f.write('\n')
        f.write(data3[0][1])
        f.write('\n')
        f.write(data4[0][1])
        f.write('\n')
        f.write('\n')
        f.close()
