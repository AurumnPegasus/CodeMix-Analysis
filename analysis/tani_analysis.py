import matplotlib.pyplot as plt
from pprint import pprint

# gettint the data in
with open('tani_analysed.txt') as f:
    data = f.readlines()

count = 0
details = {
    'AH': [],
    'AE': [],
    'WS': [],
    'WRS': [],
    'CS': [],
    'NP': [],
    'QUOTE': [],
    'IMP': [],
    'RC': [],
    'GREET': [],
    'HKIN': [],
    'EKIN': [],
    'RESP': []
}

# GREET: english start as greeting, rest AH
# RC: jiska/jitne/that clause marking hindi RC in english sentence
# QUOTE: hindi quote in english sentence
# NP: not word swap exactly, but noun-phrase swap
# RESP: sir/maam (only the ones seen)
# EKIN: (bro/mom/dad)/darling
# HKIN: yaar/bhai/bhaiya/mummy/papa/babu/bhaijaan/bhaiyya/dada

for i, sent in enumerate(data):
    if "Analysis: " not in sent or len(sent) == len("Analysis: \n"):
        continue
    count += 1
    for k in details.keys():
        if k in sent: details[k].append((data[i-1], sent))

def plotter(details):
    keys = list(details.keys())
    values = [len(x) for x in details.values()]
    plt.bar(keys, values)
    plt.show()

print("count:", count)
pprint(details)

plotter(details)
