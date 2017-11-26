# ai-python-case-WordCloud
Python词云
前提条件
1、安装git
2、安装pycharm
3、生成ssh 参照https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/#platform-windows
github + PyCharm 集成配置参照 https://www.cnblogs.com/feixuelove1009/p/5955332.html
4、安装pip 
5、pip install wordcloud 报错 
building 'wordcloud.query_integral_image' extension、
#找到对应上面部分
error: Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools": http://landinghub.visualstudio.com/visual-cpp-build-tools

解决方案

http://www.lfd.uci.edu/~gohlke/pythonlibs/#wordcloud下载wordcloud对应版本的whl文件wordcloud-1.3.2-cp36-cp36m-win_amd64.whl），
cp后面是python版本，amd64代表64位，
运行
pip install C:\Users\CR\Downloads\wordcloud-1.3.2-cp36-cp36m-win_amd64.whl
参考 http://blog.csdn.net/HHTNAN/article/details/77931782
