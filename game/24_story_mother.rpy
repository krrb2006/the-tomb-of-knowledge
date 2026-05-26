# -*- coding: utf-8 -*-
# 24_story_mother.rpy
# 第四章：母亲纠正

label mother_correction:

    call chapter_card("第四章", "不是知识")

    scene bg kitchen
    with fade

    narrator "傍晚，妈妈坐在厨房的小桌旁批改作业。"

    narrator "她是镇上的老师。"

    narrator "红笔在纸上划过，发出很轻的沙沙声。"

    me "妈妈，爷爷昨天讲的那个知识冢，到底在哪？"

    narrator "红笔停住了。"

    mother "什么冢？"

    me "知识冢啊。"

    me "爷爷说以前村里闹鼠灾，去知识冢问老人。"

    narrator "妈妈抬起头，看了我很久。"

    mother "你听错了。"

    me "啊？"

    mother "不是知识。"

    narrator "她把红笔放下。"

    mother "是支死。"

    me "哪个支死？"

    mother "支着等死的支死。"

    scene bg old_house
    with fade

    narrator "我忽然想起爷爷昨晚讲故事时说过的话。"

    grandpa "那老人住在支死冢里。"

    centered "支死冢。"

    narrator "原来他说的一直是这个。"

    narrator "不是知识。"

    narrator "是支死。"

    scene bg kitchen
    with fade

    $ clue_mother_correction = True
    $ fear_score += 2
    $ add_clue("mother_correction", "母亲的纠正", "妈妈说，不是「知识冢」，是「支死冢」。支着等死的支死。")

    narrator "我一开始没反应过来。"

    narrator "那两个字像一块冷砖，突然塞进了我胸口。"

    me "什么叫……支着等死？"

    mother "那是很早以前的事了。"

    me "是坟吗？"

    mother "不是。"

    narrator "妈妈的声音很低。"

    mother "坟是人死了以后去的地方。"

    mother "支死冢，是人还活着的时候去的地方。"

    narrator "厨房里很安静。"

    narrator "灶台上的水壶咕嘟响了一声。"

    me "你们一直说的是这个？"

    mother "一直是这个。"

    me "那我为什么一直听成知识？"

    mother "你那时候小。"

    mother "又总觉得老人懂得多，什么都能往知识上想。"

    me "那爷爷为什么不纠正我？"

    mother "也许他以为你长大就会明白。"

    me "这太吓人了。"

    mother "是吓人。"

    narrator "妈妈没有否认。"

    mother "所以别把它当成什么神秘故事。"

    mother "也别把它当成鬼故事。"

    mother "那是以前的人真的过过的日子。"

    menu:
        "问妈妈：你不觉得这很残忍吗？":
            $ understand_score += 1
            me "你不觉得这很残忍吗？"

            mother "当然残忍。"

            mother "我是老师，我教学生人要有尊严，要珍惜生命。"

            mother "可也正因为我是老师，我不能把它只讲成几个坏人做坏事。"

            mother "那不是一个人的坏。"

            mother "那是穷，是饿，是没有办法。"

        "问妈妈：那老人为什么不逃？":
            $ fear_score += 1
            me "那老人为什么不逃？"

            mother "你现在问得出来，是因为你没见过真正走不动的人。"

            mother "有些老人病了，饿了，腿也不行了。"

            mother "不是不想走，是走不了。"

        "沉默，不想再听":
            narrator "我低下头。"

            narrator "我忽然不想知道了。"

            mother "不想听就先不听。"

            mother "你还小。害怕也正常。"

    narrator "那天晚上，我第一次觉得老家的黑不是天黑。"

    narrator "是有什么旧东西，从土里慢慢浮了出来。"

    jump fear_night
