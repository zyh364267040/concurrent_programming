# -*- coding = utf-8 -*-
# @Time: 2021/8/31 下午11:12
import subprocess


proc = subprocess.Popen(
    ['open', 'datas/余生一个浪.mp3']
)

if __name__ == '__main__':
    proc.communicate()
