# -*-encoding=utf8-*-
from stanfordcorenlp import StanfordCoreNLP
import os

project_base_dir = '/Users/weihangzhang/code/dl-nlp'

nlp = StanfordCoreNLP(r'stanfordnlp', lang='zh')

fin = open(os.path.join(project_base_dir, './ch02/ep_2_4/news.txt'), 'r', encoding='utf8')
fner = open(os.path.join(project_base_dir, './ch02/ep_2_4/ner.txt'), 'w', encoding='utf8')  # 实体
ftag = open(os.path.join(project_base_dir, './ch02/ep_2_4/pos_tag.txt'), 'w', encoding='utf8')  # 词性
for line in fin:
    line = line.strip()
    if len(line) < 1:  # 空行
        continue

    fner.write(" ".join([each[0] + "/" + each[1] for each in nlp.ner(line) if len(each) == 2]) + "\n")
    ftag.write(" ".join([each[0] + "/" + each[1] for each in nlp.pos_tag(line) if len(each) == 2]) + "\n")
fner.close()
ftag.close()
