from pprint import pprint

with open('tani_majdoori.txt') as f:
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

print("count:", count)
pprint(details)
