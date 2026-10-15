# -*- coding: utf-8 -*-
# 08_audio_events.rpy
# 游戏音效语义封装 —— 剧情里调用这些函数，换文件名只需改这里

init python:
    def sfx_cat():
        safe_play_sound("audio/cat_meow.wav")

    def sfx_brick():
        safe_play_sound("audio/brick_hit.wav")

    def sfx_pencil():
        safe_play_sound("audio/pencil_write.wav")

    def bgm_night():
        safe_play_music("audio/night_wind.wav")

    def stop_bgm():
        safe_stop_music()
