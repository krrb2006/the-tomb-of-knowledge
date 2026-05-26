# -*- coding: utf-8 -*-
# 00_settings_cn.rpy
# 中文字体与基础界面设置

init 999 python:
    chinese_font = "fonts/chinese.ttf"

    if renpy.loadable(chinese_font):
        gui.text_font = chinese_font
        gui.name_text_font = chinese_font
        gui.interface_text_font = chinese_font

        style.default.font = chinese_font
        style.say_dialogue.font = chinese_font
        style.say_label.font = chinese_font
        style.choice_button_text.font = chinese_font
        style.button_text.font = chinese_font
        style.input.font = chinese_font
