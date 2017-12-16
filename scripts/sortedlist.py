class SortedList:
    def __init__(self, word_dict):
        self.words = word_dict
        self.list = []

    def spliceintolist(self, word, i):
        self.list = self.list[:i] + [word] + self.list[i:]

    def sort(self):
        for word in self.words.keys():
            if not word.isdigit():
                for i in range(len(self.list)):
                    if self.words[word] < self.words[self.list[i]]:
                        self.spliceintolist(word, i)
                        break
                if word not in self.list:
                    self.list.append(word)

    def write(self):
        for word in self.list:
            print(word + ': ' + str(self.words[word]))
