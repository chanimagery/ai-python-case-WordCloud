#!/usr/bin/env python3
"""
    Function:词云的用法
    Author:xueyf
"""
import jieba
text="我在美丽的大学城"
alist=jieba.cut(text)
alist_all=jieba.cut(text,cut_all=True)
print("默认模式","/".join(alist))
print("全模式","/".join(alist_all))