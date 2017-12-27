from dominate.document import document
from dominate.dom_tag import dom_tag
from dominate.tags import *
from dominate.tags import input_
import encodings
from instrumentreport import InstrumentLibraryReport
import json, dominate
from mock import patch
from packreport import PackLibraryReport
from sortedlist import SortedList
import unittest


class InstrumentreportTest(unittest.TestCase):
    def test_write(self):
        instrumentlibraryreport_instance = InstrumentLibraryReport({u'Jazz Sax and Bass': {u'words': {u'bass': {u'total': 7, u'other': 0, u'bass': 7}, u'horns-and-reeds': {u'total': 13, u'sax': 13, u'other': 0}}}, u'Electronic Indie Session': {u'words': {u'guitar': {u'guitar': 8, u'total': 8, u'other': 0}, u'percussion': {u'total': 6, u'other': 0, u'bells': 6}, u'synths': {u'total': 5, u'hat': 1, u'other': 2, u'kick': 2}, u'bass': {u'total': 1, u'other': 0, u'bass': 1}}}, u'Ethereal Guitar and Vocals': {u'words': {u'guitar': {u'guitar': 10, u'total': 10, u'other': 0}, u'vocals': {u'ariah': 4, u'lewis': 6, u'other': 0, u'total': 10}}}}, '../../css/main.css')
        self.assertEquals(
            instrumentlibraryreport_instance.write(),
            None
        )

    @patch.object(dom_tag, '__new__')
    @patch.object(SortedList, 'getlist')
    @patch.object(SortedList, 'sort')
    @patch.object(input_, '__init__')
    @patch.object(SortedList, '__init__')
    @patch.object(dom_tag, '__enter__')
    @patch.object(dom_tag, '__exit__')
    @patch.object(document, 'render')
    @patch.object(document, '__init__')
    def test_writereport(self, mock___init__, mock_render, mock___exit__, mock___enter__, mock___init__, mock___init__, mock_sort, mock_getlist, mock___new__):
        mock___init__.return_value = None
        mock_render.return_value = u'<!DOCTYPE html>\n<html>\n  <head>\n    <title>Converse Pack Library Report</title>\n    <link href="../../css/main.css" rel="stylesheet">\n  </head>\n  <body>\n    <table>\n      <tr>\n        <th>Pack Name</th>\n        <th>Total Number of Files</th>\n        <th>Number of Files Present</th>\n        <th>Number of Files Missing</th>\n        <th>Package Completion Percentage</th>\n      </tr>\n      <tr>\n        <td>Jazz Sax and Bass</td>\n        <td>149</td>\n        <td>20</td>\n        <td>129</td>\n        <td>13.42</td>\n      </tr>\n      <tr>\n        <td>Electronic Indie Session</td>\n        <td>84</td>\n        <td>20</td>\n        <td>64</td>\n        <td>23.81</td>\n      </tr>\n      <tr>\n        <td>Ethereal Guitar and Vocals</td>\n        <td>183</td>\n        <td>20</td>\n        <td>163</td>\n        <td>10.93</td>\n      </tr>\n    </table>\n  </body>\n</html>'
        mock___exit__.return_value = None
        mock___enter__.return_value = <dominate.document "Jazz Sax and Bass Instrument Library Report">
        mock___init__.return_value = None
        mock___init__.return_value = None
        mock_sort.return_value = None
        mock_getlist.return_value = [u'guitar']
        mock___new__.return_value = <dominate.tags.tr at 4a34cf8: 0 attributes, 5 children>
        instrumentlibraryreport_instance = InstrumentLibraryReport({u'Jazz Sax and Bass': {u'words': {u'bass': {u'total': 7, u'other': 0, u'bass': 7}, u'horns-and-reeds': {u'total': 13, u'sax': 13, u'other': 0}}}, u'Electronic Indie Session': {u'words': {u'guitar': {u'guitar': 8, u'total': 8, u'other': 0}, u'percussion': {u'total': 6, u'other': 0, u'bells': 6}, u'synths': {u'total': 5, u'hat': 1, u'other': 2, u'kick': 2}, u'bass': {u'total': 1, u'other': 0, u'bass': 1}}}, u'Ethereal Guitar and Vocals': {u'words': {u'guitar': {u'guitar': 10, u'total': 10, u'other': 0}, u'vocals': {u'ariah': 4, u'lewis': 6, u'other': 0, u'total': 10}}}}, '../../css/main.css')
        self.assertEquals(
            instrumentlibraryreport_instance.writereport(data={u'guitar': {u'guitar': 8, u'total': 8, u'other': 0}, u'percussion': {u'total': 6, u'other': 0, u'bells': 6}, u'synths': {u'total': 5, u'hat': 1, u'other': 2, u'kick': 2}, u'bass': {u'total': 1, u'other': 0, u'bass': 1}},pack=u'Electronic Indie Session'),
            None
        )

if __name__ == "__main__":
    unittest.main()