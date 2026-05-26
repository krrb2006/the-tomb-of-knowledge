# -*- coding: utf-8 -*-
# 21_story_fertilizer.rpy
# 第一章：化肥与土地

label fertilizer_lesson:

    call chapter_card("第一章", "氮长叶，磷长根，钾壮秆")

    scene bg field
    with fade

    narrator "中午的田里很亮，太阳照在水渠上，晃得人睁不开眼。"

    narrator "爷爷蹲在田埂边，手里抓着一把黑土。"

    me "爷爷，氮肥、磷肥、钾肥分别是干什么的？"

    grandpa "你们现在书上还考这个？"

    me "考。"

    grandpa "氮长叶，磷长根，钾壮秆。"

    cousin "这么简单？"

    grandpa "种地人说话就这样。简单，好记。"

    me "爷爷你还懂生物啊？"

    grandpa "我不懂生物。"

    grandpa "我懂地。"

    narrator "爷爷把手里的土慢慢撒回田里。"

    grandpa "书上讲肥，地里讲命。"

    me "什么意思？"

    grandpa "你现在还小。先把作业写对。"

    narrator "爷爷指着旁边三小块地。"

    grandpa "我考考你。"

    grandpa "第一块，叶子发黄，苗也矮。该补什么？"

    menu:
        "氮肥":
            $ learned_fertilizer = True
            $ future_score += 1
            grandpa "对。氮长叶。叶子黄，苗弱，多半缺氮。"

        "磷肥":
            grandpa "磷管根。这个不是主要问题。"

        "钾肥":
            grandpa "钾壮秆。叶子发黄，不先补它。"

    grandpa "第二块，根弱，开花少。该补什么？"

    menu:
        "氮肥":
            grandpa "叶子不是最要紧。根不行，先看磷。"

        "磷肥":
            $ future_score += 1
            grandpa "对。磷长根，也管开花结果。"

        "钾肥":
            grandpa "钾是壮秆抗倒伏。"

    grandpa "第三块，茎细，风一吹就倒。该补什么？"

    menu:
        "氮肥":
            grandpa "氮多了，叶子旺，秆不一定硬。"

        "磷肥":
            grandpa "根不是这块最要紧的毛病。"

        "钾肥":
            $ future_score += 1
            grandpa "对。钾壮秆。"

    narrator "我把爷爷的话记在本子上。"

    me "氮长叶，磷长根，钾壮秆。"

    cousin "比老师讲得好记。"

    grandpa "老师讲得细，我讲得粗。都得听。"

    narrator "他说完，带我们走到另一块田边。"

    narrator "那块田的土特别黑，庄稼长得也密。"

    me "这块施了很多肥吗？"

    grandpa "这块不用怎么施。"

    me "为什么？"

    grandpa "老地。自己肥。"

    me "有机肥吗？"

    narrator "爷爷看了我一眼。"

    grandpa "也可以这么说。"

    $ clue_black_soil = True
    $ add_clue("black_soil", "异常肥沃的黑土", "田边有一块不用怎么施肥也长得很好的黑土。爷爷说：老地，自己肥。")

    narrator "那时候我还没有觉得这句话奇怪。"

    narrator "我只觉得爷爷真懂。"

    me "还是老人有智慧。"

    narrator "爷爷的手停了一下。"

    grandpa "老人是有智慧。"

    grandpa "可有时候，有智慧也救不了自己。"

    narrator "我没听懂。"

    narrator "于是爷爷给我们讲了一个很久以前的故事。"

    jump rat_story
