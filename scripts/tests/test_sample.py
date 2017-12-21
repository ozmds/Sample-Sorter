from instrumentlibrary import InstrumentLibrary
import json
from mock import patch
from packreport import PackLibraryReport
from report import Report
from sample import Sample
from sortedlist import SortedList
import unittest


class SampleTest(unittest.TestCase):
    def test_initsample(self):
        sample_instance = Sample('timo-vollbrecht_sax-7_horns-and-reeds_one_shot_152.wav.wav', 'Jazz Sax and Bass')
        self.assertEquals(
            sample_instance.initsample(),
            None
        )

    def test_setbpm(self):
        sample_instance = Sample('carey-clayton-feat.-lewis-and-ariah-noetzel_lewis-3_vocals_one_shot_.wav.wav', 'Ethereal Guitar and Vocals')
        self.assertEquals(
            sample_instance.setbpm(split=['lewis-3']),
            ['lewis-3']
        )

    def test_setdupindex(self):
        sample_instance = Sample('torches-balancer-mainland-mr.-james_bells-stem-2_percussion_stem_100.wav.wav', 'Electronic Indie Session')
        self.assertEquals(
            sample_instance.setdupindex(split=['bells-stem-2']),
            ['bells-stem-2']
        )

    def test_setinstrument(self):
        sample_instance = Sample('carey-clayton-feat.-lewis-and-ariah-noetzel_guitar-4_guitar_one_shot_.wav.wav', 'Ethereal Guitar and Vocals')
        self.assertEquals(
            sample_instance.setinstrument(split=['guitar-4']),
            ['guitar-4']
        )

    def test_setname(self):
        sample_instance = Sample('carey-clayton-feat.-lewis-and-ariah-noetzel_guitar-stem-5_guitar_stem_132.wav.wav', 'Ethereal Guitar and Vocals')
        self.assertEquals(
            sample_instance.setname(split=['guitar-stem-5']),
            'carey-clayton-feat.-lewis-and-ariah-noetzel-guitar-stem-5'
        )

    def test_settype(self):
        sample_instance = Sample('carey-clayton-feat.-lewis-and-ariah-noetzel_lewis-2_vocals_one_shot_.wav.wav', 'Ethereal Guitar and Vocals')
        self.assertEquals(
            sample_instance.settype(split=['lewis-2']),
            ['lewis-2']
        )

    def test_stripwav(self):
        sample_instance = Sample('david-lizmi_bass-loop-14_bass_loop_152.wav.wav', 'Jazz Sax and Bass')
        self.assertEquals(
            sample_instance.stripwav(split=['bass-loop-14']),
            ['bass-loop-14']
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