#!/usr/bin/env python3
"""
    Function:词云的用法
    Author:xueyf
"""
from wordcloud import WordCloud
import os
cur_path=os.path.dirname(__file__)+"./resource"
with open(os.path.join(cur_path,'love_en.txt'),'r') as fp:
    text=fp.read()
   # print(text)
    #wordcloud=WordCloud().generate(text)
   # wordcloud = WordCloud(background_color='red').generate(text) #自定义颜色
   # wordcloud = WordCloud(background_color='red',max_words=10).generate(text)  # 指定单词个数
    wordcloud = WordCloud(background_color='red', max_words=50,max_font_size=40).generate(text)  # 指定最大字号
    image=wordcloud.to_image()
    image.show();