# -*-coding:utf-8-*-
import ssl
import urllib.request


class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None

        response = urllib.request.urlopen(url)

        if response.code != 200:
            return None

        return response.read()

    ssl._create_default_https_context = ssl._create_unverified_context
