爬虫小试牛刀<br>
============
记录下爬虫所用的程序和遇到的问题，以及解决的方法，方便日后使用<br>

1.程序<br>
------

eslfast文件夹下保存的是从 https://www.eslfast.com/robot/ （涵盖涵盖了各种生活场景的短对话）爬取对话的程序，后续程序修改不大，故只上传了爬取第一个网页和第二个网页的程序。这两个程序中用到了request和bs库，使用了select的方法来找到网页中对话所在的位置，然后又对网页中无法编码的字符（如：/x93）进行了去除，至此顺利把所有网页上的对话都爬取了下来。其中request和bs库的教程可以参考：<br>
https://www.jianshu.com/p/9c266216957b<br>https://zhuanlan.zhihu.com/p/111123472<br>https://zhuanlan.zhihu.com/p/47035491<br>https://blog.csdn.net/weixin_42105977/article/details/80390957<br>

2.问题<br>
------

* 1.关于Python3在保存抓取文件时候遇到的格式问题，解决代码如下：<br>
```python
filename = "teacher.html"
with open(filename, 'w', encoding='utf-8') as f:    
   f.write(response.body.decode())
```
这里需要注意几点：
* open 一定要加上 encoding='utf-8'，否则在 f.write 的时候会报错。
* response.body 返回的是 bytes，需要将其 decode 成 string。
