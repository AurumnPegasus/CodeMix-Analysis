import json

class toJSON:
    def __init__(self):
        self.twitter = self.readArticle('./data/TwitterData.txt')
        self.facebook = self.readArticle('./data/FacebookData.txt')
        self.whatsapp = self.readArticle('./data/WaData.txt')
        self.json = {}
        self.counter = 0
        self.toJSON(self.twitter)
        self.toJSON(self.whatsapp)
        self.toJSON(self.facebook)
        self.dumpJSON()

    def dumpJSON(self):
        with open('hi_en_dataset.json', 'w') as f:
            json.dump(self.json, f)


    def readArticle(self, path):
        f = open(path, 'r')
        dataset = f.readlines()
        return dataset

    def getInformation(self, line):
        try:
            info = line.split()
            word = info[0]
            lang = info[1]
            pos = info[2]

            return word, lang, pos
        except:
            return None, None, None

    def toJSON(self, dataset):
        sentence = []
        for line in dataset:
            if len(line) == 1:
                self.json[self.counter] = {
                    'sentence': sentence
                }
                self.counter += 1
                sentence = []
            else:
                word, lang, pos = self.getInformation(line)
                if word == None:
                    continue
                word_information = {
                    'word': word,
                    'lang': lang,
                    'pos': pos
                }
                sentence.append(word_information)


x = toJSON()


    