#!/usr/bin/env python3
#_*_ coding:utf-8 _*_

"""
    Function:词云的用法
    Author:xueyf
"""
from wordcloud import WordCloud
import jieba  #擅长中文处理
import numpy  #遮罩
from PIL import Image  #图片处理
import os
stopwords={"很多":0,"依然":0,"怎么":0,"什么":0,"就是":0,"活着":0,"可能":0,"一个":0,"不是":0,"因为":0,"没有":0,"只是":0,"如果":0,"还是":0,"那些":0,"这是":0}  #噪声词
cur_path=os.path.dirname(__file__)+"./resource"
def chinese_jieba(text):
    wordlist_jieba=jieba.cut(text)
    text_jieba=" ".join(wordlist_jieba)
    return text_jieba #返回分词列表
with open(os.path.join(cur_path,'love_en.txt'),'r') as fp:
    text=fp.read()
    text=chinese_jieba(text);
    mask_pic=numpy.array(Image.open(os.path.join(cur_path,"love.jpg")))
    #print(text)
    wordcloud = WordCloud(background_color='white',font_path="FZLTXIHK.TTF",stopwords=stopwords,mask=mask_pic).generate(text)  # 指定中文 去除噪声词 字体文件需要与py 文件处于同一目录
    image=wordcloud.to_image()
    image.show();