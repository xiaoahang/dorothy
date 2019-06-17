# encoding=utf8
import re

from jpype import *
from path_dic import djclass_path

startJVM(getDefaultJVMPath(), djclass_path, "-Xms1g", "-Xmx1g")

Tokenizer = JClass('com.hankcs.hanlp.tokenizer.StandardTokenizer')
keep_pos = "q,qg,qt,qv,s,t,tg,g,gb,gbc,gc,gg,gm,gp,m,mg,Mg,mq,n,an,vn,ude1,nr,ns,nt,nz,nb,nba,nbc,nbp,nf,ng,nh,nhd,o,nz,nx,ntu,nts,nto,nth,ntch,ntcf,ntcb,ntc,nt,nsf,ns,nrj,nrf,nr2,nr1,nr,nnt,nnd,nn,nmc,nm,nl,nit,nis,nic,ni,nhm,nhd"
keep_pos_nouns = set(keep_pos.split(","))
keep_pos_v = "v,vd,vg,vf,vl,vshi,vyou,vx,vi"
keep_pos_v = set(keep_pos_v.split(","))
keep_pos_p = set(['p', 'pbei', 'pba'])
drop_pos_set = set(
    ['xu', 'xx', 'y', 'yg', 'wh', 'wky', 'wkz', 'wp', 'ws', 'wyy', 'wyz', 'wb', 'u', 'ud', 'ude1', 'ude2', 'ude3',
     'udeng', 'udh', 'p', 'rr', 'a', 'rr'])  # 不需要的词性
han_pattern = re.compile(r'[^\dA-Za-z\u3007\u4E00-\u9FCB\uE815-\uE864]+')
HanLP = JClass('com.hankcs.hanlp.HanLP')


def to_string(sentence, return_generator=False):
    if return_generator:
        return (word_pos_item.toString().split('/') for word_pos_item in Tokenizer.segment(sentence))
    else:
        # 得到词和词性
        return [(word_pos_item.toString().split('/')[0], word_pos_item.toString().split('/')[1]) for word_pos_item in
                Tokenizer.segment(sentence)]


def seg_sentences(sentence, with_filter=True, return_generator=False):
    # 把文件读取进来以后，先进行分词
    segs = to_string(sentence, return_generator=return_generator)
    if with_filter:
        g = [word_pos_pair[0] for word_pos_pair in segs if
             len(word_pos_pair) == 2 and word_pos_pair[0] != ' ' and word_pos_pair[1] not in drop_pos_set]
    else:
        g = [word_pos_pair[0] for word_pos_pair in segs if len(word_pos_pair) == 2 and word_pos_pair[0] != ' ']
    return iter(g) if return_generator else g
