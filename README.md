# Minos - System Monitor Tool

A floating Windows desktop monitor that displays CPU temperature, CPU usage, memory usage, and network speed in real time.

## Features

- **Always on top** — stays above other windows without interfering.
- **Minimize to tray** — closing the window hides it to the system tray for background monitoring.
- **Immersive mode** — hides window borders and locks position, blending into the desktop.
- **Transparent background** — optional transparent background in immersive mode, showing only text.
- **Display options** — toggle CPU temperature, CPU usage, memory, and network speed (at least one remains visible).
- **Temperature unit** — switch between Celsius and Fahrenheit.
- **Seven languages** — Chinese / English / Japanese / Korean / Spanish / Portuguese / French.
- **Auto-start** — toggle on/off from the tray menu.
- **Ultra-low footprint** — single exe file (~32MB) with minimal memory usage.

## Running

```bash
pythonw main.py
```

Or launch the packaged `Minos.exe`. The app appears in the system tray on startup.

## Building from Source

```bash
pyinstaller Minos.spec --distpath . --noconfirm
```

The exe is output to the project root directory.

## Changelog

### v1.12.0 — Seven-language internationalization

Added language switching for all 7 languages. New "Language" submenu in the tray. Labels, menu text, about dialog, and tray tooltip all update on switch.

### v1.10.1 — Display options submenu

Added "Display Options" submenu to toggle visibility of all four metrics. Window height dynamically adapts to visible rows.

### v1.10.0 — CPU usage and memory display

Added CPU usage (amber) and memory usage (blue, "used/total GB") rows. Window enlarged to 310×280.

### v1.9.0 — Transparent background

Added "Transparent Background" option in immersive mode. Background becomes transparent, showing only text. Auto-disabled when exiting immersive mode.

### v1.6.0 — Tray menu and immersive mode

Added immersive mode toggle, auto-start option, and about dialog to the tray right-click menu. Window reduced to 340×260.

### v1.0.0 — Initial release

Floating tray window showing CPU temperature and network upload/download speed in real time. Temperature sources: LHM → PerfFormattedData → ACPI WMI. Tray icon drawn as a number via PIL ImageDraw.

---

Copyright: Qianyu Network Technology Studio, Baoshan District, Shanghai
