class InstrumentLibrary:
    def __init__(self, pack):
        self.pack = pack
        self.library = {}

    def createinstrument(self, key):
        if not key in self.library.keys():
            self.library[key] = {}

    def populatewords(self, instrument, name):
        words = name.split('-')
        for word in words:
            if word in self.library[instrument].keys():
                self.library[instrument][word] += 1
            else:
                self.library[instrument][word] = 1

    def populate(self):
        for sample in self.pack:
            self.createinstrument(sample.instrument)
            self.populatewords(sample.instrument, sample.basename)

    def sort(self):
        for instrument in self.library.keys():
            sorted_list = SortedList(self.library[instrument])
            sorted_list.sort()
            sorted_list.write()
            confirm = False
            while not confirm:
                words = raw_input('Please list the words that you would want to categorize by: ')
                words = words.split()
                new_dict = {}
                for word in words:
                    new_dict[word] = self.library[instrument][word]
                input_list = SortedList(new_dict)
                input_list.sort()
                count = 0
                for sample in self.pack:
                    if sample.instrument == instrument:
                        for word in input_list.list:
                            if word in sample.basename:
                                count += 1
                                break
                confirm = raw_input('This would categorize ' + str(count) + ' of a possible ' + str(len(self.pack)) + ' samples, press y to confirm: ')
                if confirm == 'y':
                    confirm = True
                else:
                    confirm = False
            for sample in self.pack:
                if sample.instrument == instrument:
                    for word in input_list.list:
                        if word in sample.basename:
                            sample.setsubinstrument(word)
                            break
                    if sample.subinstrument == None:
                        sample.setsubinstrument('other')
