# -*- coding:UTF-8 -*-
import re
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    for i in range(1,119):
        f = open('D:/伴鱼/spider/hujiang/hujiang_2_result.txt', 'a')
        f.write('Part' + str(i))
        f.write('\n')
        f.write('\n')
        f.close()
        url = ['https://yuer.hujiang.com/yeyingyu/yyky/p230196/',#1
               'https://yuer.hujiang.com/yeyingyu/yyky/p230195/',#2
               'https://yuer.hujiang.com/yeyingyu/yyky/p230194/',#3
               'https://yuer.hujiang.com/yeyingyu/yyky/p230193/',#4
               'https://yuer.hujiang.com/yeyingyu/yyky/p230192/',#5
               'https://yuer.hujiang.com/yeyingyu/yyky/p230191/',#6
               'https://yuer.hujiang.com/yeyingyu/yyky/p229654/',#7
               'https://yuer.hujiang.com/yeyingyu/yyky/p229655/',#8
               'https://yuer.hujiang.com/yeyingyu/yyky/p229684/',#9
               'https://yuer.hujiang.com/yeyingyu/yyky/p229686/',#10
               'https://yuer.hujiang.com/yeyingyu/yyky/p229688/',#11
               'https://yuer.hujiang.com/yeyingyu/yyky/p229689/',#12
               'https://yuer.hujiang.com/yeyingyu/yyky/p229690/',#13
               'https://yuer.hujiang.com/yeyingyu/yyky/p229691/',#14
               'https://yuer.hujiang.com/yeyingyu/yyky/p229692/',#15
               'https://yuer.hujiang.com/yeyingyu/yyky/p229693/',#16
               'https://yuer.hujiang.com/yeyingyu/yyky/p229694/',#17
               'https://yuer.hujiang.com/yeyingyu/yyky/p229695/',#18
               'https://yuer.hujiang.com/yeyingyu/yyky/p229696/',#20
               'https://yuer.hujiang.com/yeyingyu/yyky/p229697/',#21
               'https://yuer.hujiang.com/yeyingyu/yyky/p229698/',#22
               'https://yuer.hujiang.com/yeyingyu/yyky/p229699/',#23
               'https://yuer.hujiang.com/yeyingyu/yyky/p229700/',#24
               'https://yuer.hujiang.com/yeyingyu/yyky/p229701/',#25
               'https://yuer.hujiang.com/yeyingyu/yyky/p229702/',#26
               'https://yuer.hujiang.com/yeyingyu/yyky/p229703/',#27
               'https://yuer.hujiang.com/yeyingyu/yyky/p229704/',#28
               'https://yuer.hujiang.com/yeyingyu/yyky/p229705/',#29
               'https://yuer.hujiang.com/yeyingyu/yyky/p229706/',#30
               'https://yuer.hujiang.com/yeyingyu/yyky/p229707/',#31
               'https://yuer.hujiang.com/yeyingyu/yyky/p229708/',#32
               'https://yuer.hujiang.com/yeyingyu/yyky/p229709/',#33
               'https://yuer.hujiang.com/yeyingyu/yyky/p229710/',#34
               'https://yuer.hujiang.com/yeyingyu/yyky/p229711/',#35
               'https://yuer.hujiang.com/yeyingyu/yyky/p229712/',#36
               'https://yuer.hujiang.com/yeyingyu/yyky/p229713/',#37
               'https://yuer.hujiang.com/yeyingyu/yyky/p229715/',#38
               'https://yuer.hujiang.com/yeyingyu/yyky/p229653/',#39
               'https://yuer.hujiang.com/yeyingyu/yyky/p228739/',#40
               'https://yuer.hujiang.com/yeyingyu/yyky/p228740/',#41
               'https://yuer.hujiang.com/yeyingyu/yyky/p228741/',#42
               'https://yuer.hujiang.com/yeyingyu/yyky/p228742/',#43
               'https://yuer.hujiang.com/yeyingyu/yyky/p228744/',#44
               'https://yuer.hujiang.com/yeyingyu/yyky/p228745/',#45
               'https://yuer.hujiang.com/yeyingyu/yyky/p228746/',#46
               'https://yuer.hujiang.com/yeyingyu/yyky/p228747/',#47
               'https://yuer.hujiang.com/yeyingyu/yyky/p228748/',#48
               'https://yuer.hujiang.com/yeyingyu/yyky/p228749/',#49
               'https://yuer.hujiang.com/yeyingyu/yyky/p228750/',#50
               'https://yuer.hujiang.com/yeyingyu/yyky/p228751/',#51
               'https://yuer.hujiang.com/yeyingyu/yyky/p228752/',#52
               'https://yuer.hujiang.com/yeyingyu/yyky/p228753/',#53
               'https://yuer.hujiang.com/yeyingyu/yyky/p228754/',#54
               'https://yuer.hujiang.com/yeyingyu/yyky/p228755/',#55
               'https://yuer.hujiang.com/yeyingyu/yyky/p228756/',#56
               'https://yuer.hujiang.com/yeyingyu/yyky/p228757/',#57
               'https://yuer.hujiang.com/yeyingyu/yyky/p228758/',#58
               'https://yuer.hujiang.com/yeyingyu/yyky/p228759/',#59
               'https://yuer.hujiang.com/yeyingyu/yyky/p228760/',#60
               'https://yuer.hujiang.com/yeyingyu/yyky/p228761/',#61
               'https://yuer.hujiang.com/yeyingyu/yyky/p228762/',#62
               'https://yuer.hujiang.com/yeyingyu/yyky/p228763/',#63
               'https://yuer.hujiang.com/yeyingyu/yyky/p228764/',#64
               'https://yuer.hujiang.com/yeyingyu/yyky/p228765/',#65
               'https://yuer.hujiang.com/yeyingyu/yyky/p228766/',#66
               'https://yuer.hujiang.com/yeyingyu/yyky/p228767/',#67
               'https://yuer.hujiang.com/yeyingyu/yyky/p228768/',#68
               'https://yuer.hujiang.com/yeyingyu/yyky/p228778/',#69
               'https://yuer.hujiang.com/yeyingyu/yyky/p228770/',#70
               'https://yuer.hujiang.com/yeyingyu/yyky/p228771/',#71
               'https://yuer.hujiang.com/yeyingyu/yyky/p228774/',#72
               'https://yuer.hujiang.com/yeyingyu/yyky/p228777/',#73
               'https://yuer.hujiang.com/yeyingyu/yyky/p228769/',#74
               'https://yuer.hujiang.com/yeyingyu/yyky/p228779/',#75
               'https://yuer.hujiang.com/yeyingyu/yyky/p228780/',#76
               'https://yuer.hujiang.com/yeyingyu/yyky/p228600/',#77
               'https://yuer.hujiang.com/yeyingyu/yyky/p228598/',#78
               'https://yuer.hujiang.com/yeyingyu/yyky/p228595/',#79
               'https://yuer.hujiang.com/yeyingyu/yyky/p228547/',#80
               'https://yuer.hujiang.com/yeyingyu/yyky/p228548/',#81
               'https://yuer.hujiang.com/yeyingyu/yyky/p228550/',#82
               'https://yuer.hujiang.com/yeyingyu/yyky/p228552/',#83
               'https://yuer.hujiang.com/yeyingyu/yyky/p228553/',#84
               'https://yuer.hujiang.com/yeyingyu/yyky/p228554/',#85
               'https://yuer.hujiang.com/yeyingyu/yyky/p228555/',#86
               'https://yuer.hujiang.com/yeyingyu/yyky/p228556/',#87
               'https://yuer.hujiang.com/yeyingyu/yyky/p228557/',#88
               'https://yuer.hujiang.com/yeyingyu/yyky/p228558/',#89
               'https://yuer.hujiang.com/yeyingyu/yyky/p228560/',#90
               'https://yuer.hujiang.com/yeyingyu/yyky/p228562/',#91
               'https://yuer.hujiang.com/yeyingyu/yyky/p228563/',#92
               'https://yuer.hujiang.com/yeyingyu/yyky/p228564/',#93
               'https://yuer.hujiang.com/yeyingyu/yyky/p228568/',#94
               'https://yuer.hujiang.com/yeyingyu/yyky/p228570/',#95
               'https://yuer.hujiang.com/yeyingyu/yyky/p228571/',#96
               'https://yuer.hujiang.com/yeyingyu/yyky/p228572/',#97
               'https://yuer.hujiang.com/yeyingyu/yyky/p228573/',#98
               'https://yuer.hujiang.com/yeyingyu/yyky/p228575/',#99
               'https://yuer.hujiang.com/yeyingyu/yyky/p228577/',#100
               'https://yuer.hujiang.com/yeyingyu/yyky/p228578/',#101
               'https://yuer.hujiang.com/yeyingyu/yyky/p228579/',#102
               'https://yuer.hujiang.com/yeyingyu/yyky/p228592/',#103
               'https://yuer.hujiang.com/yeyingyu/yyky/p228580/',#104
               'https://yuer.hujiang.com/yeyingyu/yyky/p228738/',#105
               'https://yuer.hujiang.com/yeyingyu/yyky/p228581/',#106
               'https://yuer.hujiang.com/yeyingyu/yyky/p228582/',#107
               'https://yuer.hujiang.com/yeyingyu/yyky/p228583/',#108
               'https://yuer.hujiang.com/yeyingyu/yyky/p228585/',#109
               'https://yuer.hujiang.com/yeyingyu/yyky/p228587/',#110
               'https://yuer.hujiang.com/yeyingyu/yyky/p228589/',#111
               'https://yuer.hujiang.com/yeyingyu/yyky/p228590/',#112
               'https://yuer.hujiang.com/yeyingyu/yyky/p228586/',#113
               'https://yuer.hujiang.com/yeyingyu/yyky/p228591/',#114
               'https://yuer.hujiang.com/yeyingyu/yyky/p228546/',#115
               'https://yuer.hujiang.com/yeyingyu/yyky/p228545/',#116
               'https://yuer.hujiang.com/yeyingyu/yyky/p228542/',#117
               'https://yuer.hujiang.com/yeyingyu/yyky/p228303/',#118
               'https://yuer.hujiang.com/yeyingyu/yyky/p228268/',#119
               ]
        # 记录这是第几个网页
        # req中保存了我们获取到信息
        req = requests.get(url[i-1])
        content = req.text
        # print(content)
        bf = BeautifulSoup(content, 'lxml')
        divs = bf.find_all(class_='langs_en')
        # print(divs)
        data = str(divs)
        # 去除html符号
        pattern = re.compile(r'<[^>]+>', re.S)
        data = pattern.sub('', data)
        # print(data)
        result = re.findall(r"(: )([\s\S]*?)(\r)", data, re.S)  # 除最后一句的对话
        # result_last=re.findall(r"(\t)([\s\S]*)(\])", data, re.S) # 最后一句的对话找不到啊，只好放弃。。。
        # print(result)
        for i in range(0, len(result) - 1, 2):
            f = open('D:/伴鱼/spider/hujiang/hujiang_2_result.txt', 'a')
            f.write(result[i][1])
            f.write('\t')
            f.write(result[i + 1][1])
            f.write('\n')
        f.write('\n')
        f.close()
