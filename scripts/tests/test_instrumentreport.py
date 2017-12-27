from dominate.document import document
from dominate.dom_tag import dom_tag
from dominate.tags import *
from dominate.tags import input_
import encodings
from encodings.cp850 import Codec
import genericpath
from instrumentlibrary import InstrumentLibrary
from instrumentreport import InstrumentLibraryReport
import json
import json, dominate
from mock import patch
import ntpath
import os
import os, os.path, shutil, sys, time, json, copy
from packlibrary import PackLibrary
from packreport import PackLibraryReport
from sample import Sample
import shutil
from sortedlist import SortedList
import unittest


class InstrumentreportTest(unittest.TestCase):
    def test_write(self):
        instrumentlibraryreport_instance = InstrumentLibraryReport({u'Jazz Sax and Bass': {u'words': {u'bass': {u'total': 7, u'other': 0, u'bass': 7}, u'horns-and-reeds': {u'total': 13, u'sax': 13, u'other': 0}}}, u'Electronic Indie Session': {'words': {u'guitar': {'guitar': 8, 'total': 8, 'other': 0}, u'percussion': {'total': 6, 'other': 0, 'bells': 6}, u'synths': {'total': 5, 'other': 2, 'hat': 1, 'kick': 2}, u'bass': {'total': 1, 'other': 0, 'bass': 1}}}}, '../../css/main.css')
        self.assertEquals(
            instrumentlibraryreport_instance.write(),
            None
        )

    @patch.object(document, '__init__')
    @patch.object(dom_tag, '__new__')
    @patch.object(dom_tag, '__exit__')
    @patch.object(input_, '__init__')
    @patch.object(document, 'render')
    @patch.object(SortedList, 'sort')
    @patch.object(dom_tag, '__enter__')
    @patch.object(SortedList, '__init__')
    @patch.object(SortedList, 'getlist')
    def test_writereport(self, mock_getlist, mock___init__, mock___enter__, mock_sort, mock_render, mock___init__, mock___exit__, mock___new__, mock___init__):
        mock_getlist.return_value = ['guitar']
        mock___init__.return_value = None
        mock___enter__.return_value = <dominate.document "Jazz Sax and Bass Instrument Library Report">
        mock_sort.return_value = None
        mock_render.return_value = u'<!DOCTYPE html>\n<html>\n  <head>\n    <title>Converse Pack Library Report</title>\n    <link href="../../css/main.css" rel="stylesheet">\n  </head>\n  <body>\n    <table>\n      <tr>\n        <th>Pack Name</th>\n        <th>Total Number of Files</th>\n        <th>Number of Files Present</th>\n        <th>Number of Files Missing</th>\n        <th>Package Completion Percentage</th>\n      </tr>\n      <tr>\n        <td>Jazz Sax and Bass</td>\n        <td>149</td>\n        <td>20</td>\n        <td>129</td>\n        <td>13.42</td>\n      </tr>\n      <tr>\n        <td>Electronic Indie Session</td>\n        <td>84</td>\n        <td>20</td>\n        <td>64</td>\n        <td>23.81</td>\n      </tr>\n      <tr>\n        <td>Ethereal Guitar and Vocals</td>\n        <td>183</td>\n        <td>20</td>\n        <td>163</td>\n        <td>10.93</td>\n      </tr>\n    </table>\n  </body>\n</html>'
        mock___init__.return_value = None
        mock___exit__.return_value = None
        mock___new__.return_value = <dominate.tags.tr at 4e88208: 0 attributes, 5 children>
        mock___init__.return_value = None
        instrumentlibraryreport_instance = InstrumentLibraryReport({u'Jazz Sax and Bass': {u'words': {u'bass': {u'total': 7, u'other': 0, u'bass': 7}, u'horns-and-reeds': {u'total': 13, u'sax': 13, u'other': 0}}}, u'Electronic Indie Session': {'words': {u'guitar': {'guitar': 8, 'total': 8, 'other': 0}, u'percussion': {'total': 6, 'other': 0, 'bells': 6}, u'synths': {'total': 5, 'other': 2, 'hat': 1, 'kick': 2}, u'bass': {'total': 1, 'other': 0, 'bass': 1}}}}, '../../css/main.css')
        self.assertEquals(
            instrumentlibraryreport_instance.writereport(data={u'guitar': {'guitar': 8, 'total': 8, 'other': 0}, u'percussion': {'total': 6, 'other': 0, 'bells': 6}, u'synths': {'total': 5, 'other': 2, 'hat': 1, 'kick': 2}, u'bass': {'total': 1, 'other': 0, 'bass': 1}},pack=u'Electronic Indie Session'),
            None
        )

if __name__ == "__main__":
    unittest.main()