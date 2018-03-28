# -*-coding:utf-8-*-
import sys
from PyQt5 import QtWidgets

from jd import html_downloader, html_parser, html_outputer
from jd.price_monitor import Ui_Form


class SpiderMain(object):
    def __init__(self):
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, url):
        if url is None:
            return

        html_content = self.downloader.download(url)
        new_data = self.parser.parser(url, html_content)
        print('craw %s : %s' % (url, new_data))
        return new_data
        # self.outputer.collect_data(new_data)
        # self.outputer.output_html()

if __name__ == "__main__":
    # urls = ["https://item.jd.com/1993087.html", "https://item.jd.com/1993089.html"]
    # obj_spider = SpiderMain()
    # obj_spider.craw(urls)
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
