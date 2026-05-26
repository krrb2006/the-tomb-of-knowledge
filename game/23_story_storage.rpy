# -*- coding: utf-8 -*-
# 23_story_storage.rpy
# 第三章：杂物间

label storage_chapter:

    call chapter_card("第三章", "旧物")

    scene bg storage
    with fade

    narrator "第二天，我去了老屋后面的杂物间。"

    narrator "门一推开，灰尘扑了出来。"

    narrator "里面堆着旧农具、竹筐、瓦罐，还有一股潮湿的土腥味。"

    jump storage_menu


label storage_menu:

    menu:
        "调查角落里的旧麻袋":
            if not clue_sack:
                $ clue_sack = True
                $ add_clue("sack", "旧麻袋", "麻袋内侧有很深的抓痕。爷爷说，过去村里人曾把猫装进麻袋里，用猫叫吓退老鼠。")
                narrator "麻袋被压在竹筐下面。"

                narrator "我把它拖出来时，里面的干草哗啦响。"

                narrator "麻袋内侧有几道很深的抓痕。"

                me "应该是猫抓的吧。"

            else:
                narrator "旧麻袋安静地瘫在地上。"
                narrator "那些抓痕还在那里。"

            jump storage_menu

        "调查木架下的破饭碗":
            if not clue_bowl:
                $ clue_bowl = True
                $ fear_score += 1
                $ add_clue("bowl", "破饭碗", "破碗底下刻着「送饭」两个字。它不像普通饭碗，更像某种旧规矩留下来的东西。")
                narrator "木架下面扣着一只破碗。"

                narrator "碗边缺了一块，碗底有两个很浅的字。"

                centered "送饭"

                me "给谁送饭？"

            else:
                narrator "破碗底下的字还在那里。"
                narrator "送饭。"

            jump storage_menu

        "调查墙角的半块砖":
            if not clue_brick:
                $ clue_brick = True
                $ fear_score += 1
                $ add_clue("brick", "半块旧砖", "半块旧砖边缘磨得很光，砖面上有类似指甲刮过的痕迹。")
                narrator "墙角堆着几块旧砖。"

                narrator "其中一块只有半截，边缘磨得很光。"

                narrator "砖面上像是被什么硬东西刮过。"

                cousin "姐，这砖有什么好看的？"

                me "不知道。"

                narrator "我也不知道。可我莫名觉得它不该在这里。"

            else:
                narrator "半块砖摸起来很凉。"

            jump storage_menu

        "离开杂物间":
            narrator "我拍掉手上的灰。"

            narrator "旧麻袋、破饭碗、半块砖。"

            narrator "它们都不像真正恐怖的东西。"

            narrator "可我心里有一点不舒服。"

            jump mother_correction
