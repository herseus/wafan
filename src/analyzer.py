#! /usr/bin/env python
# -*- coding: utf-8 -*-

import collections
import re

import jieba
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from wordcloud import WordCloud


# 文本分析，先用结巴分词，然后生成词云，数据放在data目录下
class Analyzer(object):

    # 对文本进行分词，并生成词云
    @staticmethod
    def segment_and_visualize(content_file_path, content_png_path):
        f = open(content_file_path, 'r', encoding='utf-8')
        text = f.read()
        f.close()

        f = open('utils/stopwords.txt', 'r', encoding='utf-8')
        stopwords = {}.fromkeys(f.read().split('\n'))
        f.close()

        jieba.load_userdict('utils/jieba_user_dict.txt')
        segs = jieba.cut(text)

        mytext_list = []
        for seg in segs:
            if seg not in stopwords and seg != ' ' and len(seg) != 1:
                mytext_list.append(seg.replace(' ', ''))

        mytext_count = collections.Counter(mytext_list)
        cloud_mask = np.array(Image.open('bg_img/circle.png'))

        sw = set(['东西', '这是'])
        wc = WordCloud(background_color='white',
                       mask=cloud_mask,
                       max_words=2000,
                       font_path='utils/qingningyouyuan.ttf',
                       min_font_size=22,
                       max_font_size=80,
                       # width=100,
                       stopwords=sw)
        wc.generate_from_frequencies(mytext_count)
        wc.to_file(content_png_path)

    # 统计发表日记时间，生成柱状图
    @staticmethod
    def count_times(time_file_path, time_png_path):
        count_for_24_hours = [0 for x in range(24)]
        regex = re.compile('(\d+):')

        time_file = open(time_file_path, 'r', encoding='utf-8')

        timestamps = time_file.read().split('\n')

        for timestamp in timestamps:
            if len(timestamp) > 0:
                if re.search(regex, timestamp) is not None:
                    hour = re.search(regex, timestamp).group(1)
                    hour = int(hour)
                    count_for_24_hours[hour] += 1

        print(count_for_24_hours)

        name_list = [x for x in range(24)]
        plt.barh(range(len(count_for_24_hours)), count_for_24_hours, color='#74D3F2', tick_label=name_list)
        plt.savefig(time_png_path)
