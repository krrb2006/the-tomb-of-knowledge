# -*- coding: utf-8 -*-
# 31_demo_end.rpy
# Demo 结束页

label demo_end:

    scene bg black
    with fade

    narrator "我站在山沟口，看着那行被青苔盖住的字。"

    centered "一日一饭，一日一砖。"

    narrator "那一刻，我终于明白。"

    narrator "所谓支死冢，不是坟。"

    narrator "坟是人死后去的地方。"

    narrator "支死冢，是人还活着的时候，被送去等死的地方。"

    pause 0.8

    narrator "我第一次觉得，课本上的「肥力」两个字，也会让人害怕。"

    pause 0.8

    centered "《知识冢》Demo 完"

    pause 0.8

    centered "恐怖的不是故乡。"

    centered "恐怖的是那个让人没有选择的年代。"

    $ demo_clue_count = clue_count()

    scene bg memory
    with fade

    centered "知识冢 · 可试玩版本"

    narrator "这一程，你在故事里留下了 [demo_clue_count] 条线索。"

    narrator "感谢你走到这里。更多故事仍在田埂另一端。"

    menu:
        "重新开始这段 Demo":
            $ renpy.full_restart()

        "结束试玩，回到标题":
            return
