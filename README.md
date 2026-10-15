# 《知识冢》The Tomb of Knowledge

> 一款以乡土记忆为背景的现实主义叙事游戏。恐怖不来自故乡，而来自曾经让人没有选择的处境。

[浏览器试玩 Demo](https://krrb2006.github.io/the-tomb-of-knowledge/) · [源代码](https://github.com/krrb2006/the-tomb-of-knowledge)

## 项目简介

玩家跟随一名初中生回到乡下，在生物作业、祖辈口述和旧物线索之间，逐渐听清“知识冢”背后的真实含义。作品尝试把氮磷钾等课堂知识、家庭记忆与代际创伤编织进同一条叙事线，并避免把乡村或贫困本身当作猎奇对象。

当前仓库提供 Ren'Py 剧情源码、上一版试玩中的原始配图与华文行楷字体，以及音频资源；不包含 Ren'Py SDK 或打包产物。浏览器试玩是独立发布的 Demo 构建；修改源码后需要重新用 Ren'Py 构建并部署，试玩页不会自动从 `.rpy` 文件更新。

## 项目亮点

- **模块化叙事**：按序章、章节、结局拆分脚本，故事路由由 Ren'Py label 与明确的跳转关系组成。
- **线索收集**：调查旧麻袋、饭碗、砖块、石刻等可选线索，收集记录集中写入线索本。
- **状态驱动分支**：恐惧、理解、未来取向与线索数量共同影响结尾；Demo 在第七章形成清晰的试玩断点。
- **语义化音频层**：剧情只调用 `sfx_cat()`、`bgm_night()` 等事件名；缺失音频安全跳过，单条音轨增益不覆盖玩家的混音器偏好。
- **开发/发布分离**：调试面板和占位音频生成默认关闭；项目模式集中在 `game/00_project_flags.rpy`。
- **质量门禁**：零依赖静态验证会检查 label 路由、音频文件引用和发布默认值；GitHub Actions 在 push 与 pull request 上运行。

## 技术栈

- Ren'Py / Screen Language / Python（游戏内扩展）
- GitHub Actions + Python 标准库（源码静态检查）
- GitHub Pages（当前浏览器试玩 Demo）

## 运行源码

1. 安装 [Ren'Py SDK](https://www.renpy.org/latest.html)，在启动器中新建一个 **1280×720** 项目。
2. 将仓库 `game/` 中的 `.rpy` 文件和 `audio/` 资源复制到新项目的 `game/` 目录。保留启动器生成的 `screens.rpy`、`gui.rpy` 及 GUI 资源；本仓库的 `game/gui.rpy` 仅是占位说明。
3. `game/fonts/chinese.ttf` 是旧版试玩中的华文行楷字体；场景配图也已恢复到 `game/images/`。
4. 在启动器点击 **Launch Project**。修改 `game/00_project_flags.rpy` 可在本地开启开发面板、关闭 Demo 断点。

当前模式：`DEMO_BUILD = True`、`DEV_MODE = False`、`AUTO_AUDIO_PLACEHOLDER = False`。正式发布前请先完成素材授权核对，并以目标平台实际构建结果为准。

## 质量检查

本地运行（Python 3.10+，无第三方依赖）：

```bash
python tools/validate_project.py
```

该检查能发现静态 label/资源路由错误，但不能替代 Ren'Py 启动器的脚本编译、实际游玩、Web/桌面构建或人工叙事审阅。完整回归项目见 [`TEST_CHECKLIST.txt`](TEST_CHECKLIST.txt)。

## 项目结构

```text
game/
├── 00_project_flags.rpy     # 开发、Demo、资源占位开关
├── 01–09_*.rpy              # 角色、资源、状态、音频、线索、UI
├── 10_start.rpy             # 启动与内容提示
├── fonts/                   # 旧版试玩的华文行楷字体
├── images/bg/               # 旧版试玩场景配图
├── images/ui/               # 旧版试玩标题/界面配图
├── 20–29_story_*.rpy        # 序章、章节与最终选择
├── 30_endings.rpy           # 三种结局
└── 31_demo_end.rpy          # Demo 断点
tools/validate_project.py    # 无依赖静态质量门禁
```

## 简历描述（可按实际完成情况调整）

**《知识冢》｜Ren'Py 叙事游戏 Demo**

- 使用 Ren'Py 将章节化剧情、可调查线索、状态变量与多结局组织为可维护的叙事系统。
- 封装容错音频事件，保留玩家音量偏好，并区分开发工具与发布默认配置。
- 编写标准库静态验证器并接入 GitHub Actions，自动检查剧情目标、音频资源及发布开关。

> 请只保留你亲自验证过、能够在面试中讲清楚的内容。素材来源/授权信息仍需在发布前补全，详见 [`ASSET_CREDITS.md`](ASSET_CREDITS.md)。
