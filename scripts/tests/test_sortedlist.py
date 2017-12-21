import genericpath
from instrumentlibrary import InstrumentLibrary
import json
from mock import patch
import ntpath
import os
import os, os.path, shutil, sys, time, json, copy
from packlibrary import PackLibrary
from packreport import PackLibraryReport
import report
from report import Report
from sample import Sample
import shutil
from sortedlist import SortedList
import unittest


class SortedlistTest(unittest.TestCase):
    def test_getlist(self):
        sortedlist_instance = SortedList({'sax': 13})
        self.assertEquals(
            sortedlist_instance.getlist(),
            ['sax']
        )

        sortedlist_instance = SortedList({'sax': 13})
        self.assertEquals(
            sortedlist_instance.getlist(),
            ['sax']
        )

    def test_sort(self):
        sortedlist_instance = SortedList({'ariah': 4, 'lewis': 6})
        self.assertEquals(
            sortedlist_instance.sort(),
            None
        )

        sortedlist_instance = SortedList({'ariah': 4, 'lewis': 6})
        self.assertEquals(
            sortedlist_instance.sort(),
            None
        )

    def test_spliceintolist(self):
        sortedlist_instance = SortedList({'1': 2, 'di': 2, 'stem': 2, 'guitar': 8, 'felipe': 5, '3': 2, '2': 4, 'jordan': 3, 'loop': 3})
        self.assertEquals(
            sortedlist_instance.spliceintolist(i=2,word='felipe'),
            None
        )

    def test_write(self):
        sortedlist_instance = SortedList({'di': 1, 'stutter': 1, '1': 2, '3': 1, '2': 1, '5': 1, 'kick': 2, 'hat': 1, 'cpu': 5, 'loop': 1})
        self.assertEquals(
            sortedlist_instance.write(),
            None
        )

        sortedlist_instance = SortedList({'di': 1, 'stutter': 1, '1': 2, '3': 1, '2': 1, '5': 1, 'kick': 2, 'hat': 1, 'cpu': 5, 'loop': 1})
        self.assertEquals(
            sortedlist_instance.write(),
            None
        )

if __name__ == "__main__":
    unittest.main()