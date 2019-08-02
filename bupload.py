# -*- coding:utf-8 -*-
from bilibiliupload import *
import logging
logging.basicConfig(level=logging.DEBUG)

b = Bilibili()

login_status = b.login('15073124380', 'zhang1314nmopM')
print("Login:", login_status)

videoPart1 = VideoPart("爆笑星际虚空之遗-aDE9VCYAnc8.mp4", '爆笑星际虚空之遗-aDE9VCYAnc8.mp4')
videoPart2 = VideoPart("TheBeast vs AlphaStar [ZvZ] Deepmind A.I. Starcraft 2-ckbVqwhkY60.mkv", '已发现的欧服天梯阿尔法星replay(三)ZVZ')
videoPart3 = VideoPart("Alphastar vs Stekepanne [TvZ] Deepmind A.I. Starcraft 2-hVy47vr5WaI.mkv", '已发现的欧服天梯阿尔法星replay(四)TVZ')



tags = {u"星际争霸2", u"AlphaStar", u"人工智能", u"机器人", u"暴雪游戏"}
tags = {u"星际争霸2", u"动画", u"搞笑", u"暴雪游戏",u"游戏CG"}

b.upload(parts=videoPart1, title='爆笑星际mod版的虚空之遗CG宣传片', tid=65, tag=tags, desc='爆笑星际mod版的虚空之遗CG宣传片',source="https://www.youtube.com/watch?v=aDE9VCYAnc8",open_elec=1)

b.upload(parts=videoPart2, title='已发现的欧服天梯阿尔法星replay(三)ZVZ', tid=65, tag=tags, desc='已发现的欧服天梯阿尔法星replay(三)ZVZ',source="https://www.youtube.com/watch?v=ckbVqwhkY60",cover=b.cover_up("cover.jpg"),open_elec=1)

b.upload(parts=videoPart3, title='已发现的欧服天梯阿尔法星replay(四)TVZ', tid=65, tag=tags, desc='已发现的欧服天梯阿尔法星replay(四)TVZ',source="https://www.youtube.com/watch?v=hVy47vr5WaI",cover=b.cover_up("cover.jpg"),open_elec=1)



