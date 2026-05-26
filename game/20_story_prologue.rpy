# -*- coding: utf-8 -*-
# 20_story_prologue.rpy
# 序章：生物作业

label prologue:

    call chapter_card("序章", "生物作业")

    scene bg yard
    with fade

    narrator "初二那年暑假，我回了老家。"

    narrator "老家的院子很大，土墙发黄，屋檐下挂着玉米，风吹过去，玉米叶子哗啦啦地响。"

    narrator "我带着一本没写完的生物作业。"

    narrator "那一页讲的是植物生长。"

    narrator "题目问："

    centered "植物生长需要无机盐。请说明氮肥、磷肥、钾肥对植物生长的作用。"

    narrator "我盯着那几个字看了很久。"

    narrator "氮。磷。钾。"

    narrator "它们像三种我背不熟的咒语。"

    cousin "姐，你会不会？"

    narrator "表妹趴在桌边，也拿着一本生物书。"

    me "我……大概会一点。"

    narrator "我嘴上这么说，心里其实也没底。"

    narrator "爷爷正在田边翻土。"

    narrator "他种了一辈子地。"

    narrator "我忽然觉得，这种题问他应该比问课本更有用。"

    me "走，问爷爷去。"

    jump fertilizer_lesson
