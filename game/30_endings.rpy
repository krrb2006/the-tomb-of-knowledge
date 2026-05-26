# -*- coding: utf-8 -*-
# 30_endings.rpy
# 所有结局

# ------------------------------------------------------------
# 结局一：安静结局
# ------------------------------------------------------------

label ending_quiet:

    scene bg morning
    with fade

    narrator "最后，我只写下了标准答案。"

    centered "有机肥能改善土壤结构，提高土壤肥力。"

    narrator "字写得很工整。"

    narrator "老师应该会给我打对。"

    narrator "可那天以后，我再看到田边那条小路，还是会绕开。"

    narrator "我没有讨厌老家。"

    narrator "我只是暂时还不知道，应该怎么面对那个故事。"

    centered "结局：暂时不问"

    return


# ------------------------------------------------------------
# 结局二：母亲的解释
# ------------------------------------------------------------

label ending_mother:

    scene bg kitchen
    with fade

    narrator "我把那天知道的事写进了日记。"

    narrator "写到一半，我停下来问妈妈。"

    me "我这样写，会不会像在讲鬼故事？"

    mother "你怎么写的？"

    narrator "我把本子推给她。"

    narrator "妈妈看了很久。"

    mother "可以害怕。"

    mother "但别只写害怕。"

    me "那还要写什么？"

    mother "写他们为什么会走到那一步。"

    mother "写那时候没有粮，没有药，没有养老。"

    mother "也写现在为什么不能再那样。"

    me "妈妈，你是不是也害怕？"

    mother "怕。"

    mother "所以我当老师。"

    mother "我希望你们这一代知道生命很重，也知道知识有用。"

    narrator "我低头看着本子。"

    narrator "第一次觉得，写字也像在垒砖。"

    narrator "但这一次，不是为了封住谁。"

    narrator "是为了让后来的人看见。"

    centered "结局：母亲的解释"

    return


# ------------------------------------------------------------
# 真结局：知识真正的意思
# ------------------------------------------------------------

label ending_true:

    scene bg morning
    with fade

    narrator "那天晚上，我没有逃回城里，也没有讨厌老家。"

    narrator "我坐在灯下，把生物作业写完。"

    narrator "标准答案写在前面。"

    centered "氮长叶，磷长根，钾壮秆。"

    centered "有机肥经微生物分解后形成腐殖质，可以改善土壤结构，提高土壤肥力。"

    narrator "然后，我在最后一页写下另一段话。"

    me "我以前以为，老人留下的是知识。"

    me "后来我知道，他们留下的是自己。"

    me "再后来我明白，知识要做的事，是不让后来的人也变成这样的牺牲。"

    scene bg field
    with fade

    narrator "第二天早晨，我和爷爷去了田边。"

    narrator "风吹过庄稼，叶子翻出一层浅浅的光。"

    grandpa "还怕吗？"

    me "怕。"

    grandpa "怕就别往那边去了。"

    me "不是。"

    narrator "我看向山沟的方向。"

    me "我不是怕这里。"

    me "我是怕那样的日子再回来。"

    narrator "爷爷很久没有说话。"

    grandpa "那就好好读书。"

    me "读书能让地多打粮吗？"

    grandpa "能。"

    me "能让老人不用被送进山沟吗？"

    grandpa "也能。"

    narrator "他说得很轻。"

    narrator "但这一次，我听懂了。"

    scene bg future
    with fade

    narrator "后来，我还是离开了老家。"

    narrator "但那不是逃离。"

    narrator "我去上学，去考试，去学那些爷爷说不清名字的肥料、土壤、病虫害、医疗、养老和人的尊严。"

    narrator "很多年后，村里的路修好了。"

    narrator "山沟旁立了护栏。"

    narrator "老人们坐在村口晒太阳，手里拿着养老金存折，互相笑话谁家的菜长得不好。"

    narrator "孩子们放学从田埂上跑过去，书包一晃一晃。"

    narrator "他们知道山沟那边有一个很旧很旧的名字。"

    narrator "但那只是过去。"

    narrator "不是将来。"

    centered "知识不是用来美化苦难的。"

    centered "知识是用来让苦难不再发生的。"

    pause 1.0

    centered "结局：知识真正的意思"

    return
