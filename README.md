爬虫小试牛刀<br>
============
记录下爬虫所用的程序和遇到的问题，以及解决的方法，方便日后使用<br>

一.程序<br>
------

#### 1.request、bs4方法<br>
eslfast文件夹下保存的是从 https://www.eslfast.com/robot/ （涵盖涵盖了各种生活场景的短对话）爬取对话的程序，后续程序修改不大，故只上传了爬取第一个网页和第二个网页的程序。这两个程序中用到了request和bs库，使用了select的方法来找到网页中对话所在的位置，然后又对网页中无法编码的字符（如：/x93）进行了去除，至此顺利把所有网页上的对话都爬取了下来。其中request和bs库的教程可以参考：<br>
https://www.jianshu.com/p/9c266216957b<br>https://zhuanlan.zhihu.com/p/111123472<br>https://zhuanlan.zhihu.com/p/47035491<br>https://blog.csdn.net/weixin_42105977/article/details/80390957<br>
#### 2.scrapy方法<br>
https://www.runoob.com/w3cnote/scrapy-detail.html<br>
https://www.zhihu.com/column/woodenrobot<br>

二.问题<br>
------

#### 1.关于Python3在保存抓取文件时候遇到的格式问题，解决代码如下：<br>
```python
filename = "teacher.html"
with open(filename, 'w', encoding='utf-8') as f:    
   f.write(response.body.decode())
```
这里需要注意几点：<br>
* open 一定要加上 encoding='utf-8'，否则在 f.write 的时候会报错。<br>
* response.body 返回的是 bytes，需要将其 decode 成 string。<br>

#### 2.关于正则表达式中标点符号的问题：<br>
正则表达式中标点符号基本就是用自己原本的符号来表示，不用进行转义。<br>
其中需要注意的是 . 这个符号，在正则表达式中它表示所有字符，所以英语句号就要考虑非常多的情况（蛮复杂的），可以参考：https://bbs.csdn.net/topics/390737228<br>

#### 3.利用正则表达式去掉乱码字符/提取字符串中的中文字符/提取字符串中的大小写字母：<br>
https://blog.csdn.net/weixin_40683253/article/details/89637064<br>
但有个问题，提取出来的英文字符都在一块，还需要额外分词，所以这种方式感觉更适合中文。<br>

三.github中readme的编写<br>
-------
https://blog.csdn.net/guodongxiaren/article/details/23690801<br>
