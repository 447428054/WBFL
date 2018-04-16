#-*- encoding:utf-8 -*-
from __future__ import print_function
import codecs
from textrank4zh import TextRank4Keyword, TextRank4Sentence

# text = codecs.open('../test/doc/05.txt', 'r', 'utf-8').read()
# tr4w = TextRank4Keyword()
#
# tr4w.analyze(text=text, lower=True, window=2)
#
# print( '关键词：' )
# for item in tr4w.get_keywords(5, word_min_len=2):
#     print(item.word, item.weight)
#
# print()
# print( '关键短语：' )
# for phrase in tr4w.get_keyphrases(keywords_num=20, min_occur_num= 2):
#     print(phrase)
#
# tr4s = TextRank4Sentence()
# tr4s.analyze(text=text, lower=True, source = 'all_filters')
#
# print()
# print( '摘要：' )
# for item in tr4s.get_key_sentences(num=3):
#     print(item.index, item.weight, item.sentence)


def finalGet(content,number=5):
    text = content
    tr4w = TextRank4Keyword()
    tr4w.analyze(text=text, lower=True, window=2)
    # 得到五个关键词，能够是用户在列表中通过关键词组来对Note进行辨别
    wordList = []
    for phrase in tr4w.get_keyphrases(keywords_num=20, min_occur_num=2):
        wordList.append(phrase)
    if len(wordList) < number:
        for item in tr4w.get_keywords(number-len(wordList), word_min_len=2):
            wordList.append(item.word)
    print(wordList)
    # 得到一个合起来的摘要
    summary = []
    tr4s = TextRank4Sentence()
    tr4s.analyze(text=text, lower=True, source='all_filters')
    for item in tr4s.get_key_sentences(num=3):
        summary.append(item.sentence)
    print(summary)
    sumText = '。'.join(summary)
    print(sumText)
    return (wordList, sumText)


