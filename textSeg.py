#encoding=utf-8
from __future__ import print_function, unicode_literals
import sys
sys.path.append("../")
import jieba
#jieba.load_userdict("userdict.txt")
import jieba.posseg as pseg

def init():
    jieba.del_word('自定义词')

def seg(text_sent):
    words = jieba.cut(text_sent, cut_all=False)
    return " ".join(words)