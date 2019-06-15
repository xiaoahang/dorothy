import os

# hanlp 的rootpath
root_path = '/Users/weihangzhang/code/dl-nlp/hanlp/'
# hanlp的jar包名称
jar_name = 'hanlp-1.7.3.jar'
#
djclass_path = "-Djava.class.path=" + root_path + os.sep + jar_name + ":" + root_path
