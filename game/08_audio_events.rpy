# -*- coding: utf-8 -*-
# 08_audio_events.rpy
# 游戏音效语义封装 —— 剧情里调用这些函数，换文件名只需改这里

init python:
    def sfx_cat():
        safe_play_sound("audio/cat_meow.mp3", volume=0.6)

    def sfx_brick():
        safe_play_sound("audio/brick_hit.mp3", volume=0.5)

    def sfx_pencil():
        safe_play_sound("audio/pencil_write.mp3", volume=0.4)

    def bgm_night():
        safe_play_music("audio/night_wind.mp3", volume=0.35)

    def stop_bgm():
        safe_stop_music()
