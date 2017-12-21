import report
from report import Report
import unittest


class ReportTest(unittest.TestCase):
    def test_addEscapeDashes(self):
        self.assertEquals(
            Report.addEscapeDashes(text='100%'),
            "'100%'"
        )

    def test_addNewLineToTag(self):
        self.assertEquals(
            Report.addNewLineToTag(tag='<table>'),
            '<table>\n'
        )

    def test_convertToCloseTag(self):
        self.assertEquals(
            Report.convertToCloseTag(tag='<title>\n'),
            '</title>\n'
        )

    def test_createCloseTag(self):
        self.assertEquals(
            Report.createCloseTag(text='title',endline=True),
            '</title>\n'
        )

    def test_createHTMLCloser(self):
        report_instance = Report([['Pack Name', 'Total Number of Files', 'Number of Files Present', 'Number of Files Missing', 'Package Completion Percentage'], [u'Jazz Sax and Bass', 20, 20, 0, 100.0], [u'Electronic Indie Session', 20, 20, 0, 100.0], [u'Ethereal Guitar and Vocals', 20, 20, 0, 100.0]], 'report.html', 'Converse Library Report')
        self.assertEquals(
            report_instance.createHTMLCloser(file=<open file 'report.html', mode 'w' at 0x0000000004B4EA50>),
            None
        )

    def test_createHTMLHeader(self):
        report_instance = Report([['Pack Name', 'Total Number of Files', 'Number of Files Present', 'Number of Files Missing', 'Package Completion Percentage'], [u'Jazz Sax and Bass', 20, 20, 0, 100.0], [u'Electronic Indie Session', 20, 20, 0, 100.0], [u'Ethereal Guitar and Vocals', 20, 20, 0, 100.0]], 'report.html', 'Converse Library Report')
        self.assertEquals(
            report_instance.createHTMLHeader(header='Converse Library Report',file=<open file 'report.html', mode 'w' at 0x0000000004B4EA50>),
            None
        )

    def test_createHTMLTag(self):
        self.assertEquals(
            Report.createHTMLTag(text='body',endline=True),
            '<body>\n'
        )

        self.assertEquals(
            Report.createHTMLTag(text='body',endline=True),
            '<body>\n'
        )

    def test_createOpenTag(self):
        self.assertEquals(
            Report.createOpenTag(text='th',endline=False,attr={}),
            '<th>'
        )

        self.assertEquals(
            Report.createOpenTag(text='th',endline=False,attr={}),
            '<th>'
        )

        self.assertEquals(
            Report.createOpenTag(text='th',endline=False,attr={}),
            '<th>'
        )

        self.assertEquals(
            Report.createOpenTag(text='th',endline=False,attr={}),
            '<th>'
        )

        self.assertEquals(
            Report.createOpenTag(text='th',endline=False,attr={}),
            '<th>'
        )

    def test_createTable(self):
        report_instance = Report([['Pack Name', 'Total Number of Files', 'Number of Files Present', 'Number of Files Missing', 'Package Completion Percentage'], [u'Jazz Sax and Bass', 20, 20, 0, 100.0], [u'Electronic Indie Session', 20, 20, 0, 100.0], [u'Ethereal Guitar and Vocals', 20, 20, 0, 100.0]], 'report.html', 'Converse Library Report')
        self.assertEquals(
            report_instance.createTable(data=[['Pack Name', 'Total Number of Files', 'Number of Files Present', 'Number of Files Missing', 'Package Completion Percentage'], [u'Jazz Sax and Bass', 20, 20, 0, 100.0], [u'Electronic Indie Session', 20, 20, 0, 100.0], [u'Ethereal Guitar and Vocals', 20, 20, 0, 100.0]],file=<open file 'report.html', mode 'w' at 0x0000000004B4EA50>),
            None
        )

if __name__ == "__main__":
    unittest.main()