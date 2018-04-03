#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ref: https://www.cnblogs.com/masako/p/5868367.html

from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        """
        recognize start tag, like <div>
        :param tag:
        :param attrs:
        :return:
        """
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        """
        recognize end tag, like </div>
        :param tag:
        :return:
        """
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        """
        recognize data, html content string
        :param data:
        :return:
        """
        print("Encountered some data  :", data)

    def handle_startendtag(self, tag, attrs):
        """
        recognize tag that without endtag, like <img />
        :param tag:
        :param attrs:
        :return:
        """
        print("Encountered startendtag :", tag)

    def handle_comment(self,data):
        """

        :param data:
        :return:
        """
        print("Encountered comment :", data)


parser = MyHTMLParser()
parser.feed('<html><head><title>Test</title></head>'
            '<body><h1>Parse me!内容</h1><img src = "" />'
            '<p>abc'
            '<!-- comment --></body></html>')


