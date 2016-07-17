#!/usr/bin/env python 

import re
import sys

contractions = {"I'm": "I am", "ain't" : "am not", "can't" : "can not", "won't" : "will not", "don't" : "do not", "wouldn't" : "would not"}
separadores = [".", ","]

def main():
  if len(sys.argv) != 3:
    print "Modo de Uso: python tokenizer.py [Nombre del archivo] [Tipo de salida]"
    print "Tipo de salida:"
    print "A: un archivo con una linea por cada token"
    print "P: una linea por cada token (por pantalla)"
    return

  filename = sys.argv[1]
  with open (filename, "r") as myfile:
    text = myfile.readlines()
  parsed_text = tokenize(text)

  output_mode = sys.argv[2]
  if output_mode == "A":
    f = open(filename + "_tokenized.txt", 'w')
    for line in parsed_text:
      f.write(line + '\n')
    f.close()
  else:
    for line in parsed_text:
      print line


def tokenize(text):
  text = [multiwordReplace(sentence, contractions) for sentence in text]

  parsed_quotes = []  
  for line in text:
    line = re.split("([^\"]*)", line)
    if line == ['', '\n', '']:
      line = ["<PP>"]
    line = map(lambda s: s.strip(), line)    
    parsed_quotes.append(line)
  parsed_quotes = [item for array in parsed_quotes for item in array]
  
  
  # parsed_endlines = []
  # for line in parsed_quotes:
  #   line = re.split("(?<=\w{4,})\.(?=\s)", line)
  #   parsed_endlines.append(line)
  # parsed_endlines = [item for array in parsed_endlines for item in array]    
  # print parsed_endlines

  parsed_hyphen = []
  for line in parsed_quotes:
    line = re.split("([^\s\(]*[\/\-][^\s\)]*)", line)
    parsed_hyphen.append(line)
  parsed_hyphen = [item for array in parsed_hyphen for item in array]


  parsed_blanks = []
  for array in parsed_quotes:
      line_blanks = array.split()
      for word in line_blanks:
        parsed_blanks.append(word)
  return parsed_blanks

def multiwordReplace(text, wordDic):
    """
    take a text and replace words that match a key in a dictionary with
    the associated value, return the changed text
    """
    rc = re.compile('|'.join(map(re.escape, wordDic)))
    def translate(match):
        return wordDic[match.group(0)]
    return rc.sub(translate, text)

if __name__ == '__main__':
  main()
