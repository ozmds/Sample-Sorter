class Sample:
    def __init__(self, f, pack):
        self.filename = f
        self.pack = pack
        self.type = None
        self.instrument = None
        self.name = None
        self.basename = None
        self.bpm = 0
        self.subinstrument = None

        self.dupindex = None

        self.initsample()

    def todict(self):
        data = {}
        data["filename"] = self.filename
        data["pack"] = self.pack
        data["type"] = self.type
        data["instrument"] = self.instrument
        data["name"] = self.name
        data["basename"] = self.basename
        data["bpm"] = self.bpm
        data["subinstrument"] = self.subinstrument

        return data

    def setsubinstrument(self, x):
        self.subinstrument = x

    def initsample(self):
        split = self.stripwav(self.filename.split('_'))
        split = self.setdupindex(split)
        split = self.stripwav(split)
        split = self.setbpm(split)

        split = self.settype(split)
        split = self.setinstrument(split)

        self.name = self.setname(split)
        split.pop(0)
        self.basename = self.setname(split)

    def stripwav(self, split):
        split[-1] = split[-1][:-4]
        return split

    def setdupindex(self, split):
        if split[-1][-1] == ')':
            self.dupindex = split[-1][-2]
            split[-1] = split[-1][:-3]
        return split

    def setinstrument(self, split):
        self.instrument = split[-1]
        split.pop(-1)
        return split

    def setbpm(self, split):
        if split[-1] == '':
            self.bpm = str(None)
        else:
            self.bpm = split[-1]
        split.pop(-1)
        return split

    def settype(self, split):
        if split[-1] == 'shot':
            samptype = split[-2] + '-' + split[-1]
            split.pop(-1)
        else:
            samptype = split[-1]
        split.pop(-1)
        self.type = samptype
        return split

    def setname(self, split):
        name = ''
        for i in split:
            name = name + i
            name = name + '-'
        name = name[:-1]
        if self.dupindex:
            name = name + '-' + self.dupindex
        return name
