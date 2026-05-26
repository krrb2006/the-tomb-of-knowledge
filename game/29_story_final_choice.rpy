# -*- coding: utf-8 -*-
# 29_story_final_choice.rpy
# 最终选择

label final_choice:

    call chapter_card("终章", "知识真正的意思")

    scene bg kitchen
    with fade

    narrator "那天晚上，我又坐回了作业本前。"

    narrator "题目还是那道题。"

    centered "有机肥为什么能提高土壤肥力？"

    narrator "我拿起笔，却迟迟写不下去。"

    narrator "我知道标准答案。"

    narrator "有机肥含有丰富的有机质。"

    narrator "微生物分解后形成腐殖质。"

    narrator "可以改善土壤结构，提供植物生长所需养分。"

    narrator "可我脑子里总是出现那块石头。"

    centered "一日一饭，一日一砖。"

    mother "还写不下去？"

    me "妈妈。"

    mother "嗯。"

    me "我是不是不该觉得老家可怕？"

    mother "你可以害怕。"

    mother "但不要把害怕放错地方。"

    me "什么意思？"

    mother "恐怖的是过去。"

    mother "不是生你养你的故乡。"

    narrator "妈妈把我的生物书翻到那一页。"

    mother "你现在学这些，不是为了把苦难写得好听。"

    mother "是为了以后遇到苦难，有办法。"

    narrator "我看着书上的字。"

    menu:
        "只写标准答案，不再想这件事":
            jump ending_quiet

        "把这件事写进日记，问妈妈能不能这样记住":
            $ future_score += 1
            jump ending_mother

        "写下：我要好好学习，让支死冢离现在越来越远":
            $ future_score += 3
            if clue_count() >= 6:
                jump ending_true
            else:
                jump ending_mother
