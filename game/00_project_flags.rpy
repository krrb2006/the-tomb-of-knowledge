# -*- coding: utf-8 -*-
# 00_project_flags.rpy
# 项目模式开关 —— 正式发布时只需改这里

# init -100 保证在任何其他 init 块之前执行，不受文件排序影响
init -100 python:
    # 是否为开发模式（关闭后调试面板不显示）
    DEV_MODE = True

    # 是否启用 Demo 断点（关闭后进入完整剧情）
    DEMO_BUILD = True

    # 是否允许自动生成静默音频占位文件（正式打包时关闭）
    AUTO_AUDIO_PLACEHOLDER = True
