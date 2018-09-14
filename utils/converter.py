# coding=utf-8
from __future__ import absolute_import, division, print_function, unicode_literals
 
import os
import sys

#Convert word-segmented corpus into 10-column format for dependency parsing
def conllConverter(inputFilePath):
    with open(inputFilePath) as reader:
        lines = reader.readlines()
    with open(inputFilePath + ".conllu", "w") as writer:
        for line in lines:
            tok = line.strip().split()
            if not tok or line.strip() == '':
                writer.write("\n")
            else:
                count = 0
                for word in tok:
                    count += 1
                    writer.write(str(count) + "\t" + word + "\t" + '\t'.join(['_'] * 8) + "\n")
            writer.write("\n")    

if __name__ == "__main__":
    conllConverter(sys.argv[1])
