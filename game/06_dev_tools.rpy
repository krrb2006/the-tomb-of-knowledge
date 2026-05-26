# -*- coding: utf-8 -*-
# 06_dev_tools.rpy
# 开发调试工具
# 正式发布前，把 dev_panel_enabled 改成 False

default dev_panel_enabled = DEV_MODE

init python:
    def grant_all_clues():
        store.clue_sack = True
        store.clue_bowl = True
        store.clue_brick = True
        store.clue_black_soil = True
        store.clue_mother_correction = True
        store.clue_elder_words = True
        store.clue_gully_stone = True
        store.clue_grandpa_truth = True
        store.fear_score = 3
        store.understand_score = 3
        store.future_score = 5
        add_clue("black_soil", "异常肥沃的黑土", "田边有一块不用怎么施肥也长得很好的黑土。爷爷说：老地，自己肥。")
        add_clue("sack", "旧麻袋", "麻袋内侧有很深的抓痕。爷爷说，过去村里人曾把猫装进麻袋里，用猫叫吓退老鼠。")
        add_clue("bowl", "破饭碗", "破碗底下刻着「送饭」两个字。")
        add_clue("brick", "半块旧砖", "半块旧砖边缘磨得很光，砖面上有类似指甲刮过的痕迹。")
        add_clue("mother_correction", "母亲的纠正", "妈妈说，不是「知识冢」，是「支死冢」。支着等死的支死。")
        add_clue("elder_words", "村里老人的话", "村口老人说：以前怕，现在不怕了。因为现在没人会把我们送去了。")
        add_clue("gully_stone", "山沟石刻", "山沟旧址的石头上刻着：一日一饭，一日一砖。")
        add_clue("grandpa_truth", "爷爷的解释", "爷爷说：支死冢不是应该，是没得选。")
        renpy.notify("已获得全部测试线索")


screen dev_button():
    zorder 999
    if dev_panel_enabled:
        textbutton "调试":
            xpos 0.02
            ypos 0.03
            action Show("dev_panel")
            background "#00000099"
            hover_background "#333333cc"
            text_color "#ffcc66"
            text_hover_color "#ffffff"


screen dev_panel():
    modal True
    zorder 1000
    add Solid("#000000cc")
    frame:
        xalign 0.5
        yalign 0.5
        xsize 950
        ysize 650
        background "#181818ee"
        padding (30, 30)
        vbox:
            spacing 16
            text "开发调试面板" size 36 color "#ffcc66"
            text "章节跳转" size 26 color "#ffffff"
            grid 3 5:
                spacing 10
                textbutton "序章" action [Hide("dev_panel"), Jump("prologue")]
                textbutton "肥料谜题" action [Hide("dev_panel"), Jump("fertilizer_lesson")]
                textbutton "鼠灾故事" action [Hide("dev_panel"), Jump("rat_story")]
                textbutton "杂物间" action [Hide("dev_panel"), Jump("storage_chapter")]
                textbutton "母亲纠正" action [Hide("dev_panel"), Jump("mother_correction")]
                textbutton "夜晚恐惧" action [Hide("dev_panel"), Jump("fear_night")]
                textbutton "村里老人" action [Hide("dev_panel"), Jump("village_elders")]
                textbutton "山沟旧址" action [Hide("dev_panel"), Jump("gully_visit")]
                textbutton "爷爷解释" action [Hide("dev_panel"), Jump("grandpa_truth")]
                textbutton "最终选择" action [Hide("dev_panel"), Jump("final_choice")]
                textbutton "母亲结局" action [Hide("dev_panel"), Jump("ending_mother")]
                textbutton "真结局" action [Hide("dev_panel"), Jump("ending_true")]
                textbutton "安静结局" action [Hide("dev_panel"), Jump("ending_quiet")]
                textbutton "标题入口" action [Hide("dev_panel"), Jump("start")]
                textbutton "关闭" action Hide("dev_panel")
            null height 10
            text "测试工具" size 26 color "#ffffff"
            hbox:
                spacing 16
                textbutton "一键获得全部线索":
                    action Function(grant_all_clues)
                textbutton "关闭调试按钮":
                    action SetVariable("dev_panel_enabled", False)
                textbutton "关闭面板":
                    action Hide("dev_panel")
