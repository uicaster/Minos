"""
Minos — 系统监控小工具
CPU温度 + 网络上下行速度，图标直接显示温度数值
"""

VERSION = "1.12.0"

# ============================================================
# 国际化
# ============================================================

LANGUAGES = {
    "zh": "中文",
    "en": "English",
    "ja": "日本語",
    "ko": "한국어",
    "es": "Español",
    "pt": "Português",
    "fr": "Français",
}

I18N = {
    "zh": {
        "cpu_temp_label": "CPU 温度",
        "cpu_usage_label": "CPU 占用",
        "memory_label": "内存",
        "upload_label": "▲ 上行",
        "download_label": "▼ 下行",
        "show_window": "显示窗口",
        "startup": "开机自启",
        "immersive": "沉浸模式",
        "transparent_bg": "透明背景",
        "display_options": "显示选项",
        "cpu_temp_option": "CPU温度",
        "cpu_usage_option": "CPU占用率",
        "memory_option": "内存占用率",
        "network_option": "网络速度",
        "temp_unit": "温度单位",
        "about": "关于",
        "exit": "退出",
        "language": "语言",
        "about_title": "关于 Minos",
        "about_desc": "系统监控小工具",
        "copyright": "版权方：上海市宝山区千语网络科技工作室",
        "tooltip_cpu": "CPU",
        "tooltip_cpu_usage": "CPU占用",
        "tooltip_memory": "内存",
        "tooltip_upload": "▲",
        "tooltip_download": "▼",
    },
    "en": {
        "cpu_temp_label": "CPU Temp",
        "cpu_usage_label": "CPU Usage",
        "memory_label": "Memory",
        "upload_label": "▲ Upload",
        "download_label": "▼ Download",
        "show_window": "Show Window",
        "startup": "Startup",
        "immersive": "Immersive",
        "transparent_bg": "Transparent BG",
        "display_options": "Display Options",
        "cpu_temp_option": "CPU Temp",
        "cpu_usage_option": "CPU Usage",
        "memory_option": "Memory",
        "network_option": "Network",
        "temp_unit": "Unit",
        "about": "About",
        "exit": "Exit",
        "language": "Language",
        "about_title": "About Minos",
        "about_desc": "System Monitor Tool",
        "copyright": "Copyright: Qianyu Network Technology Studio, Baoshan District, Shanghai",
        "tooltip_cpu": "CPU",
        "tooltip_cpu_usage": "CPU Usage",
        "tooltip_memory": "Memory",
        "tooltip_upload": "▲",
        "tooltip_download": "▼",
    },
    "ja": {
        "cpu_temp_label": "CPU 温度",
        "cpu_usage_label": "CPU 使用率",
        "memory_label": "メモリ",
        "upload_label": "▲ 送信",
        "download_label": "▼ 受信",
        "show_window": "表示",
        "startup": "起動時実行",
        "immersive": "没入モード",
        "transparent_bg": "透明背景",
        "display_options": "表示オプション",
        "cpu_temp_option": "CPU温度",
        "cpu_usage_option": "CPU使用率",
        "memory_option": "メモリ",
        "network_option": "ネットワーク",
        "temp_unit": "温度単位",
        "about": "情報",
        "exit": "終了",
        "language": "言語",
        "about_title": "Minos について",
        "about_desc": "システムモニターツール",
        "copyright": "Copyright: Qianyu Network Technology Studio, Baoshan District, Shanghai",
        "tooltip_cpu": "CPU",
        "tooltip_cpu_usage": "CPU使用率",
        "tooltip_memory": "メモリ",
        "tooltip_upload": "▲",
        "tooltip_download": "▼",
    },
    "ko": {
        "cpu_temp_label": "CPU 온도",
        "cpu_usage_label": "CPU 사용률",
        "memory_label": "메모리",
        "upload_label": "▲ 업로드",
        "download_label": "▼ 다운로드",
        "show_window": "창 표시",
        "startup": "시작프로그램",
        "immersive": "몰입 모드",
        "transparent_bg": "투명 배경",
        "display_options": "표시 옵션",
        "cpu_temp_option": "CPU 온도",
        "cpu_usage_option": "CPU 사용률",
        "memory_option": "메모리",
        "network_option": "네트워크",
        "temp_unit": "온도 단위",
        "about": "정보",
        "exit": "종료",
        "language": "언어",
        "about_title": "Minos 정보",
        "about_desc": "시스템 모니터 도구",
        "copyright": "Copyright: Qianyu Network Technology Studio, Baoshan District, Shanghai",
        "tooltip_cpu": "CPU",
        "tooltip_cpu_usage": "CPU 사용률",
        "tooltip_memory": "메모리",
        "tooltip_upload": "▲",
        "tooltip_download": "▼",
    },
    "es": {
        "cpu_temp_label": "Temp. CPU",
        "cpu_usage_label": "Uso CPU",
        "memory_label": "Memoria",
        "upload_label": "▲ Subida",
        "download_label": "▼ Bajada",
        "show_window": "Mostrar",
        "startup": "Inicio",
        "immersive": "Inmersivo",
        "transparent_bg": "Fondo Transp.",
        "display_options": "Opciones",
        "cpu_temp_option": "Temp. CPU",
        "cpu_usage_option": "Uso CPU",
        "memory_option": "Memoria",
        "network_option": "Red",
        "temp_unit": "Unidad Temp.",
        "about": "Acerca de",
        "exit": "Salir",
        "language": "Idioma",
        "about_title": "Acerca de Minos",
        "about_desc": "Monitor del Sistema",
        "copyright": "Copyright: Qianyu Network Technology Studio, Baoshan District, Shanghai",
        "tooltip_cpu": "CPU",
        "tooltip_cpu_usage": "Uso CPU",
        "tooltip_memory": "Memoria",
        "tooltip_upload": "▲",
        "tooltip_download": "▼",
    },
    "pt": {
        "cpu_temp_label": "Temp. CPU",
        "cpu_usage_label": "Uso CPU",
        "memory_label": "Memória",
        "upload_label": "▲ Upload",
        "download_label": "▼ Download",
        "show_window": "Mostrar",
        "startup": "Inicializar",
        "immersive": "Imersivo",
        "transparent_bg": "Fundo Transp.",
        "display_options": "Opções",
        "cpu_temp_option": "Temp. CPU",
        "cpu_usage_option": "Uso CPU",
        "memory_option": "Memória",
        "network_option": "Rede",
        "temp_unit": "Unidade Temp.",
        "about": "Sobre",
        "exit": "Sair",
        "language": "Idioma",
        "about_title": "Sobre o Minos",
        "about_desc": "Monitor do Sistema",
        "copyright": "Copyright: Qianyu Network Technology Studio, Baoshan District, Shanghai",
        "tooltip_cpu": "CPU",
        "tooltip_cpu_usage": "Uso CPU",
        "tooltip_memory": "Memória",
        "tooltip_upload": "▲",
        "tooltip_download": "▼",
    },
    "fr": {
        "cpu_temp_label": "Temp. CPU",
        "cpu_usage_label": "Util. CPU",
        "memory_label": "Mémoire",
        "upload_label": "▲ Montant",
        "download_label": "▼ Descendant",
        "show_window": "Afficher",
        "startup": "Démarrage",
        "immersive": "Immersif",
        "transparent_bg": "Fond Transp.",
        "display_options": "Options",
        "cpu_temp_option": "Temp. CPU",
        "cpu_usage_option": "Util. CPU",
        "memory_option": "Mémoire",
        "network_option": "Réseau",
        "temp_unit": "Unité Temp.",
        "about": "À propos",
        "exit": "Quitter",
        "language": "Langue",
        "about_title": "À propos de Minos",
        "about_desc": "Moniteur Système",
        "copyright": "Copyright: Qianyu Network Technology Studio, Baoshan District, Shanghai",
        "tooltip_cpu": "CPU",
        "tooltip_cpu_usage": "Util. CPU",
        "tooltip_memory": "Mémoire",
        "tooltip_upload": "▲",
        "tooltip_download": "▼",
    },
}

