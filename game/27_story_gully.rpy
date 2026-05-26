# -*- coding: utf-8 -*-
# 27_story_gully.rpy
# 第七章：山沟旧址

label gully_visit:

    call chapter_card("第七章", "一日一饭，一日一砖")

    scene bg field
    with fade

    narrator "下午，我一个人去了田边。"

    narrator "那块黑土田旁边，有一条被草遮住的小路。"

    narrator "我知道它通向哪里。"

    menu:
        "沿着小路去山沟":
            $ fear_score += 1
            jump gully_scene

        "先回家找妈妈一起去":
            $ understand_score += 1
            scene bg kitchen
            with fade

            me "妈妈，我想去看看。"

            mother "去看可以。"

            mother "但你要记住，那里不是鬼屋。"

            mother "那里是一些人最后没办法去的地方。"

            me "嗯。"

            jump gully_scene


label gully_scene:

    scene bg gully
    with fade

    narrator "山沟比我想象中安静。"

    narrator "没有鬼。"

    narrator "没有哭声。"

    narrator "只有草、石头、塌下去的土坡，还有一些埋了一半的旧砖。"

    narrator "我看见一只碎碗。"

    narrator "又看见一块长满青苔的石头。"

    narrator "石头上的字已经很浅。"

    narrator "我用手擦掉泥。"

    centered "一日一饭，一日一砖。"

    $ clue_gully_stone = True
    $ add_clue("gully_stone", "山沟石刻", "山沟旧址的石头上刻着：一日一饭，一日一砖。那不是诅咒，而是旧时代的规矩。")

    narrator "我终于懂了。"

    narrator "饭让人多活一天。"

    narrator "砖让死亡更近一天。"

    narrator "这不是传说。"

    narrator "也不是鬼故事。"

    narrator "这是规矩。"

    narrator "比鬼故事更可怕的规矩。"

    narrator "我蹲在石头前，忽然想起生物书上的一句话。"

    centered "有机肥来自动植物遗体分解形成的腐殖质。"

    narrator "我以前觉得这句话很自然。"

    narrator "叶落归根，万物循环。"

    narrator "可现在，我再看脚下的黑土，忽然不敢只说它肥了。"

    narrator "老人活着时，把力气给了田，把粮食让给孩子，把经验留给后人。"

    narrator "到了最后，连死亡也像被算进了一年的收成里。"

    narrator "我说不清这是奉献，还是牺牲。"

    narrator "我只觉得害怕。"

    if demo_mode:
        jump demo_end
    else:
        jump grandpa_truth
