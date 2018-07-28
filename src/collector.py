#! /usr/bin/env python
# -*- coding: utf-8 -*-

from urllib import request

from bs4 import BeautifulSoup


# 数据爬取
class Collector(object):

    @staticmethod
    def collect(url, phpsessid, content_output_path, time_output_path):
        base_url = url
        content_file = open(content_output_path, 'w', encoding='utf-8')
        time_file = open(time_output_path, 'w', encoding='utf-8')

        page_num = 0
        while True:
            page_num = page_num + 1
            # 拼接url
            req = request.Request(base_url + '/p.' + str(page_num))
            req.add_header('Host', 'fanfou.com')
            req.add_header('User-agent',
                           'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0')
            req.add_header('Referer', 'http://fanfou.com/home')
            req.add_header('Cookie', 'PHPSESSID=' + phpsessid)

            # 访问url
            res = request.urlopen(req)
            html = res.read()
            page = BeautifulSoup(html, "html.parser")

            stream = page.find(name='div', attrs={'id': 'stream'})
            if stream is None:
                break

            # if page_num > 500:
            #     break

            # 提取所有日记
            list_items = stream.find_all(name='li')
            if list_items is not None and len(list_items) > 0:
                for item in list_items:
                    content = item.find(name='span', attrs={'class': 'content'}).text
                    time = item.find(name='a', attrs={'class': 'time'}).text

                    if len(content) > 0:
                        # 保存日记内容
                        content_file.write(content)
                        content_file.write('\n')

                        # 保存日记时间
                        time_file.write(time)
                        time_file.write('\n')

                        # 打印日记时间和内容
                        print('%s %s' % (time, content))
