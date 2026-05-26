# -*- coding: utf-8 -*-
# 10_start.rpy
# 游戏入口

label start:

    show screen dev_button
    show screen clue_button

    scene bg black
    with fade

    if not renpy.loadable("fonts/chinese.ttf"):
        system "没有检测到 game/fonts/chinese.ttf。"
        system "如果中文显示成方框或乱码，请在 game/fonts/ 下放入中文字体，并命名为 chinese.ttf。"
        system "如果你现在能正常看到中文，也可以暂时继续运行。"

    scene bg title
    with fade

    centered "知识冢"

    pause 0.8

    centered "我以为老人留下的是知识。"

    pause 0.8

    centered "后来我知道，他们留下的是自己。"

    pause 0.8

    centered "再后来我明白，知识要做的事，是不让后来的人也变成这样的牺牲。"

    pause 1.0

    centered "本游戏包含关于饥饿年代、老人死亡与乡村旧俗的沉重叙事。"

    centered "它不是为了猎奇乡村，也不是为了美化苦难。"

    centered "恐怖的是过去，不是故乡。"

    pause 1.5

    jump prologue
