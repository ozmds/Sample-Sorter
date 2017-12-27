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
        sample_instance = Sample('torches-balancer-mainland-mr.-james_bells-loop-2_percussion_loop_100.wav.wav', 'Electronic Indie Session')
        self.assertEquals(
            sample_instance.initsample(),
            None
        )

    def test_setbpm(self):
        sample_instance = Sample('timo-vollbrecht_sax-12_horns-and-reeds_one_shot_152.wav.wav', 'Jazz Sax and Bass')
        self.assertEquals(
            sample_instance.setbpm(split=['sax-12']),
            ['sax-12']
        )

    def test_setdupindex(self):
        sample_instance = Sample('timo-vollbrecht_sax-24_horns-and-reeds_one_shot_128.wav.wav', 'Jazz Sax and Bass')
        self.assertEquals(
            sample_instance.setdupindex(split=['sax-24']),
            ['sax-24']
        )

    def test_setinstrument(self):
        sample_instance = Sample('carey-clayton-feat.-lewis-and-ariah-noetzel_ariah-1_vocals_one_shot_149.wav.wav', 'Ethereal Guitar and Vocals')
        self.assertEquals(
            sample_instance.setinstrument(split=['ariah-1']),
            ['ariah-1']
        )

    def test_setname(self):
        sample_instance = Sample('timo-vollbrecht_sax-stem-2_horns-and-reeds_stem_128.wav.wav', 'Jazz Sax and Bass')
        self.assertEquals(
            sample_instance.setname(split=['sax-stem-2']),
            'sax-stem-2'
        )

    def test_settype(self):
        sample_instance = Sample('timo-vollbrecht_sax-loop-29_horns-and-reeds_loop_128.wav.wav', 'Jazz Sax and Bass')
        self.assertEquals(
            sample_instance.settype(split=['sax-loop-29']),
            ['sax-loop-29']
        )

    def test_stripwav(self):
        sample_instance = Sample('timo-vollbrecht_sax-loop-24_horns-and-reeds_loop_128.wav.wav', 'Jazz Sax and Bass')
        self.assertEquals(
            sample_instance.stripwav(split=['sax-loop-24']),
            ['sax-loop-24']
        )

    def test_todict(self):
        sample_instance = Sample('carey-clayton-feat.-lewis-and-ariah-noetzel_ariah-3_vocals_one_shot_149.wav.wav', 'Ethereal Guitar and Vocals')
        self.assertEquals(
            sample_instance.todict(),
            {'subinstrument': 'ariah', 'name': 'carey-clayton-feat.-lewis-and-ariah-noetzel-ariah-3', 'basename': 'ariah-3', 'bpm': '149', 'filename': 'carey-clayton-feat.-lewis-and-ariah-noetzel_ariah-3_vocals_one_shot_149.wav.wav', 'instrument': 'vocals', 'type': 'one-shot', 'pack': 'Ethereal Guitar and Vocals'}
        )

        sample_instance = Sample('carey-clayton-feat.-lewis-and-ariah-noetzel_ariah-3_vocals_one_shot_149.wav.wav', 'Ethereal Guitar and Vocals')
        self.assertEquals(
            sample_instance.todict(),
            {'subinstrument': 'ariah', 'name': 'carey-clayton-feat.-lewis-and-ariah-noetzel-ariah-3', 'basename': 'ariah-3', 'bpm': '149', 'filename': 'carey-clayton-feat.-lewis-and-ariah-noetzel_ariah-3_vocals_one_shot_149.wav.wav', 'instrument': 'vocals', 'type': 'one-shot', 'pack': 'Ethereal Guitar and Vocals'}
        )

if __name__ == "__main__":
    unittest.main()