# -*- coding:utf-8 -*-
from bilibiliupload import *
import logging
logging.basicConfig(level=logging.DEBUG)

b = Bilibili()

login_status = b.login('15073124380', 'zhang1314nmopM')
print("Login:", login_status)

videoPart1 = [VideoPart("Let's see how this robot boogies - AlphaStar Breakdown Pt. 1-8AfzMA3Cvio.mkv", '已发现的欧服天梯阿尔法星人族replay.mkv'),VideoPart("Let's see how this robot boogies - AlphaStar Breakdown Pt. 2-i1qBpgaSWHU.mkv", '已发现的欧服天梯阿尔法星虫族replay.mkv')]


tags = {u"星际争霸2", u"AlphaStar", u"人工智能", u"机器人", u"暴雪游戏"}

b.upload(parts=videoPart1, title='已发现的欧服天梯阿尔法星replay(二)', tid=65, tag=tags, desc='已发现的欧服天梯阿尔法星replay人族和虫族',cover=b.cover_up("cover.jpg"),open_elec=1)



