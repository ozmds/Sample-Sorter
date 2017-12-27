from encodings.cp850 import Codec
from mock import patch
from sortedlist import SortedList
import unittest


class SortedlistTest(unittest.TestCase):
    def test_getlist(self):
        sortedlist_instance = SortedList({'bass': 1})
        self.assertEquals(
            sortedlist_instance.getlist(),
            ['bass']
        )

        sortedlist_instance = SortedList({'bass': 1})
        self.assertEquals(
            sortedlist_instance.getlist(),
            ['bass']
        )

    def test_sort(self):
        sortedlist_instance = SortedList({'bass': 1})
        self.assertEquals(
            sortedlist_instance.sort(),
            None
        )

        sortedlist_instance = SortedList({'bass': 1})
        self.assertEquals(
            sortedlist_instance.sort(),
            None
        )

    def test_spliceintolist(self):
        sortedlist_instance = SortedList({'total': 1, 'other': 0, 'bass': 1})
        self.assertEquals(
            sortedlist_instance.spliceintolist(i=0,word='other'),
            None
        )

    @patch.object(Codec, 'encode')
    def test_write(self, mock_encode):
        mock_encode.return_value = ('C:\\Users\\athav\\Desktop\\Sample-Sorter\\scripts\\testdata\\sorted files/guitar/None/stem', 83)
        sortedlist_instance = SortedList({u'di': 1, u'stutter': 1, u'1': 2, u'3': 1, u'2': 1, u'5': 1, u'kick': 2, u'hat': 1, u'cpu': 5, u'loop': 1})
        self.assertEquals(
            sortedlist_instance.write(),
            None
        )

        sortedlist_instance = SortedList({u'di': 1, u'stutter': 1, u'1': 2, u'3': 1, u'2': 1, u'5': 1, u'kick': 2, u'hat': 1, u'cpu': 5, u'loop': 1})
        self.assertEquals(
            sortedlist_instance.write(),
            None
        )

if __name__ == "__main__":
    unittest.main()