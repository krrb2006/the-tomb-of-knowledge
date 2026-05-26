# -*- coding: utf-8 -*-
# 25_story_night.rpy
# 第五章：恐惧的夜

label fear_night:

    call chapter_card("第五章", "夜里的砖声")

    scene bg night
    with fade

    $ bgm_night()

    narrator "夜里，我躺在床上，怎么也睡不着。"

    narrator "我一闭眼，就想到妈妈说的那句话。"

    centered "人还活着的时候去的地方。"

    narrator "窗外有风。"

    narrator "远处好像有猫叫。"

    $ sfx_cat()
    voice "喵——"

    pause 0.6

    narrator "我忽然想起爷爷故事里的麻袋。"

    narrator "猫被装在里面。"

    narrator "老人被留在洞里。"

    narrator "我知道它们不是一回事。"

    narrator "可我的脑子偏要把它们放在一起。"

    $ sfx_brick()

    narrator "咚。"

    pause 0.4

    narrator "咚。"

    pause 0.4

    narrator "咚。"

    narrator "像有人在很远的地方垒砖。"

    menu:
        "蒙住被子":
            $ fear_score += 1
            narrator "我把被子拉过头顶。"

            narrator "可声音还是钻了进来。"

            narrator "不是从窗外。"

            narrator "是从我知道真相以后，心里自己响起来的。"

        "去找妈妈":
            $ understand_score += 1
            scene bg kitchen
            with fade

            narrator "妈妈还没睡。"

            narrator "她坐在灯下备课。"

            me "妈妈，我害怕。"

            mother "我知道。"

            me "我一想到那个地方，就觉得老家也变得可怕。"

            mother "老家不可怕。"

            mother "可怕的是那个让人没得选的年代。"

            mother "你要分清楚。"

        "去院子里看一眼":
            $ fear_score += 1
            scene bg yard
            with fade

            narrator "院子里很黑。"

            narrator "爷爷站在井边，看着远处的山。"

            me "爷爷，你听见了吗？"

            grandpa "听见什么？"

            me "砖声。"

            grandpa "邻居家垒猪圈，白天剩的砖没搬完。"

            narrator "我不知道他说的是不是真的。"

            narrator "可我知道，就算声音是假的，我的害怕是真的。"

    $ stop_bgm()

    jump village_elders
