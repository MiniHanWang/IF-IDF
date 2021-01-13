#Author：Mini
#！/usr/bin/env python
import pandas as pd
import numpy as np
import pymysql
import jieba
conn= pymysql.connect(host="127.0.0.1", user="root", passwd="wangmianny111", db="galaxy_macau_ad",charset='utf8')
combine_dict = {}
for line in open("C:/Users/Administrator/Desktop/tripadvisor_gm/tripadvisor_code_python/chinese_sentiment_score/synonyms.txt", "r",encoding='utf-8'):
    seperate_word = line.strip().split(",")
    jieba.suggest_freq(seperate_word, tune=True)  # change the frequency
    #print (seperate_word)
    num = len(seperate_word)
    #print(num)
    for i in range(1, num):
        combine_dict[seperate_word[i]] = seperate_word[0]
        #print (seperate_word[0])
print("loading dic and changing freq finished!")

data=pd.read_csv("C:/Users/Administrator/Desktop/tripadvisor_gm/data_results/result_chinese/tfidf_200.csv",encoding="utf8",header=None,sep=',',names=["word","weight"])
print(data["word"])
corpus=[]
for item in data["word"]:
    if item in corpus:
        pass
    else:
        corpus.append(item)
print(corpus)
for i in range(0,len(data["word"])):
    if data["word"][i] in combine_dict:
       data["word"][i] = combine_dict[data["word"][i]]
    else:
       pass

corpus_1=[]
for word in corpus:
    if word in combine_dict:
        word = combine_dict[word]
        corpus_1.append(word)
    else:
        pass
print(corpus_1)
for i in range(0,len(corpus_1)):
    tfidf=0.00
    for j in range(0,len(data["word"])):
        if data["word"][j]==corpus_1[i]:
            tfidf+=float(data["weight"][j])
        else:
            pass
    sql = "insert into tfidf_17(word,weight) values('" + str(corpus_1[i]) + "','" + str(
        tfidf) + "' );"
    conn.query(sql)
    conn.commit()
    print("insert sucess!")
    print(corpus_1[i])
    print(tfidf)
