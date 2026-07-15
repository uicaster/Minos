Minos - 系统监控小工具
Minos - System Monitor Tool

Windows 桌面悬浮监控面板，实时展示 CPU 温度、CPU 占用率、内存使用量和网络速度。 A floating Windows desktop monitor that displays CPU temperature, CPU usage, memory usage, and network speed in real time.

特性
Features

悬浮置顶 — 始终在桌面最上层，不影响其他窗口操作 Always on top — stays above other windows without interfering.
隐藏至托盘 — 关闭窗口自动隐藏到系统托盘，后台持续监控 Minimize to tray — closing the window hides it to the system tray for background monitoring.
沉浸模式 — 隐藏窗口边框并锁定位置，融入桌面背景 Immersive mode — hides window borders and locks position, blending into the desktop.
透明背景 — 沉浸模式下可选透明背景，仅显示监控文字 Transparent background — optional transparent background in immersive mode, showing only text.
显示选项 — 自由开关 CPU 温度 / CPU 占用率 / 内存 / 网络速度四项（至少保留一项） Display options — toggle CPU temperature, CPU usage, memory, and network speed (at least one remains visible).
温度单位 — 支持摄氏度和华氏度切换 Temperature unit — switch between Celsius and Fahrenheit.
七语言 — 中文 / English / 日本語 / 한국어 / Español / Português / Français Seven languages — Chinese / English / Japanese / Korean / Spanish / Portuguese / French.
开机自启 — 托盘菜单一键开启/关闭 Auto-start — toggle on/off from the tray menu.
超低资源占用 — 单文件 exe，约 32MB，内存占用极低 Ultra-low footprint — single exe file (~32MB) with minimal memory usage.
运行方式
Running

在 main.py 同级目录下执行： Run from the project directory:

pythonw main.py
或运行打包后的 Minos.exe，启动后出现在系统托盘。 Or launch the packaged Minos.exe. The app appears in the system tray on startup.

从源码构建
Building from Source

pyinstaller Minos.spec --distpath . --noconfirm
exe 输出到项目根目录。 The exe is output to the project root directory.

版本历史
Changelog

v1.12.0 — 七语言国际化
Seven-language internationalization

支持中文 / English / 日本語 / 한국어 / Español / Português / Français，托盘菜单新增「语言」子菜单，主界面标签、菜单文字、关于对话框、托盘 Tooltip 全部可切换。 Added language switching for all 7 languages. New "Language" submenu in the tray. Labels, menu text, about dialog, and tray tooltip all update on switch.

v1.10.1 — 显示选项子菜单
Display options submenu

托盘菜单增加「显示选项」子菜单，可勾选 CPU 温度 / CPU 占用率 / 内存 / 网络速度四项目标，至少保留一项。窗口高度动态适应可见行数。 Added "Display Options" submenu to toggle visibility of all four metrics. Window height dynamically adapts to visible rows.

v1.10.0 — CPU 占用与内存显示
CPU usage and memory display

新增 CPU 占用率（鹅黄色）和内存使用量（蓝色 已用/总量 GB）两行，窗口扩大至 310×280。 Added CPU usage (amber) and memory usage (blue, "used/total GB") rows. Window enlarged to 310×280.

v1.9.0 — 透明背景
Transparent background

沉浸模式下新增「透明背景」选项，窗口背景变为透明仅显示文字。退出沉浸模式自动关闭透明背景。 Added "Transparent Background" option in immersive mode. Background becomes transparent, showing only text. Auto-disabled when exiting immersive mode.

v1.6.0 — 托盘菜单与沉浸模式
Tray menu and immersive mode

托盘右键菜单添加沉浸模式切换（隐藏边框并锁定位置）、开机自启选项、关于弹窗。窗口缩小至 340×260。 Added immersive mode toggle, auto-start option, and about dialog to the tray right-click menu. Window reduced to 340×260.

v1.0.0 — 初始版本
Initial release

系统托盘悬浮窗口，实时展示 CPU 温度和网络上传/下载速度。温度采集优先级：LHM → PerfFormattedData → ACPI WMI。托盘图标通过 PIL ImageDraw 绘制纯数字。 Floating tray window showing CPU temperature and network upload/download speed in real time. Temperature sources: LHM → PerfFormattedData → ACPI WMI. Tray icon drawn as a number via PIL ImageDraw.

版权方：上海市宝山区千语网络科技工作室 
Copyright: Qianyu Network Technology Studio, Baoshan District, Shanghai 