import tkinter as tk
from tkinter import messagebox
import threading
import time
import subprocess
import sys
import os
import logging

import winreg

import psutil
import pystray
from PIL import Image, ImageDraw, ImageFont

# 日志输出到项目目录
LOG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "minos.log")
logging.basicConfig(filename=LOG_PATH, level=logging.INFO,
                    format="%(asctime)s %(levelname)s: %(message)s")
log = logging.getLogger("minos")

# LibreHardwareMonitor（可选，需要管理员权限）
_LHM_COMPUTER = None
_LHM_AVAILABLE = False
_HT_CPU = 1      # 兜底值（HardwareType.Cpu）
_ST_TEMP = 2     # 兜底值（SensorType.Temperature）
try:
    import clr as _clr
    _lib = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "LibreHardwareMonitorLib.dll"
    )
    if os.path.exists(_lib):
        _clr.AddReference(_lib)
    else:
        # 从 HardwareMonitor 包查找 DLL
        import HardwareMonitor as _hm
        _hm_dir = os.path.dirname(_hm.__file__)
        _lib = os.path.join(_hm_dir, "lib", "LibreHardwareMonitorLib.dll")
        if os.path.exists(_lib):
            _clr.AddReference(_lib)
    from LibreHardwareMonitor.Hardware import Computer as LHMComputer
    from LibreHardwareMonitor.Hardware import HardwareType as _LHM_HWType
    from LibreHardwareMonitor.Hardware import SensorType as _LHM_SensorType
    _HT_CPU = _LHM_HWType.Cpu
    _ST_TEMP = _LHM_SensorType.Temperature
    _lhm = LHMComputer()
    _lhm.CPUEnabled = True
    _lhm.Open()
    if len(_lhm.Hardware) > 0:
        _LHM_COMPUTER = _lhm
        _LHM_AVAILABLE = True
        log.info("LibreHardwareMonitor initialized OK (%d hardware)", len(_lhm.Hardware))
    else:
        _lhm.Close()
        log.info("LibreHardwareMonitor: no hardware (need admin?)")
