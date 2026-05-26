# The Tomb of Knowledge / 知识冢

《知识冢》是一款 Ren'Py 制作的乡土现实恐怖叙事游戏。

## 游戏简介

女主在初中暑假回到老家，带着生物作业向种了一辈子地的爷爷请教化肥知识。她一直以为爷爷口中的"知识冢"是老人智慧聚集的地方，直到母亲纠正她：那不是"知识"，而是"支死"。

支死冢，是过去贫穷年代中，老人被时代和饥饿推向的最后归处。

本游戏的恐怖并不来自故乡本身，而来自那个让人没有选择的年代。

## 当前版本

v0.3-engine-stable

已完成：

- Ren'Py 工程模块化
- 中文字体支持
- 线索系统
- 调试面板
- Demo 模式
- 音频占位系统
- 音频语义封装
- 章节标题卡
- 测试清单

## 项目结构

```text
game/
├── 00_project_flags.rpy
├── 00_settings_cn.rpy
├── 01_characters.rpy
├── 02_assets.rpy
├── 03_state.rpy
├── 04_audio_safe.rpy
├── 05_clues.rpy
├── 06_dev_tools.rpy
├── 07_ui_style.rpy
├── 08_audio_events.rpy
├── 09_chapter_cards.rpy
├── 10_start.rpy
├── 20_story_prologue.rpy
├── ...
└── 31_demo_end.rpy
```

## 字体说明

本项目不上传中文字体文件。请自行在 `game/fonts/` 下放入支持中文的字体，并命名为：

```
chinese.ttf
```

## 开发状态

当前处于 Demo 开发阶段。

下一目标：

- 优化 Demo 结尾
- 替换真实音效
- 添加临时背景图
- 打包 Windows 试玩版
