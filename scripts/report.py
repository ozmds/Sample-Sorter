class Report:
    def __init__(self, data, filename, title):
        file = open(filename, 'w')
        self.createHTMLHeader(title, file)
        file.write(Report.createOpenTag('body'))
        self.createTable(data, file)
        file.write(Report.createCloseTag('body'))
        self.createHTMLCloser(file)

    @staticmethod
    def convertToCloseTag(tag):
        return tag[0] + '/' + tag[1:]

    @staticmethod
    def addNewLineToTag(tag):
        return tag + '\n'

    @staticmethod
    def createHTMLTag(text, endline):
        tag = '<' + text + '>'
        if endline:
            return Report.addNewLineToTag(tag)
        else:
            return tag

    @staticmethod
    def createOpenTag(text, endline=True, attr={}):
        for a in attr.keys():
            text = text + ' ' + a + ' = ' + Report.addEscapeDashes(attr[a])
        return Report.createHTMLTag(text, endline)

    @staticmethod
    def createCloseTag(text, endline=True):
        tag = Report.createHTMLTag(text, endline)
        return Report.convertToCloseTag(tag)

    @staticmethod
    def addEscapeDashes(text):
        return '\'' + text + '\''

    def createHTMLHeader(self, header, file):
        file.write(Report.createOpenTag('!DOCTYPE html'))
        file.write(Report.createOpenTag('html'))
        file.write(Report.createOpenTag('head'))
        file.write(Report.createOpenTag('title', False))
        file.write(header)
        file.write(Report.createCloseTag('title'))
        file.write(Report.createCloseTag('head'))

    def createHTMLCloser(self, file):
        file.write(Report.createCloseTag('html'))

    def createTable(self, data, file):
        tableattr = {}
        tableattr['width'] = '100%'
        tableattr['bordercolor'] = 'blue'
        tableattr['border'] = '1'
        tableattr['cellpadding'] = '10'

        file.write(Report.createOpenTag('table', attr=tableattr))

        for row in range(len(data)):
            file.write('<tr>\n')
            cell_status = 'td'
            if row == 0:
                cell_status = 'th'
            for j in range(len(data[0])):
                file.write(Report.createOpenTag(cell_status, False))
                file.write(str(data[row][j]))
                file.write(Report.createCloseTag(cell_status))
            file.write('</tr>\n')

        file.write(Report.createCloseTag('table'))