except Exception as e:
    log.info("LibreHardwareMonitor not available: %s", e)

# ============================================================
# 数据采集
# ============================================================

def get_cpu_temperature():
    """获取 CPU 温度（摄氏度），优先 LibreHardwareMonitor，回退到 ACPI WMI。"""
    global _LHM_COMPUTER, _LHM_AVAILABLE
    # 方案1：LibreHardwareMonitor
    if _LHM_AVAILABLE and _LHM_COMPUTER is not None:
        try:
            temps = []
            for hw in _LHM_COMPUTER.Hardware:
                if hw.HardwareType == _HT_CPU:
                    hw.Update()
                    for s in hw.Sensors:
                        if s.SensorType == _ST_TEMP and s.Value is not None:
                            temps.append(float(s.Value))
                    for ss in hw.SubHardware:
                        ss.Update()
                        for s in ss.Sensors:
                            if s.SensorType == _ST_TEMP and s.Value is not None:
                                temps.append(float(s.Value))
            if temps:
                return round(max(temps), 1)
        except Exception as e:
            log.warning("LHM failed, fallback to ACPI: %s", e)
            try:
                _LHM_COMPUTER.Close()
            except Exception:
                pass
            _LHM_COMPUTER = None
            _LHM_AVAILABLE = False

    # 方案2：Win32_PerfFormattedData（高频更新）
    try:
        si = subprocess.STARTUPINFO()
        si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        si.wShowWindow = subprocess.SW_HIDE

        cmd = (
            'Get-CimInstance Win32_PerfFormattedData_Counters_ThermalZoneInformation '
            '-ErrorAction Stop | Select-Object -ExpandProperty HighPrecisionTemperature'
        )
        result = subprocess.run(
            ['powershell', '-NoProfile', '-Command', cmd],
            capture_output=True, text=True, timeout=5,
            startupinfo=si
        )
        if result.returncode == 0 and result.stdout.strip():
            lines = result.stdout.strip().splitlines()
            temps = []
            for line in lines:
                try:
                    raw = float(line.strip())
                    temps.append((raw / 10.0) - 273.15)
                except ValueError:
                    continue
            if temps:
                return round(max(temps), 1)
    except Exception as e:
        log.warning("PerfFormattedData failed, fallback to ACPI: %s", e)

    # 方案3：ACPI WMI 后备（更新慢）
    try:
        si = subprocess.STARTUPINFO()
        si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        si.wShowWindow = subprocess.SW_HIDE

        cmd = (
            'Get-CimInstance -Namespace root/wmi -ClassName MSAcpi_ThermalZoneTemperature '
            '-ErrorAction Stop | Select-Object -ExpandProperty CurrentTemperature'
        )
        result = subprocess.run(
            ['powershell', '-NoProfile', '-Command', cmd],
            capture_output=True, text=True, timeout=5,
            startupinfo=si
        )
        if result.returncode == 0 and result.stdout.strip():
            lines = result.stdout.strip().splitlines()
            temps = []
            for line in lines:
                try:
                    raw = float(line.strip())
                    temps.append((raw / 10.0) - 273.15)
                except ValueError:
                    continue
            if temps:
                return round(max(temps), 1)
    except Exception as e:
        log.warning("get_cpu_temperature: %s", e)
    return None


