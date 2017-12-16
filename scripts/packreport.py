import json
from report import Report

class PackLibraryReport(Report):
    def __init__(self, pack_library):
        data = self.createdata(pack_library)
        Report.__init__(self, data, 'report.html', 'Converse Library Report')

    def createpackdata(self, pack, count, total_count):
        pack_data = [pack, total_count, count]
        pack_data.append(pack_data[1] - pack_data[2])
        pack_data.append(round(float(pack_data[2]) / pack_data[1] * 100, 2))

        return pack_data

    def createdata(self, pack_library):
        data = []
        pack_header = ['Pack Name', 'Total Number of Files', 'Number of Files Present',
                       'Number of Files Missing', 'Package Completion Percentage']
        data.append(pack_header)
        total_count = json.loads('../data/count.json')
        for pack in pack_library.keys():
            data.append(self.createpackdata(pack, len(pack_library[pack], total_count[pack])))
        return data
