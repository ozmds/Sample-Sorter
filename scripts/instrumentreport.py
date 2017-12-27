import json, dominate
from dominate.tags import *
from sortedlist import SortedList

class InstrumentLibraryReport():
    def __init__(self, data, css):
        self.css = css
        self.words = data
        self.write()

    def write(self):
        for pack in self.words.keys():
            self.writereport(pack, self.words[pack]['words'])

    def writereport(self, pack, data):
        doc = dominate.document(title=pack + ' Instrument Library Report')

        rows = []

        for instrument in data.keys():
            rows.append(len(data[instrument].keys()))

        rows = max(rows)

        with doc.head:
            link(rel='stylesheet', href=self.css)

        with doc:
            with table():
                with tr():
                    th(pack, colspan=rows + 1)
                data_keys = data.keys()
                for instrument in data_keys:
                    words = SortedList(data[instrument])
                    words.sort()
                    words = words.getlist()
                    words.remove('total')
                    words.remove('other')
                    with tr():
                        td(instrument, rowspan=2)
                        for i in range(len(words)):
                            td(words[i])
                        td('other', colspan=rows - len(words) - 1)
                        td('total')
                    with tr():
                        for i in range(len(words)):
                            td(data[instrument][words[i]])
                        td(data[instrument]['other'], colspan=rows - len(words) - 1)
                        td(data[instrument]['total'])

        pack = pack.lower()
        pack = pack.split()
        pack = '-'.join(pack)

        file = open(pack + '-instrument-report.html', 'w')
        file.write(doc.render())
        file.close()
