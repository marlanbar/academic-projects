#!/usr/bin/python

from nltk.tag import pos_tag  
from nltk.tokenize import word_tokenize 

def main():

  wsjsubset = open("../corpus/wsjsubset", 'r').readlines()
  genia = open("../corpus/genia", 'r').readlines()

  words = []
  postag = []
  chunktag = []
  for line in wsjsubset:
    if len(line.split()) > 0:
      words.append(line.split()[0])
      postag.append(line.split()[1])
      chunktag.append(line.split()[2])
  
  postag_nltk = pos_tag(words) 
  hits = 0
  fails = {}
  for i in xrange(len(postag_nltk)):
    if postag_nltk[i][1] == postag[i]:
      hits += 1
    else:
      fails[(postag[i], postag_nltk[i][1])] = fails.get((postag[i], postag_nltk[i][1]), 0) + 1

  accuracy = hits/float(len(postag))
  for fail in fails:
    fails[fail] = fails[fail] / float(len(postag) - hits)

  for key, value in fails.iteritems():
    print value, key
  #0.935601663254 wsjsubset
  # 0.793755622353 genia



if __name__ == '__main__':
  main()