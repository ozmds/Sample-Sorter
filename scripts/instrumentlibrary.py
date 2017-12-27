from sortedlist import SortedList

class InstrumentLibrary:
    def __init__(self, pack, name):
        self.pack = pack
        self.packname = name
        self.library = {}
        self.instrumentpack = {}

    def createinstrument(self, key):
        if not key in self.library.keys():
            self.library[key] = {}
        if not key in self.instrumentpack.keys():
            self.instrumentpack[key] = []

    def populatewords(self, instrument, name):
        words = name.split('-')
        for word in words:
            if word in self.library[instrument].keys():
                self.library[instrument][word] += 1
            else:
                self.library[instrument][word] = 1

    def populate(self):
        for sample in self.pack:
            self.createinstrument(sample["instrument"])
            self.populatewords(sample["instrument"], sample["basename"])
            self.instrumentpack[sample["instrument"]].append(sample)

    def listallwords(self, inst_dict):
        sorted_list = SortedList(inst_dict)
        sorted_list.sort()
        sorted_list.write()

    def listpossibleoptions(self, words, instrument):
        words = words.split()
        possible_options = {}
        for word in words:
            possible_options[word] = self.library[instrument][word]
        possible_options = SortedList(possible_options)
        possible_options.sort()
        return possible_options.getlist()

    def getcount(self, instrument, possible_options):
        count = 0
        for sample in self.instrumentpack[instrument]:
            for word in possible_options:
                if word in sample["basename"]:
                    count += 1
                    break
        return count

    def setconfirm(self, confirm):
        if confirm == 'y':
            confirm = True
        else:
            confirm = False
        return confirm

    def setsubinstrument(self, sample_list, possible_options):
        new_samples = []
        new_dict = {}
        new_dict['other'] = 0
        for sample in sample_list:
            for word in possible_options:
                if word in sample["basename"]:
                    sample["subinstrument"] = word
                    if word in new_dict.keys():
                        new_dict[word] += 1
                    else:
                        new_dict[word] = 1
                    break
            if sample["subinstrument"] == str(None):
                sample["subinstrument"] = 'other'
                new_dict['other'] += 1
            new_samples.append(sample)

        return {'samples': new_samples, 'words': new_dict}

    def sort(self):
        new_pack = []
        new_dict = {}
        new_dict['words'] = {}
        for instrument in self.library.keys():
            new_dict['words'][instrument] = {}
            print self.packname + ': ' + instrument
            self.listallwords(self.library[instrument])
            confirm = False
            while not confirm:
                message = 'Please list the words that you would want to categorize by: '
                words = raw_input(message)
                possible_options = self.listpossibleoptions(words, instrument)
                if len(possible_options) > 7:
                    print 'Sorry that is too many options, please try again.'
                else:
                    count = self.getcount(instrument, possible_options)
                    confirm = raw_input('This would categorize ' + str(count) + ' of a possible ' + str(len(self.instrumentpack[instrument])) + ' samples, press y to confirm: ')
                    confirm = self.setconfirm(confirm)
            sample_list = self.setsubinstrument(self.instrumentpack[instrument], possible_options)
            new_dict['words'][instrument] = sample_list['words']
            new_dict['words'][instrument]['total'] = len(self.instrumentpack[instrument])
            sample_list = sample_list['samples']
            new_pack = new_pack + sample_list
        cont = raw_input('Would you like to continue? Press y to sort next pack: ')
        cont = self.setconfirm(cont)
        new_dict = {'samples': new_pack, 'continue': cont, 'words': new_dict}
        return new_dict
