from sortedlist import SortedList
import unittest


class SortedlistTest(unittest.TestCase):
    def test_getlist(self):
        sortedlist_instance = SortedList({u'guitar': 10, u'total': 10, u'other': 0})
        self.assertEquals(
            sortedlist_instance.getlist(),
            [u'guitar']
        )

        sortedlist_instance = SortedList({u'guitar': 10, u'total': 10, u'other': 0})
        self.assertEquals(
            sortedlist_instance.getlist(),
            [u'guitar']
        )

    def test_sort(self):
        sortedlist_instance = SortedList({u'total': 7, u'other': 0, u'bass': 7})
        self.assertEquals(
            sortedlist_instance.sort(),
            None
        )

        sortedlist_instance = SortedList({u'total': 7, u'other': 0, u'bass': 7})
        self.assertEquals(
            sortedlist_instance.sort(),
            None
        )

    def test_spliceintolist(self):
        sortedlist_instance = SortedList({u'total': 5, u'hat': 1, u'other': 2, u'kick': 2})
        self.assertEquals(
            sortedlist_instance.spliceintolist(i=0,word=u'hat'),
            None
        )

if __name__ == "__main__":
    unittest.main()