# -*- coding: utf-8 -*-
# 05_clues.rpy
# 线索系统 + 线索本界面

init python:
    def has_clue(clue_id):
        for c in clues:
            if c["id"] == clue_id:
                return True
        return False

    def add_clue(clue_id, title, desc):
        if not has_clue(clue_id):
            clues.append({
                "id": clue_id,
                "title": title,
                "desc": desc
            })
            renpy.notify("获得线索：" + title)

    def clue_count():
        return len(clues)


screen clue_button():

    zorder 100

    if len(clues) > 0:
        textbutton "线索":
            xpos 0.90
            ypos 0.03
            action Show("clue_book")
            background "#00000099"
            hover_background "#333333cc"
            text_color "#eeeeee"
            text_hover_color "#ffcc66"


screen clue_book():

    modal True
    zorder 200

    add Solid("#000000cc")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 920
        ysize 620
        background "#181818ee"
        padding (30, 30)

        vbox:
            spacing 18

            text "线索记录" size 36 color "#ffcc66"

            if len(clues) == 0:
                text "目前还没有获得任何线索。" size 24 color "#dddddd"

            else:
                viewport:
                    draggable True
                    mousewheel True
                    ysize 440

                    vbox:
                        spacing 18

                        for item in clues:
                            vbox:
                                spacing 6
                                text item["title"] size 28 color "#ffffff"
                                text item["desc"] size 22 color "#cccccc"

            textbutton "关闭":
                action Hide("clue_book")
                xalign 0.5
