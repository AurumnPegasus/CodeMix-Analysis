from pprint import pprint

with open('tani_majdoori.txt') as f:
    data = f.readlines()

count = 0
details = {
    'AH': 0,
    'AE': 0,
    'WS': 0,
    'WRS': 0,
    'CS': 0,
    'NP': 0,
    'QUOTE': 0,
    'IMP': 0,
    'RC': 0,
    'GREET': 0
}

# GREET: english start as greeting, rest AH
# RC: jiska/jitne/that clause marking hindi RC in english sentence
# QUOTE: hindi quote in english sentence
# NP: not word swap exactly, but noun-phrase swap

for sent in data:
    if "Analysis: " not in sent or len(sent) == len("Analysis: \n"):
        continue
    count += 1
    for k in details.keys():
        details[k] += sent.count(k)

print("count:", count)
pprint(details)
print("sum:", sum(details.values()))
