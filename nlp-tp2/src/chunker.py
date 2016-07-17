#!/usr/bin/python


from nltk.tag import pos_tag  
from nltk.tokenize import word_tokenize 
from nltk.chunk.util import tree2conlltags
import nltk.data
chunker = nltk.data.load("chunkers/corpus_ub.pickle")


def main():

  wsjsubset = open("../corpus/wsjsubset", 'r').readlines()
  genia = open("../corpus/genia", 'r').readlines()
  txt_esp1 = open("../corpus/espanol1", 'r').readlines() 
  txt_esp2 = open("../corpus/espanol2", 'r').readlines() 

  words = []
  postag = []
  chunktag = []
  for line in txt_esp1:
    if len(line.split()) > 0:
      words.append(line.split()[0])
      postag.append(line.split()[1])
      chunktag.append(line.split()[2])
  
  postag_nltk = pos_tag(words) 
  chunktag_nltk = tree2conlltags(chunker.parse(postag_nltk))
  print chunktag_nltk
  cant_nominales_nltk = 0
  cant_nominales_gold = 0
  cant_nominales_hit = 0

  for i in xrange(len(chunktag_nltk)):
    if chunktag_nltk[i][2] in ['I-NP', 'B-NP']:
      cant_nominales_nltk += 1
      if chunktag_nltk[i][2] == chunktag[i]:
        cant_nominales_hit += 1
    if chunktag[i] in ['I-NP', 'B-NP']:
      cant_nominales_gold += 1

  precision = cant_nominales_hit / float(cant_nominales_nltk)
  recall = cant_nominales_hit / float(cant_nominales_gold)


  print "Precision: ", precision
  print "Recall: ", recall


if __name__ == '__main__':
  main()