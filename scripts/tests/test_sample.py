from dominate.document import document
from dominate.dom_tag import dom_tag
from dominate.tags import *
from dominate.tags import input_
import encodings
from instrumentlibrary import InstrumentLibrary
from instrumentreport import InstrumentLibraryReport
import json, dominate
from mock import patch
from packreport import PackLibraryReport
from sample import Sample
from sortedlist import SortedList
import unittest


class SampleTest(unittest.TestCase):
    def test_initsample(self):
        sample_instance = Sample('torches-balancer-mainland-mr.-james_bass-loop-2_bass_loop_100.wav.wav', 'Electronic Indie Session')
        self.assertEquals(
            sample_instance.initsample(),
            None
        )

    def test_setbpm(self):
        sample_instance = Sample('carey-clayton-feat.-lewis-and-ariah-noetzel_guitar-stem-5_guitar_stem_132.wav.wav', 'Ethereal Guitar and Vocals')
        self.assertEquals(
            sample_instance.setbpm(split=['guitar-stem-5']),
            ['guitar-stem-5']
        )

    def test_setdupindex(self):
        sample_instance = Sample('carey-clayton-feat.-lewis-and-ariah-noetzel_ariah-2_vocals_one_shot_149.wav.wav', 'Ethereal Guitar and Vocals')
        self.assertEquals(
            sample_instance.setdupindex(split=['ariah-2']),
            ['ariah-2']
        )

    def test_setinstrument(self):
        sample_instance = Sample('timo-vollbrecht_sax-loop-15_horns-and-reeds_loop_152.wav.wav', 'Jazz Sax and Bass')
        self.assertEquals(
            sample_instance.setinstrument(split=['sax-loop-15']),
            ['sax-loop-15']
        )

    def test_setname(self):
        sample_instance = Sample('david-lizmi_bass-19_bass_one_shot_128.wav.wav', 'Jazz Sax and Bass')
        self.assertEquals(
            sample_instance.setname(split=['bass-19']),
            'david-lizmi-bass-19'
        )

    def test_settype(self):
        sample_instance = Sample('carey-clayton-feat.-lewis-and-ariah-noetzel_guitar-loop-13_guitar_loop_82.wav.wav', 'Ethereal Guitar and Vocals')
        self.assertEquals(
            sample_instance.settype(split=['guitar-loop-13']),
            ['guitar-loop-13']
        )

    def test_stripwav(self):
        sample_instance = Sample('carey-clayton-feat.-lewis-and-ariah-noetzel_guitar-loop-13_guitar_loop_82.wav.wav', 'Ethereal Guitar and Vocals')
        self.assertEquals(
            sample_instance.stripwav(split=['guitar-loop-13']),
            ['guitar-loop-13']
        )

    def test_todict(self):
        sample_instance = Sample('carey-clayton-feat.-lewis-and-ariah-noetzel_guitar-4_guitar_one_shot_.wav.wav', 'Ethereal Guitar and Vocals')
        self.assertEquals(
            sample_instance.todict(),
            {'subinstrument': 'None', 'name': 'carey-clayton-feat.-lewis-and-ariah-noetzel-guitar-4', 'basename': 'guitar-4', 'bpm': 'None', 'filename': 'carey-clayton-feat.-lewis-and-ariah-noetzel_guitar-4_guitar_one_shot_.wav.wav', 'sortedpath': 'C:\\Users\\athav\\Desktop\\Sample-Sorter\\scripts\\testdata\\sorted files/guitar/None/one-shot/None/Ethereal Guitar and Vocals/carey-clayton-feat.-lewis-and-ariah-noetzel-guitar-4.wav', 'instrument': 'guitar', 'type': 'one-shot', 'pack': 'Ethereal Guitar and Vocals'}
        )

        sample_instance = Sample('carey-clayton-feat.-lewis-and-ariah-noetzel_guitar-4_guitar_one_shot_.wav.wav', 'Ethereal Guitar and Vocals')
        self.assertEquals(
            sample_instance.todict(),
            {'subinstrument': 'None', 'name': 'carey-clayton-feat.-lewis-and-ariah-noetzel-guitar-4', 'basename': 'guitar-4', 'bpm': 'None', 'filename': 'carey-clayton-feat.-lewis-and-ariah-noetzel_guitar-4_guitar_one_shot_.wav.wav', 'sortedpath': 'C:\\Users\\athav\\Desktop\\Sample-Sorter\\scripts\\testdata\\sorted files/guitar/None/one-shot/None/Ethereal Guitar and Vocals/carey-clayton-feat.-lewis-and-ariah-noetzel-guitar-4.wav', 'instrument': 'guitar', 'type': 'one-shot', 'pack': 'Ethereal Guitar and Vocals'}
        )

if __name__ == "__main__":
    unittest.main()