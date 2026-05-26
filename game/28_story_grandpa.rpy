# -*- coding: utf-8 -*-
# 28_story_grandpa.rpy
# 第八章：爷爷的话

label grandpa_truth:

    call chapter_card("第八章", "不是应该，是没得选")

    scene bg old_house
    with fade

    narrator "傍晚，我回到家。"

    narrator "爷爷坐在门槛上。"

    narrator "他好像早就知道我去了哪里。"

    me "爷爷。"

    grandpa "嗯。"

    me "支死冢……到底为什么会有？"

    narrator "爷爷沉默了很久。"

    grandpa "因为穷。"

    me "穷就可以这样吗？"

    grandpa "不可以。"

    narrator "我愣住了。"

    grandpa "我没说它对。"

    grandpa "那不是应该。"

    grandpa "那是没得选。"

    $ clue_grandpa_truth = True
    $ understand_score += 1
    $ add_clue("grandpa_truth", "爷爷的解释", "爷爷说：支死冢不是应该，是没得选。那时候的人不是不知道疼，只是穷到没有别的办法。")

    me "可是老人也是人。"

    grandpa "是人。"

    grandpa "他们自己也知道自己是人。"

    grandpa "我们也知道。"

    me "那为什么还要送去？"

    grandpa "一锅稀饭，五个人分，七个人等。"

    grandpa "你说怎么办？"

    narrator "我张了张嘴。"

    narrator "我想说，不该这样。"

    narrator "可是爷爷已经先说了不该。"

    narrator "我想说，他们残忍。"

    narrator "可是妈妈说，那不是一个人的坏。"

    me "那鼠灾的老人呢？"

    grandpa "他是真的聪明。"

    grandpa "猫装麻袋那个办法，也是他出的。"

    me "他救了粮食。"

    grandpa "嗯。"

    me "那后来呢？"

    narrator "爷爷低下头。"

    grandpa "后来砖还是砌满了。"

    narrator "我鼻子一酸。"

    me "如果他那么有智慧，为什么还是救不了自己？"

    grandpa "因为智慧不能当饭吃。"

    grandpa "至少那时候不能。"

    narrator "堂屋里静得厉害。"

    grandpa "你现在觉得害怕，是好事。"

    me "为什么大家都这么说？"

    grandpa "因为你害怕，说明你没把它当成理所当然。"

    grandpa "说明你生在好时候。"

    grandpa "也说明以后不能再让日子坏回去。"

    menu:
        "说：我还是觉得它很可怕":
            $ fear_score += 1
            me "我还是觉得它很可怕。"

            grandpa "可怕就记着。"

            grandpa "别拿它吓人，也别拿它当故事显摆。"

            grandpa "记着就行。"

        "说：我不想讨厌老家":
            $ future_score += 2
            me "我不想讨厌老家。"

            grandpa "老家也没让你讨厌。"

            grandpa "那是老年头的事。"

            grandpa "故乡也被那年月饿过。"

        "问：读书真的有用吗？":
            $ future_score += 2
            me "读书真的有用吗？"

            grandpa "有用。"

            me "你以前不是说种地靠手吗？"

            grandpa "靠手，也靠脑子。"

            grandpa "更靠日子越来越好。"

            grandpa "你们读书，就是让日子别坏回去。"

    jump final_choice
