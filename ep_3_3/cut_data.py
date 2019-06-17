# -*- coding=utf8 -*-
import jieba
import re
from tokenizer import cut_hanlp

# jieba.suggest_freq('台中', True)  # 保证台中这个词不会被切开

# 加载字典处理
# jieba.load_userdict("dict.txt")
# fp = open('dict.txt', 'r', encoding='utf-8')
# for line in fp:
#     line = line.strip()
#     jieba.suggest_freq(line, True)

# 更简单的写法
[jieba.suggest_freq(line.strip(), tune=True) for line in open('dict.txt', 'r', encoding='utf-8')]

if __name__ == "__main__":
    string = "台中正确应该不会被切开。"

    # words = jieba.cut(string,HMM=False)
    words = cut_hanlp(string)
    print(words)
