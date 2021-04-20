import pandas as pd
import re

df = pd.read_csv('parallel.csv')
x = df['Sentence']



# def cleanLines(lines):
#     clean_lines = []
#     for line in lines:
#         if len(line.split()) < 5: continue

#         nline = re.sub('http[s]:\/\/\S+', '', line)
#         nline = re.sub('@\S+', '', nline)
#         nline = re.sub('\n', '', nline)
#         nline = nline.strip()
#         nline = nline.lower()
#         nline = re.sub('-', ' ', nline)
#         nline = re.sub('\'s', '', nline)
#         nline = re.sub('\'', '', nline)
#         nline = re.sub('\"', '', nline)
#         nline = re.sub('[^a-zA-Z0-9 ]*', '', nline)
#         if len(nline) > 0:
#             clean_lines.append(nline+"\n\n")

#     return clean_lines

def fakecleanLines(lines):
    clean_lines = []
    for line in lines:
        if len(line.split()) < 5: continue
        if len(line) > 0:
            clean_lines.append(line+"\n\n")
    return clean_lines

x = fakecleanLines(x)
with open('shivu_majdoori.txt', 'w+') as f:
    f.writelines(x[:300])

with open('tani_majdoori.txt', 'w+') as f:
    f.writelines(x[300:600])