def get_net_speed(prev_counters, prev_time):
    current = psutil.net_io_counters()
    now = time.time()
    elapsed = now - prev_time
    if elapsed <= 0 or prev_counters is None:
        return 0, 0, current, now
    recv = (current.bytes_recv - prev_counters.bytes_recv) / elapsed
    sent = (current.bytes_sent - prev_counters.bytes_sent) / elapsed
    return max(0, recv), max(0, sent), current, now


def format_speed(bytes_per_sec):
    bits = bytes_per_sec * 8
    if bits >= 1e9:
        return f"{bits / 1e9:.2f}", "Gbps"
    elif bits >= 1e6:
        return f"{bits / 1e6:.2f}", "Mbps"
    else:
        return f"{bits / 1e3:.1f}", "Kbps"


def get_cpu_usage():
    """返回 CPU 整体占用百分比（浮点数）。首次调用返回 0.0。"""
    return psutil.cpu_percent()


def get_memory_usage():
    """返回 (used_gb, total_gb) 内存使用量。"""
    mem = psutil.virtual_memory()
    return mem.used / (1024 ** 3), mem.total / (1024 ** 3)


# ============================================================
# 图标绘制
# ============================================================

def _load_font(size):
    for fp in [
        "C:\\Windows\\Fonts\\arialbd.ttf",
        "C:\\Windows\\Fonts\\segoeuib.ttf",
        "C:\\Windows\\Fonts\\msyhbd.ttc",
        "C:\\Windows\\Fonts\\consolab.ttf",
        "C:\\Windows\\Fonts\\consola.ttf",
        "C:\\Windows\\Fonts\\arial.ttf",
    ]:
        try:
            return ImageFont.truetype(fp, size)
        except (IOError, OSError):
            continue
    return ImageFont.load_default()


