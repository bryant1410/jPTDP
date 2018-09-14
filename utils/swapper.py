# coding=utf-8
from __future__ import absolute_import, division, print_function, unicode_literals

import os
import sys

def swapUPosXPos(inputFilePath):
    with open(inputFilePath) as reader:
        lines = reader.readlines()
    with open(inputFilePath + ".ux2xu", "w") as writer:
        for line in lines:
            tok = line.strip().split('\t')
            if not tok or line.strip() == '':
                writer.write("\n")
            else:
                if line[0] == '#' or '-' in tok[0] or '.' in tok[0]:
                    writer.write(line.strip() + "\n")
                else:
                    if tok[4] != "_":
                        temp = tok[3]
                        tok[3] = tok[4]
                        tok[4] = temp
                    writer.write('\t'.join(['_' if v is None else v for v in tok]) + "\n")

def swapUPosXPos_folder(inputFolderPath):
    for path, subdirs, files in os.walk(inputFolderPath):
        folPath = path.replace("\\", "/") + "/"
        for name in files:
            if name.endswith(".conllu") > 0 or name.endswith(".conll") > 0:
                print(folPath + name)
                with open(folPath + name) as reader
                    lines = reader.readlines()
                with open(folPath + name + ".ux2xu", "w") as writer:
                    for line in lines:
                        tok = line.strip().split('\t')
                        if not tok or line.strip() == '':
                            writer.write("\n")
                        else:
                            if line[0] == '#' or '-' in tok[0] or '.' in tok[0]:
                                writer.write(line.strip() + "\n")
                            else:
                                if tok[4] != "_":
                                    temp = tok[3]
                                    tok[3] = tok[4]
                                    tok[4] = temp
                                writer.write('\t'.join(['_' if v is None else v for v in tok]) + "\n")
    
if __name__ == "__main__":
    #swapUPosXPos_folder("/home/dqnguyen/workspace/UD/UD-conll2017")
    swapUPosXPos(sys.argv[1])
