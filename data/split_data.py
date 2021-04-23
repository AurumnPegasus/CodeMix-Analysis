f = open('shivu_majdoori.txt', 'r')
lines = f.readlines()
f.close()
c = 0
ws = []
ae = []
ah = []
cs = []
temp = ""

x = len('Analysis: ')
z = 0
for line in lines:
    c += 1
    line = line.strip()
    if len(line) == 0:
        continue
    
    if line[:x] == 'Analysis: ':
        category = line[x:]
        if category == 'WS':
            ws.append(temp)
        elif category == 'AE':
            ae.append(temp)
        elif category == 'AH':
            ah.append(temp)
        elif category == 'CS':
            cs.append(temp)
        else:
            print('You made a mistake huh', category)
    else:
        temp = line

print('WS: {}, AE: {}, AH: {}, CS: {}'.format(len(ws), len(ae), len(ah), len(cs)))

def writeOutput(path, text):
    f = open(path, 'w')
    for line in text:
        f.write(line)
        f.write('\n')
        f.write('Analysis: ')
        f.write('\n')
        f.write('\n')

    f.close()

writeOutput('shivu/ws.txt', ws)
writeOutput('shivu/ae.txt', ae)
writeOutput('shivu/ah.txt', ah)
writeOutput('shivu/cs.txt', cs)