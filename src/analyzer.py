# -*- coding: utf-8 -*-

'''
Created on 2018. 9. 17.

@author: jason96
'''
from pyutil.fileutil import read_file
import operator


def analyzer():
    urls = read_file('urls.txt')
    urls = urls.replace('http://berlinstartupjobs.com/engineering/', '')
    urls = urls.replace('/', '')
    urls = urls.replace('\n', '-')
    frequency = {}
    for word in urls.split('-'):
        count = frequency.get(word, 0)
        frequency[word] = count + 1

    items = sorted(frequency.items(), key=operator.itemgetter(1), reverse=True)
    for x in items:
        print x


if __name__ == '__main__':
    analyzer()

