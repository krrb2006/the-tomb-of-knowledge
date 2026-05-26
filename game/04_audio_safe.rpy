# -*- coding: utf-8 -*-
# 04_audio_safe.rpy
# 安全音效系统：文件存在就播放，不存在就跳过

init python:
    def safe_play_sound(filename):
        if renpy.loadable(filename):
            renpy.sound.play(filename)

    def safe_play_music(filename):
        if renpy.loadable(filename):
            renpy.music.play(filename, loop=True)

    def safe_stop_music():
        renpy.music.stop()
