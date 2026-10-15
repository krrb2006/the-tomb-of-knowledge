# -*- coding: utf-8 -*-
# 02_assets.rpy
# 背景资源定义：优先使用旧版试玩中的原始配图，资源缺失时才回退纯色。

image bg black = Solid("#050505")

init python:
    def safe_image(name, path, fallback_color):
        if renpy.loadable(path):
            renpy.image(name, Transform(path, fit="cover"))
        else:
            renpy.image(name, Solid(fallback_color))

    safe_image("bg title",     "images/ui/title_bg.png",          "#080806")
    safe_image("bg yard",      "images/bg/bg_yard.png",           "#2b241c")
    safe_image("bg old_house", "images/bg/bg_old_house.png",      "#201914")
    safe_image("bg storage",   "images/bg/bg_storage.png",        "#16120f")
    safe_image("bg field",     "images/bg/bg_field.png",          "#1f2a18")
    safe_image("bg kitchen",   "images/bg/bg_kitchen.png",        "#231c17")
    safe_image("bg night",     "images/bg/bg_night_yard.png",     "#08090d")
    safe_image("bg village",   "images/bg/bg_village.png",        "#242424")
    safe_image("bg gully",     "images/bg/bg_gully.png",          "#090909")
    safe_image("bg memory",    "images/bg/bg_memory_dark.png",   "#1a1512")
    safe_image("bg morning",   "images/bg/bg_morning_field.png", "#262018")
    safe_image("bg future",    "images/bg/bg_future_village.png","#202820")
