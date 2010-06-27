import urllib
import mechanize

class GCalc:
    def __init__(self):
        self.base_url = "http://google.com/?q="
        self.browser = mechanize.Browser()
        self.browser.set_handle_robots(False)
        self.browser.addheaders = \
            [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

    def calc(self, query):
        raw_result = self.browser.open("http://www.google.com/search?hl=en&q="+urllib.quote_plus(query)).read()
        return self.parse(raw_result)

    def parse(self, raw_result):
         result = raw_result.split('''id=res''')[1].split('<b>')[1].split('</b>')[0]
         return result

if __name__=='__main__':
    g = GCalc()
    while True:
        print "G>>>",
        query = raw_input()
        print g.calc(query)

