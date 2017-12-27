import json, dominate
from dominate.tags import *

class PackLibraryReport():
    def __init__(self, pack_library, count_file, css):
        totalcount = json.loads(file(count_file, 'r').read())
        data = self.createdata(pack_library, totalcount)
        self.writereport(data, css)

    def createdata(self, pack_library, total_count):
        data = []
        pack_header = ['Pack Name', 'Total Number of Files', 'Number of Files Present',
                       'Number of Files Missing', 'Package Completion Percentage']
        data.append(pack_header)
        for pack in pack_library.keys():
            data.append(self.createpackdata(pack, len(pack_library[pack]), total_count[pack]))
        return data

    def createpackdata(self, pack, count, total_count):
        pack_data = [pack, total_count, count]
        pack_data.append(pack_data[1] - pack_data[2])
        pack_data.append(round(float(pack_data[2]) / pack_data[1] * 100, 2))
        return pack_data

    def writereport(self, data, css):
        doc = dominate.document(title='Converse Pack Library Report')

        with doc.head:
            link(rel='stylesheet', href=css)

        with doc:
            with table():
                for i in range(len(data)):
                    with tr():
                        for col in data[i]:
                            if i == 0:
                                th(col)
                            else:
                                td(col)

        file = open('pack-report.html', 'w')
        file.write(doc.render())
        file.close()
