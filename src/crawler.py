# -*- coding: utf-8 -*-

'''
Created on 2018. 9. 17.

@author: jason96
'''

from selenium import webdriver
from pyutil.fileutil import write_file
import time


def crawl():

    target_urls = []
    try:
        for page in range(1, 18):
            base_url = 'http://berlinstartupjobs.com/engineering/'
            if page != 1:
                base_url = base_url + '/page/' + str(page)
            driver = webdriver.Chrome('../util/chromedriver')
            driver.get(base_url)
            xpath = '//div[@class="product-listing-item"]'
            for elem in driver.find_elements_by_xpath(xpath):
                href = elem.find_element_by_class_name('product-listing-h2')\
                    .find_element_by_tag_name('a')\
                    .get_attribute('href')
                target_urls.append(href)
            driver.close()
            time.sleep(1)

    finally:
        write_file('urls.txt', '\n'.join(target_urls))


if __name__ == '__main__':
    crawl()
