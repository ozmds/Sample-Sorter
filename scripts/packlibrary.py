import os, os.path, shutil, sys, time, json, copy

from sample import Sample
from instrumentlibrary import InstrumentLibrary
from packreport import PackLibraryReport
from instrumentreport import InstrumentLibraryReport

class PackLibrary:
    def __init__(self, spath, dpath, countfile, datafile, css):
        self.data = {}
        self.words = {}
        self.sourcepath = os.path.abspath(spath)
        self.destpath = os.path.abspath(dpath)
        self.countfile = countfile
        self.datafile = datafile
        self.css = css

    def addsample(self, f, pack):
        sample = Sample(f, pack)
        self.data[pack].append(sample.todict())

    def addfile(self, filename, path, pack):
        if filename[-4:] == '.wav':
            self.addsample(filename, pack)
        else:
            os.remove(os.path.join(path, filename))

    def movesample(self, path, pack, sample):
        start_path = os.path.join(self.sourcepath, pack, sample["filename"])
        end_path = os.path.join(path, sample["name"] + '.wav')
        shutil.copy2(start_path, end_path)

    def createorderpath(self, order, sample):
        path = self.destpath
        for i in range(len(order)):
            path += '/' + sample[order[i]]
        return path

    def trycreatepath(self, path):
        try:
            os.makedirs(path)
        except:
            pass

    def sortfiles(self, order=['instrument', 'subinstrument', 'type', 'bpm', 'pack']):
        for pack in self.data.keys():
            for sample in self.data[pack]:
                path = self.createorderpath(order, sample)
                self.trycreatepath(path)
                if not sample["name"] + '.wav' in os.listdir(path):
                    self.movesample(path, pack, sample)

    def initJSON(self):
        self.data = {}
        for pack in os.listdir(self.sourcepath):
            path = os.path.join(self.sourcepath, pack)
            if os.path.isdir(path):
                self.data[pack] = []
                for f in os.listdir(path):
                    self.addfile(f, path, pack)

    def editJSON(self):
        self.data = json.loads(open(self.datafile, 'r').read())
        self.data = self.data['samples']
        for pack in os.listdir(self.sourcepath):
            sample_list = os.listdir(os.path.join(self.sourcepath, pack))
            pack_count = len(sample_list)
            if not (pack in self.data.keys() or (pack_count == len(self.data[pack]))):
                self.data[pack] = []
                for f in sample_list:
                    self.addfile(f, sample_list, pack)

    def setsubinstrument(self, words={}):
        for pack in self.data.keys():
            if self.data[pack][0]["subinstrument"] == str(None):
                instrument_library = InstrumentLibrary(self.data[pack], pack)
                instrument_library.populate()
                new_pack = instrument_library.sort()
                if new_pack['continue'] == False:
                    break
                else:
                    self.data[pack] = new_pack['samples']
                words[pack] = new_pack['words']

        return words

    def create(self, arguments):
        if len(arguments) == 2 and arguments[1] == 'delete':
            shutil.rmtree(self.destpath)
            os.remove(self.datafile)
        else:
            self.trycreatepath(self.destpath)

            if not os.path.exists(self.datafile):
                self.initJSON()
                self.words = self.setsubinstrument()
            else:
                self.editJSON()
                words = json.loads(open(self.datafile, 'r').read())
                words = words['words']
                self.words = self.setsubinstrument(words)

            data = {'samples': self.data, 'words': self.words}

            file = open(self.datafile, 'w')
            file.write(json.dumps(data, indent=4))
            file.close()

            if len(arguments) == 1:
                self.sortfiles()

            PackLibraryReport(self.data, self.countfile, self.css)
            InstrumentLibraryReport(self.words, self.css)
