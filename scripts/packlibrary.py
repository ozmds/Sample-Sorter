import os, os.path, shutil, sys, time, json, copy

from sample import Sample
from instrumentlibrary import InstrumentLibrary
from packreport import PackLibraryReport

class PackLibrary:
    def __init__(self):
        self.packs = {}
        self.sourcepath = os.path.abspath('../source files')
        self.destpath = os.path.abspath('../sorted files')

    def addsample(self, f, pack):
        sample = Sample(f, pack)
        self.packs[pack].append(sample)

    def addfile(self, filename, path, pack):
        if filename[-4:] == '.wav':
            self.addsample(filename, pack)
        else:
            os.remove(os.path.join(path, filename))

    def movesample(self, path, pack, sample):
        start_path = os.path.join(self.sourcepath, pack, sample.filename)
        end_path = os.path.join(path, sample.name + '.wav')
        shutil.copy2(start_path, end_path)

    def createorderpath(self, order, sample):
        path = self.destpath
        for i in range(len(order)):
            path += '/' + getattr(sample, order[i])
        return path

    def trycreatepath(self, path):
        try:
            os.makedirs(path)
        except:
            pass

    def initpacks(self):
        for pack in os.listdir(self.sourcepath):
            path = os.path.join(self.sourcepath, pack)
            if os.path.isdir(path):
                self.packs[pack] = []
                for f in os.listdir(path):
                    self.addfile(f, path, pack)

    def sortfiles(self, order=['instrument', 'subinstrument', 'type', 'bpm', 'pack']):
        for pack in self.packs.keys():
            for sample in self.packs[pack]:
                path = self.createorderpath(order, sample)
                self.trycreatepath(path)
                if not sample.name + '.wav' in os.listdir(path):
                    self.movesample(path, pack, sample)

    def initJSON(self):
        data = copy.deepcopy(self.packs)
        for pack in data.keys():
            for i in range(len(data[pack])):
                data[pack][i] = data[pack][i].todict()
        return data

    def editJSON(self):
        data = json.loads(open('../data/pack.json', 'r').read())
        for pack in self.packs.keys():
            if not (pack in data.keys() or (len(self.packs[pack]) == len(data[pack]))):
                data[pack] = []
                for i in range(len(self.packs[pack])):
                    data[pack].append(self.packs[pack][i].todict())
        return data

    def setsubinstrument(data):
        for pack in data.keys():
            if not data[pack][0]["subinstrument"]:
                instrument_library = InstrumentLibrary(self.packs[pack])
                instrument_library.populate()
                instrument_library.sort()
                for i in range(len(data[pack])):
                    data[pack][i]["subinstrument"] = self.packs[pack][i].subinstrument
        return data

    def create(self, arguments):
        if len(arguments) == 2 and arguments[1] == 'delete':
            shutil.rmtree(self.destpath)

        self.trycreatepath(self.destpath)
        self.initpacks()

        if not os.path.exists('../data/pack.json'):
            data = self.initJSON()
        else:
            data = self.editJSON()

        data = self.subinstrument(data)

        file = open('../data/pack.json', 'w')
        file.write(json.dumps(data, indent=4))
        file.close()

        if len(arguments) == 1:
            self.sortfiles()
        elif arguments[1] != 'delete':
            self.sortfiles(sys.argv[1:])

        PackLibraryReport(self.packs)