def draw_tray_icon(temp_value, display_value=None):
    size = 64
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    if temp_value is not None:
        if temp_value < 60:
            bg = "#00ADF7"
        elif temp_value < 90:
            bg = "#F09B59"
        else:
            bg = "#F00307"
    else:
        bg = "#1e1e2e"

    if display_value is None:
        display_value = temp_value
    text = f"{int(display_value)}" if display_value is not None else "--"

    draw.rectangle([0, 0, size - 1, size - 1], fill=bg)
    font = _load_font(44)
    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text(((size - tw) // 2, (size - th) // 2 - 4), text, fill="#ffffff", font=font)
    return img


def make_icon_ico(path):
    """生成 ℃ 图标文件（32x32 .ico）。"""
    img = Image.new("RGBA", (32, 32), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    font = _load_font(24)
    text = "℃"
    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text(((32 - tw) // 2, (32 - th) // 2 - 2), text, fill="#fab387", font=font)
    img.save(path, format="ICO", sizes=[(32, 32)])
    return path


# ============================================================
# GUI
# ============================================================

class MinosApp:
    def __init__(self):
        self.root = tk.Tk()
        self.lang = "zh"
        self.root.title(f"Minos - {self._t('about_desc')}")
        self.root.geometry("330x260")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e2e")
        self.root.attributes("-topmost", True)
        self.root.protocol("WM_DELETE_WINDOW", self.hide_window)

        # 窗口 / 任务栏图标
        self._setup_window_icon()

        self.prev_counters = None
        self.prev_time = time.time()
        self.running = True
        self._stop_event = threading.Event()

        self._startup_enabled = self._check_startup()
        self.immersive = False
        self.transparent_bg = False
        self._saved_geometry = None
        self.celsius = True
        self.show_temp = True
        self.show_cpu = True
        self.show_mem = True
        self.show_net = True

        # 标签引用（供语言切换后更新文本）
        self._label_refs = {}

        self._build_ui()
        self._setup_tray()

        # 首次刷新触发（延迟确保 UI 就绪）
        self.root.after(100, self._trigger_first_refresh)

        self.root.mainloop()

    def _setup_window_icon(self):
        # PyInstaller 打包后资源在 sys._MEIPASS；开发环境在同目录
        if getattr(sys, 'frozen', False):
            tp = os.path.join(sys._MEIPASS, "minos_icon.ico")
        else:
            tp = os.path.join(os.path.dirname(os.path.abspath(__file__)), "minos_icon.ico")
        if not os.path.exists(tp):
            try:
                make_icon_ico(tp)
            except Exception as e:
                log.warning("make_icon_ico failed: %s", e)
                return
        try:
            self.root.iconbitmap(default=tp)
        except Exception as e:
            log.warning("iconbitmap failed: %s", e)

    # ----- UI -----

    def _build_ui(self):
        font_title = ("Microsoft YaHei UI", 11, "bold")
        font_value = ("Consolas", 18, "bold")
        font_unit = ("Consolas", 18, "bold")
        fg_label = "#a6adc8"
        bg = "#1e1e2e"

        # 数值列宽度：format_speed 最大输出如 "1000.0" (6字符)，温度如 "100.0" (5字符)
        VAL_W = 10
        UNIT_W = 5
        LABEL_W = 10  # 左侧标签固定宽度，确保数值/单位列垂直对齐

        # --- 温度行 ---
        self.frame_temp = tk.Frame(self.root, bg=bg)
        self.frame_temp.pack(fill=tk.X, padx=10, pady=8)
        self._label_refs["cpu_temp"] = tk.Label(
            self.frame_temp, text=self._t("cpu_temp_label"),
            font=font_title, fg=fg_label, bg=bg, width=LABEL_W, anchor="w")
        self._label_refs["cpu_temp"].pack(side=tk.LEFT, anchor="s")
        ft_inner = tk.Frame(self.frame_temp, bg=bg)
        ft_inner.pack(side=tk.RIGHT, anchor="s")
        self.lbl_temp = tk.Label(
            ft_inner, text="--", font=font_value, fg="#fab387", bg=bg,
            width=VAL_W, anchor="e"
        )
        self.lbl_temp.grid(row=0, column=0)
        self.lbl_temp_unit = tk.Label(
            ft_inner, text="°C", font=font_unit, fg=fg_label, bg=bg,
            width=UNIT_W, anchor="w"
        )
        self.lbl_temp_unit.grid(row=0, column=1)

        # --- CPU 占用 ---
        self.frame_cpu = tk.Frame(self.root, bg=bg)
        self.frame_cpu.pack(fill=tk.X, padx=10, pady=8)
        self._label_refs["cpu_usage"] = tk.Label(
            self.frame_cpu, text=self._t("cpu_usage_label"),
            font=font_title, fg=fg_label, bg=bg, width=LABEL_W, anchor="w")
        self._label_refs["cpu_usage"].pack(side=tk.LEFT, anchor="s")
        fc_inner = tk.Frame(self.frame_cpu, bg=bg)
        fc_inner.pack(side=tk.RIGHT, anchor="s")
        self.lbl_cpu = tk.Label(
            fc_inner, text="--", font=font_value, fg="#f9e2af", bg=bg,
            width=VAL_W, anchor="e"
        )
        self.lbl_cpu.grid(row=0, column=0)
        self.lbl_cpu_unit = tk.Label(
            fc_inner, text="%", font=font_unit, fg=fg_label, bg=bg,
            width=UNIT_W, anchor="w"
        )
        self.lbl_cpu_unit.grid(row=0, column=1)

        # --- 内存 ---
        self.frame_mem = tk.Frame(self.root, bg=bg)
        self.frame_mem.pack(fill=tk.X, padx=10, pady=8)
        self._label_refs["memory"] = tk.Label(
            self.frame_mem, text=self._t("memory_label"),
            font=font_title, fg=fg_label, bg=bg, width=LABEL_W, anchor="w")
        self._label_refs["memory"].pack(side=tk.LEFT, anchor="s")
        fm_inner = tk.Frame(self.frame_mem, bg=bg)
        fm_inner.pack(side=tk.RIGHT, anchor="s")
        self.lbl_mem = tk.Label(
            fm_inner, text="--", font=font_value, fg="#89b4fa", bg=bg,
            width=VAL_W, anchor="e"
        )
        self.lbl_mem.grid(row=0, column=0)
        self.lbl_mem_unit = tk.Label(
            fm_inner, text="GB", font=font_unit, fg=fg_label, bg=bg,
            width=UNIT_W, anchor="w"
        )
        self.lbl_mem_unit.grid(row=0, column=1)

        # --- 上行 ---
        self.frame_up = tk.Frame(self.root, bg=bg)
        self.frame_up.pack(fill=tk.X, padx=10, pady=8)
        self._label_refs["upload"] = tk.Label(
            self.frame_up, text=self._t("upload_label"),
            font=font_title, fg=fg_label, bg=bg, width=LABEL_W, anchor="w")
        self._label_refs["upload"].pack(side=tk.LEFT, anchor="s")
        fu_inner = tk.Frame(self.frame_up, bg=bg)
        fu_inner.pack(side=tk.RIGHT, anchor="s")
        self.lbl_up = tk.Label(
            fu_inner, text="--", font=font_value, fg="#f38ba8", bg=bg,
            width=VAL_W, anchor="e"
        )
        self.lbl_up.grid(row=0, column=0)
        self.lbl_up_unit = tk.Label(
            fu_inner, text="Kbps", font=font_unit, fg=fg_label, bg=bg,
            width=UNIT_W, anchor="w"
        )
        self.lbl_up_unit.grid(row=0, column=1)

        # --- 下行 ---
        self.frame_down = tk.Frame(self.root, bg=bg)
        self.frame_down.pack(fill=tk.X, padx=10, pady=8)
        self._label_refs["download"] = tk.Label(
            self.frame_down, text=self._t("download_label"),
            font=font_title, fg=fg_label, bg=bg, width=LABEL_W, anchor="w")
        self._label_refs["download"].pack(side=tk.LEFT, anchor="s")
        fd_inner = tk.Frame(self.frame_down, bg=bg)
        fd_inner.pack(side=tk.RIGHT, anchor="s")
        self.lbl_down = tk.Label(
            fd_inner, text="--", font=font_value, fg="#a6e3a1", bg=bg,
            width=VAL_W, anchor="e"
        )
        self.lbl_down.grid(row=0, column=0)
        self.lbl_down_unit = tk.Label(
            fd_inner, text="Kbps", font=font_unit, fg=fg_label, bg=bg,
            width=UNIT_W, anchor="w"
        )
        self.lbl_down_unit.grid(row=0, column=1)

    # ----- 国际化 -----

    def _t(self, key):
        """翻译指定 key，若当前语言无对应项则回退到中文。"""
        return I18N.get(self.lang, I18N["zh"]).get(key, I18N["zh"].get(key, key))

    def _update_ui_texts(self):
        """更新所有 UI 标签和窗口标题。"""
        self.root.title(f"Minos - {self._t('about_desc')}")
        for ref_key, key in [
            ("cpu_temp", "cpu_temp_label"),
            ("cpu_usage", "cpu_usage_label"),
            ("memory", "memory_label"),
            ("upload", "upload_label"),
            ("download", "download_label"),
        ]:
            if ref_key in self._label_refs:
                self._label_refs[ref_key].config(text=self._t(key))

    def _set_language(self, lang):
        self.lang = lang
        self._update_ui_texts()
        self._rebuild_menu()

    # ----- 启动项 -----

    STARTUP_KEY = r"Software\Microsoft\Windows\CurrentVersion\Run"
    STARTUP_VALUE = "Minos"

    def _check_startup(self):
        """检查是否已注册系统启动项（只读，返回 bool）。"""
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.STARTUP_KEY)
            winreg.QueryValueEx(key, self.STARTUP_VALUE)
            winreg.CloseKey(key)
            return True
        except FileNotFoundError:
            return False

    def _add_startup(self):
        """写入 HKCU Run 键。"""
        try:
            target = f'"{sys.executable}" "{os.path.abspath(__file__)}"'
            key = winreg.OpenKey(
                winreg.HKEY_CURRENT_USER, self.STARTUP_KEY,
                0, winreg.KEY_SET_VALUE,
            )
            winreg.SetValueEx(key, self.STARTUP_VALUE, 0, winreg.REG_SZ, target)
            winreg.CloseKey(key)
            logging.info("启动项已添加: %s", target)
        except Exception as e:
            logging.error("添加启动项失败: %s", e)

    def _remove_startup(self):
        """从 HKCU Run 键删除。"""
        try:
            key = winreg.OpenKey(
                winreg.HKEY_CURRENT_USER, self.STARTUP_KEY,
                0, winreg.KEY_SET_VALUE,
            )
            winreg.DeleteValue(key, self.STARTUP_VALUE)
            winreg.CloseKey(key)
            logging.info("启动项已移除")
        except FileNotFoundError:
            logging.info("启动项不存在，无需移除")
        except Exception as e:
            logging.error("移除启动项失败: %s", e)

    def _toggle_startup_menu(self):
        if self._startup_enabled:
            self._remove_startup()
        else:
            self._add_startup()
        self._startup_enabled = self._check_startup()
        self._rebuild_menu()

    # ----- 沉浸模式 -----

    def _toggle_immersive(self):
        self.immersive = not self.immersive
        self.root.after(0, self._apply_immersive)

    def _apply_immersive(self):
        if self.immersive:
            self._saved_geometry = self.root.geometry()
            self.root.overrideredirect(True)
            self.root.attributes("-topmost", False)
            self.root.lower()
        else:
            self.root.overrideredirect(False)
            if self._saved_geometry:
                self.root.geometry(self._saved_geometry)
            self.root.attributes("-topmost", True)
            if self.transparent_bg:
                self.transparent_bg = False
                self._apply_transparent_bg(False)
        self._rebuild_menu()

    # ----- 透明背景 -----

    def _toggle_transparent_bg(self):
        if not self.immersive:
            return
        self.transparent_bg = not self.transparent_bg
        self._apply_transparent_bg(self.transparent_bg)
        self._rebuild_menu()

    def _apply_transparent_bg(self, enable):
        transparent_color = "#010102"
        if enable:
            self._set_widget_bg(self.root, transparent_color)
            self.root.attributes("-transparentcolor", transparent_color)
        else:
            self._set_widget_bg(self.root, "#1e1e2e")
            self.root.attributes("-transparentcolor", "")

    def _set_widget_bg(self, widget, color):
        try:
            widget.configure(bg=color)
        except tk.TclError:
            pass
        for child in widget.winfo_children():
            self._set_widget_bg(child, color)

    # ----- 显示选项 -----

    def _count_visible(self):
        return sum([self.show_temp, self.show_cpu, self.show_mem, self.show_net])

    def _update_visibility(self):
        frames = [
            (self.show_temp, self.frame_temp),
            (self.show_cpu, self.frame_cpu),
            (self.show_mem, self.frame_mem),
            (self.show_net, self.frame_up),
            (self.show_net, self.frame_down),
        ]
        for _, f in frames:
            f.pack_forget()

        content_rows = 0
        for flag, f in frames:
            if flag:
                f.pack(fill=tk.X, padx=10, pady=8)
                content_rows += 1

        # 动态调整窗口高度：每行 ~44px + 标题栏 ~40px
        h = content_rows * 44 + 40
        self.root.geometry(f"330x{h}")

    def _toggle_show_temp(self):
        if self.show_temp and self._count_visible() <= 1:
            return
        self.show_temp = not self.show_temp
        self._update_visibility()
        self._rebuild_menu()

    def _toggle_show_cpu(self):
        if self.show_cpu and self._count_visible() <= 1:
            return
        self.show_cpu = not self.show_cpu
        self._update_visibility()
        self._rebuild_menu()

    def _toggle_show_mem(self):
        if self.show_mem and self._count_visible() <= 1:
            return
        self.show_mem = not self.show_mem
        self._update_visibility()
        self._rebuild_menu()

    def _toggle_show_net(self):
        if self.show_net and self._count_visible() <= 1:
            return
        self.show_net = not self.show_net
        self._update_visibility()
        self._rebuild_menu()

    # ----- 托盘 -----

    def _build_tray_menu(self):
        t = self._t
        startup_text = ("✓ " if self._startup_enabled else "  ") + t("startup")
        immersive_text = ("✓ " if self.immersive else "  ") + t("immersive")
        transparent_text = ("✓ " if self.transparent_bg else "  ") + t("transparent_bg")
        temp_unit_text = t("temp_unit") + ("：°F" if self.celsius else "：°C")
        return pystray.Menu(
            pystray.MenuItem(t("show_window"), self.show_window, default=True),
            pystray.MenuItem(startup_text, self._toggle_startup_menu),
            pystray.MenuItem(immersive_text, self._toggle_immersive),
            pystray.MenuItem(transparent_text, self._toggle_transparent_bg,
                             enabled=self.immersive),
            pystray.MenuItem(t("display_options"),
                             pystray.Menu(
                                 pystray.MenuItem(
                                     ("✓ " if self.show_temp else "  ") + t("cpu_temp_option"),
                                     self._toggle_show_temp),
                                 pystray.MenuItem(
                                     ("✓ " if self.show_cpu else "  ") + t("cpu_usage_option"),
                                     self._toggle_show_cpu),
                                 pystray.MenuItem(
                                     ("✓ " if self.show_mem else "  ") + t("memory_option"),
                                     self._toggle_show_mem),
                                 pystray.MenuItem(
                                     ("✓ " if self.show_net else "  ") + t("network_option"),
                                     self._toggle_show_net),
                             )),
            pystray.MenuItem(t("language"),
                             pystray.Menu(
                                 *[pystray.MenuItem(
                                     ("✓ " if l == self.lang else "  ") + name,
                                     (lambda ll: lambda: self._set_language(ll))(l),
                                 ) for l, name in LANGUAGES.items()]
                             )),
            pystray.MenuItem(temp_unit_text, self._toggle_temperature_unit),
            pystray.Menu.SEPARATOR,
            pystray.MenuItem(t("about"), self._show_about),
            pystray.MenuItem(t("exit"), self.quit_app),
        )

    def _toggle_temperature_unit(self):
        self.celsius = not self.celsius
        unit = "°C" if self.celsius else "°F"
        self.lbl_temp_unit.config(text=unit)
        self._rebuild_menu()

    def _show_about(self):
        t = self._t
        messagebox.showinfo(
            t("about_title"),
            f"Minos v{VERSION}\n"
            f"{t('about_desc')}\n"
            f"\n"
            f"{t('copyright')}",
        )

    def _rebuild_menu(self):
        if self.tray_icon:
            self.root.after(0, self._do_rebuild_menu)

    def _do_rebuild_menu(self):
        if self.tray_icon:
            self.tray_icon.menu = self._build_tray_menu()
            self.tray_icon.update_menu()

    def _setup_tray(self):
        img = draw_tray_icon(None)
        menu = self._build_tray_menu()
        self.tray_icon = pystray.Icon("minos", img, "Minos 启动中...", menu)
        threading.Thread(target=self.tray_icon.run, daemon=True).start()

    # ----- 窗口控制 -----

    def hide_window(self):
        self.root.withdraw()

    def show_window(self):
        self.root.after(0, self._do_show)

    def _do_show(self):
        self.root.deiconify()
        self.root.lift()
        self.root.focus_force()

    def quit_app(self):
        self.running = False
        self._stop_event.set()
        if self.tray_icon:
            self.tray_icon.stop()
        self.root.after(0, self.root.destroy)

    # ----- 数据刷新 -----

    def _trigger_first_refresh(self):
        t = threading.Thread(target=self._refresh_loop, daemon=True)
        t.start()

    def _refresh_loop(self):
        log.info("refresh loop started")
        while self.running:
            try:
                temp = get_cpu_temperature()
                cpu = get_cpu_usage()
                mem_used, mem_total = get_memory_usage()
                recv, sent, self.prev_counters, self.prev_time = get_net_speed(
                    self.prev_counters, self.prev_time
                )
                down_val, down_unit = format_speed(recv)
                up_val, up_unit = format_speed(sent)
                display_temp = temp
                if not self.celsius and temp is not None:
                    display_temp = temp * 9.0 / 5.0 + 32.0
                icon_img = draw_tray_icon(temp, display_temp)
                unit = "°C" if self.celsius else "°F"
                temp_str = f"{display_temp:.1f}{unit}" if temp is not None else "N/A"
                t = self._t
                tooltip = (f"{t('tooltip_cpu')}: {temp_str}\n"
                           f"{t('tooltip_cpu_usage')}: {cpu:.1f}%\n"
                           f"{t('tooltip_memory')}: {mem_used:.1f}/{mem_total:.1f} GB\n"
                           f"{t('tooltip_upload')} {up_val} {up_unit}\n"
                           f"{t('tooltip_download')} {down_val} {down_unit}")

                self.root.after(0, self._apply,
                    display_temp, cpu, mem_used, mem_total,
                    down_val, down_unit, up_val, up_unit,
                    icon_img, tooltip)
            except Exception as e:
                log.exception("refresh loop error")

            self._stop_event.wait(5)

    def _apply(self, temp, cpu, mem_used, mem_total, down_val, down_unit, up_val, up_unit, icon_img, tooltip):
        self.lbl_temp.config(text=f"{temp:.1f}" if temp is not None else "N/A")
        self.lbl_cpu.config(text=f"{cpu:.1f}")
        self.lbl_mem.config(text=f"{mem_used:.1f}/{mem_total:.1f}")
        self.lbl_down.config(text=down_val)
        self.lbl_down_unit.config(text=down_unit)
        self.lbl_up.config(text=up_val)
        self.lbl_up_unit.config(text=up_unit)
        if self.tray_icon and self.tray_icon.visible:
            self.tray_icon.icon = icon_img
            self.tray_icon.title = tooltip


# ============================================================
# 入口
# ============================================================

if __name__ == "__main__":
    MinosApp()
