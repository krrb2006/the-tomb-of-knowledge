# -*- coding: utf-8 -*-
# 04_audio_safe.rpy
# 安全音效系统：文件存在就播放，不存在就跳过

init python:
    def safe_play_sound(filename, volume=1.0):
        loadable = renpy.loadable(filename)
        if loadable:
            try:
                # Relative track gain respects the player's sound-mixer setting.
                renpy.sound.play(filename, relative_volume=volume)
            except Exception as e:
                renpy.notify("音效播放失败: {}".format(filename))
        else:
            renpy.notify("音效文件未找到: {}".format(filename))

    def safe_play_music(filename, volume=1.0):
        loadable = renpy.loadable(filename)
        if loadable:
            try:
                # Do not mutate the persistent music-channel preference.
                renpy.music.play(filename, loop=True, relative_volume=volume)
            except Exception as e:
                renpy.notify("音乐播放失败: {}".format(filename))
        else:
            renpy.notify("音乐文件未找到: {}".format(filename))

    def safe_stop_music():
        renpy.music.stop()
