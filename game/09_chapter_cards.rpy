# -*- coding: utf-8 -*-
# 09_chapter_cards.rpy
# 章节标题卡 —— 每章开头调用，增强节奏感

label chapter_card(title, subtitle=""):
    scene bg black
    with fade
    centered "{size=44}[title]{/size}"
    if subtitle != "":
        pause 0.5
        centered "{size=26}[subtitle]{/size}"
    pause 0.8
    return
