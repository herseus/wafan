#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 挖饭，一款用于饭否的Python爬虫工具

from src.analyzer import Analyzer
from src.collector import Collector

# 挖饭入口
if __name__ == '__main__':

    # url 为你关注的人的主页
    # 张小龙的饭否主页
    url = 'http://fanfou.com/~RLhcIDBjZAM'
    # 王兴的饭否主页
    # url = 'http://fanfou.com/wangxing'

    # phpsessid 为登录饭否后的phpsessionid，到Cookies中找phpsessid
    # 不登录饭否无法访问别人的饭否
    phpsessid = 't4cjka7f4nedrmmq7dubipji16'

    # 日记内容保存路径
    content_file_path = 'data/content.txt'

    # 日记时间保存路径
    time_file_path = 'data/time.txt'

    # 词云图片保存路径
    content_png_path = 'data/content.png'

    # 统计时间柱状图保存路径
    time_png_path = 'data/time.png'

    # 爬取数据
    # url: 某个人的饭否主页
    # phpsessid: 登录饭否后浏览器 Cookie 中的值
    # content_file_path: 日记内容保存路径
    # time_file_path: 日记时间保存路径
    Collector.collect(url, phpsessid, content_file_path, time_file_path)

    # 分词，制作词云
    # content_file_path: 日记内容保存路径
    # content_png_path: 词云图片保存路径
    Analyzer.segment_and_visualize(content_file_path, content_png_path)

    # 统计发日记时间
    # time_file_path: 日记时间保存路径
    # time_png_path: 时间柱状图保存路径
    Analyzer.count_times(time_file_path, time_png_path)
