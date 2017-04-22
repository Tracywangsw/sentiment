import jieba
import numpy as np
import os

X,Y = [],[]
root_path = 'D:/pyspace/sentiment/'

def get_stop_words(path=root_path+'stop_words.txt'):
  rf = open(path,'r')
  lines = rf.readlines()
  rf.close()
  return set(lines)

stop_words = get_stop_words()
neutral_news,negative_news = [],[]

def load_data(path):
  rf = open(path,'r')
  lines = rf.readlines()
  rf.close()
  for line in lines:
    columns = line.split('~|~')
    polarity,title = columns[0],columns[4]
    words = jieba.cut_words(title)
    words = [w for w in words if w not in stop_words]
    if words:
      if polarity == '0':
        neutral_news.append(' '.join(words))
      elif polarity == '-1':
        negative_news.append(' '.join(words))



def main():
  input_pdf_dir = root_path+'data/'
  for dirname,dirnames,filenames in os.walk(input_pdf_dir):
    for filename in filenames:
      path = os.path.join(dirname,filename)
      load_data(path)

      wf = open(root_path+'negative_news.txt','a+')
      wf.write('\n'.join(negative_news))
      wf.close()

      wf = open(root_path+'neutral_news.txt','a+')
      wf.write('\n'.join(neutral_news))
      wf.close()