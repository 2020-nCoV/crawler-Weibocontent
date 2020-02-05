# -*- coding: UTF-8 -*-

import copy
import csv
import os
import sys
import traceback


def get_filepath(type, nickname):
    """获取结果文件路径"""
    file_dir = os.path.split(
        os.path.realpath(__file__))[0] + os.sep + 'weibo' + os.sep + nickname
    if type == 'img' or type == 'video':
        file_dir = file_dir + os.sep + type
    if not os.path.isdir(file_dir):
        os.makedirs(file_dir)
    if type == 'img' or type == 'video':
        return file_dir
    file_path = file_dir + os.sep + nickname + '.' + type
    return file_path


def write_log(since_date):
    """当程序因cookie过期停止运行时，将相关信息写入log.txt"""
    file_dir = os.path.split(
        os.path.realpath(__file__))[0] + os.sep + 'weibo' + os.sep
    if not os.path.isdir(file_dir):
        os.makedirs(file_dir)
    file_path = file_dir + 'log.txt'
    content = u'cookie已过期，从%s到今天的微博获取失败，请重新设置cookie\n' % since_date
    with open(file_path, 'ab') as f:
        f.write(content.encode(sys.stdout.encoding))


class Writer:
    def __init__(self, config):
        self.writer = CsvWriter(config)

    def write_user(self, user):
       self.writer.write_user(user)

    def write_weibo(self, weibo):
       self.writer.write_weibo(weibo)



class CsvWriter:
    def __init__(self, config):
        self.config = config

    def write_user(self, user):
        self.user = user
        result_headers = [
            '微博名称',
            '地点',
            '日期',
            '一天发文数',
            '与疫情相关',
            '疫情相关占比'
        ]
        if not self.config['filter']:
            result_headers.insert(-1, '被转发微博原始图片url')
            result_headers.insert(-1, '是否为原创微博')


        with open(get_filepath('csv', self.user['nickname']),
                  'a',
                  encoding='utf-8-sig',
                  newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerows([result_headers])

    def write_weibo(self, weibo):
        """将爬取的信息写入csv文件"""
        result_data = []
        for index in weibo:
            result_data.append(index)


        with open(get_filepath('csv', self.user['nickname']),
                  'a',
                  encoding='utf-8-sig',
                  newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(result_data)

        print(u'%d条微博写入csv文件完毕,保存路径:' % len(weibo))
        print(get_filepath('csv', self.user['nickname']))


