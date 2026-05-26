# -*- coding: utf-8 -*-
# 26_story_elders.rpy
# 第六章：村里老人

label village_elders:

    call chapter_card("第六章", "现在不怕了")

    scene bg village
    with fade

    narrator "第二天，我在村口遇见几个晒太阳的老人。"

    narrator "他们坐在槐树下面，摇着蒲扇，旁边放着茶杯。"

    narrator "他们看上去并不可怕。"

    narrator "甚至很普通。"

    oldwoman "你是老刘家的孙女吧？"

    me "嗯。"

    oldwoman "长这么高了。"

    narrator "我犹豫了很久，还是问了出来。"

    me "奶奶，你知道支死冢吗？"

    narrator "几个老人都看了过来。"

    narrator "我以为他们会变脸。"

    narrator "但他们没有。"

    oldwoman "知道啊。"

    oldwoman "老早以前的事了。"

    me "你们不害怕吗？"

    elder "以前怕。"

    elder "现在不怕了。"

    me "为什么？"

    elder "现在没人会把我们送去了。"

    $ clue_elder_words = True
    $ understand_score += 1
    $ add_clue("elder_words", "村里老人的话", "村口老人说：以前怕，现在不怕了。因为现在没人会把我们送去了。")

    narrator "他说得很平静。"

    narrator "可那平静让我更难受。"

    me "那你们觉得那是对的吗？"

    oldwoman "现在看，当然不对。"

    oldwoman "可那时候，不对的事多了。"

    elder "人饿到一定时候，想的就不是对不对。"

    elder "想的是明天谁还有饭吃。"

    me "可是老人也是人。"

    oldwoman "谁说不是呢？"

    narrator "老太太把蒲扇放在膝盖上。"

    oldwoman "老人也知道自己是人。"

    oldwoman "所以有些老人，自己说要去。"

    me "为什么？"

    oldwoman "怕小的饿死。"

    narrator "我说不出话。"

    elder "你觉得吓人，是好事。"

    me "这为什么是好事？"

    elder "说明你没过过那种日子。"

    elder "说明现在日子好了。"

    narrator "那一刻，我忽然明白，他们的淡然不是冷漠。"

    narrator "是劫后余生。"

    jump gully_visit
