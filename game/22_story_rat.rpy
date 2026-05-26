# -*- coding: utf-8 -*-
# 22_story_rat.rpy
# 第二章：鼠灾故事

label rat_story:

    call chapter_card("第二章", "麻袋里的猫")

    scene bg old_house
    with fade

    $ heard_rat_story = True

    narrator "晚上，堂屋里只开了一盏灯。"

    narrator "灯泡外面绕着飞虫。爷爷坐在门槛上，烟袋锅一明一暗。"

    grandpa "很早以前，村里闹过鼠灾。"

    grandpa "那时候粮食本来就少，老鼠还来糟蹋。"

    grandpa "咬粮袋，啃柜子，夜里拖着玉米跑。"

    cousin "老鼠有什么可怕的？"

    grandpa "饿时候，老鼠比鬼可怕。"

    narrator "爷爷说，村里人没办法，就去山沟那边问老人。"

    grandpa "那老人住在支死冢里。"

    narrator "那个词落进我耳朵里时，自动变成了另一个好听得多的词。"

    narrator "知识冢。"

    narrator "我以为那是个藏着老人智慧的地方。"

    me "知识冢？"

    grandpa "嗯。你先听故事。"

    grandpa "那老人说，不用毒，不用打。"

    grandpa "抓一只猫，装进麻袋里。"

    grandpa "别让猫出来，就让它叫。"

    grandpa "老鼠听见猫叫，就不敢出洞。第二天天亮，人一堵，一抓一个准。"

    cousin "真的有用？"

    grandpa "有用。"

    me "这就是天敌关系吧？"

    grandpa "你们书上会这么说。"

    me "那个老人真聪明。"

    grandpa "是聪明。"

    narrator "爷爷吐出一口烟。"

    grandpa "可聪明也不一定能救自己。"

    narrator "我又一次没听懂。"

    narrator "我只是记住了那个名字。"

    centered "知识冢。"

    narrator "我觉得那应该是个很神秘、很古老、很有智慧的地方。"

    grandpa "杂物间里好像还有旧麻袋。"

    grandpa "明天你要是好奇，可以去找找。"

    jump storage_chapter
