import re
import urllib
import mechanize
import unittest

class GCalc:
    def __init__(self):
        self.browser = mechanize.Browser()
        self.browser.set_handle_robots(False)
        self.browser.addheaders = \
            [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

    def cleanup(self,text):
        strip_tags = re.compile("<.*?>")
        return strip_tags.sub('', text.replace("<sup>","^").replace("</sup>","").replace("&#215;","X"))

    def calc(self, query):
        try:
            raw_result = self.browser.open("http://www.google.com/search?hl=en&q="+urllib.quote_plus(query)).read()
            return self.parse(raw_result)
        except:
            return "Failed to reach Google"

    def parse(self, raw_result):
        try:
            result = raw_result.split('''<td style="vertical-align:top" >''')[1].split('</h2>')[0] + '</h2>'
            return self.cleanup(result)
        except:
            return "Not a calculator query"

class TestGCalc(unittest.TestCase):
    def setUp(self):
        self.g = GCalc()

    def test_numeric(self):
        self.assertEqual(self.g.calc("4+5"), "4 + 5 = 9")

    def test_bignumbers(self):
        self.assertEqual(self.g.calc("234623476 * 59999999999"), "234 623 476 * 59 999 999 999 = 1.40774086 X 10^19")

    def test_units(self):
        self.assertEqual(self.g.calc("14 inch in mm"), "14 inch = 355.6 millimeters")
        self.assertEqual(self.g.calc("one acre"), "one acre = 4\xc2\xa0046.85642 m^2")

    def test_cacl(self):
        self.assertEqual(self.g.calc("3 * PI / sin(3)"), "(3 * PI) / sin(3) = 66.7855543")

    def test_facts(self):
        self.assertEqual(self.g.calc("speed of light"), "the speed of light = 299\xc2\xa0792\xc2\xa0458 m / s")


if __name__=='__main__':
    unittest.main()

