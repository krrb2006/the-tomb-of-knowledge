# -*- coding: utf-8 -*-
# 00_project_flags.rpy
# 项目模式开关 —— 正式发布时只需改这里

# init -100 保证在任何其他 init 块之前执行，不受文件排序影响
init -100 python:
    # Release-safe defaults. Enable locally only while testing.
    DEV_MODE = False

    # 是否启用 Demo 断点（关闭后进入完整剧情）
    DEMO_BUILD = True

    # Never generate assets as a side effect of launching a player build.
    AUTO_AUDIO_PLACEHOLDER = False
