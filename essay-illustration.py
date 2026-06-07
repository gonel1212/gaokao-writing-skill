# -*- coding: utf-8 -*-
"""
配图 for 《一字之"慢"，一生之悟》
- 主题: 慢字理解的三次蜕变
- 风格: 东方水墨 / 宣纸质朴
- 输出: essay-illustration.png / .pdf
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Rectangle, FancyBboxPatch, Circle, FancyArrowPatch
from matplotlib.lines import Line2D
import numpy as np

# ---------- 字体 ----------
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'STHeiti', 'KaiTi', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.family'] = 'sans-serif'

# ---------- 配色（水墨 / 宣纸 / 朱砂） ----------
BG       = '#f3ecd8'   # 宣纸底色
INK      = '#1c1a17'   # 浓墨
INK_SOFT = '#3d3733'   # 淡墨
GOLD     = '#a87b3c'   # 赭金
JADE     = '#4a6b54'   # 青碧
RED      = '#8a2a25'   # 朱砂
GRAY     = '#7a6f63'   # 灰褐
PAPER    = '#ebe1c3'   # 次浅宣纸

# ---------- 画布 ----------
fig = plt.figure(figsize=(14, 9), facecolor=BG)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, 14)
ax.set_ylim(0, 9)
ax.axis('off')
ax.set_facecolor(BG)

# ---------- 装饰：左上角水墨晕染（用渐变圆模拟）----------
for i, (cx, cy, r, alpha) in enumerate([
    (0.6, 8.4, 0.9, 0.08),
    (1.0, 8.0, 0.7, 0.10),
    (13.4, 0.6, 1.0, 0.08),
    (13.0, 1.0, 0.6, 0.10),
    (13.2, 8.4, 0.5, 0.07),
]):
    circ = Circle((cx, cy), r, color=INK, alpha=alpha, zorder=1)
    ax.add_patch(circ)

# ---------- 顶部标题区 ----------
ax.text(7.0, 8.45, '一字之"慢"，一生之悟',
        ha='center', va='center', fontsize=34, weight='bold',
        color=INK, family='SimHei', zorder=5)

# 副标题
ax.text(7.0, 7.85, '—— 在 "快" 的时代里，写下 "慢" 的注脚 ——',
        ha='center', va='center', fontsize=14,
        color=GRAY, style='italic', family='KaiTi', zorder=5)

# 标题下小印章（朱砂方印）
seal = Rectangle((11.2, 7.55), 0.55, 0.55, facecolor=RED, edgecolor=RED, zorder=5)
ax.add_patch(seal)
ax.text(11.475, 7.825, '慢', ha='center', va='center',
        fontsize=22, color='#fff5e6', weight='bold', family='KaiTi', zorder=6)

# ---------- 中部：三阶蜕变主体 ----------
# 阶梯底座 (P1: 童年 慢=落后)
p1 = FancyBboxPatch((1.2, 4.6), 3.4, 1.0,
                    boxstyle="round,pad=0.04,rounding_size=0.12",
                    facecolor=GRAY, edgecolor=INK, linewidth=1.6, zorder=4)
ax.add_patch(p1)
ax.text(2.9, 5.30, '童 年', ha='center', va='center',
        fontsize=20, color='#f3ecd8', weight='bold', family='KaiTi', zorder=5)
ax.text(2.9, 4.85, '"慢" = 落后 · 输', ha='center', va='center',
        fontsize=13, color='#f3ecd8', family='KaiTi', zorder=5)
ax.text(2.9, 4.30, '作业写慢被催 · 考试没写完被点名',
        ha='center', va='center', fontsize=10, color=INK_SOFT, family='SimHei', zorder=5)

# 阶梯 (P2: 少年 慢=等待)
p2 = FancyBboxPatch((5.0, 4.6), 3.4, 1.5,
                    boxstyle="round,pad=0.04,rounding_size=0.12",
                    facecolor=JADE, edgecolor=INK, linewidth=1.8, zorder=4)
ax.add_patch(p2)
ax.text(6.7, 5.65, '少 年', ha='center', va='center',
        fontsize=22, color='#f3ecd8', weight='bold', family='KaiTi', zorder=5)
ax.text(6.7, 5.20, '"慢" = 等待 · 观察', ha='center', va='center',
        fontsize=13, color='#f3ecd8', family='KaiTi', zorder=5)
ax.text(6.7, 4.85, '《山海经》慢读 · 数学题慢慢画图',
        ha='center', va='center', fontsize=10, color='#f3ecd8', family='SimHei', zorder=5)
ax.text(6.7, 4.30, '—— 拒绝被算法裹挟的"清醒" ——',
        ha='center', va='center', fontsize=10, color=INK_SOFT, family='KaiTi', zorder=5)

# 阶梯 (P3: 当下 慢=沉淀)
p3 = FancyBboxPatch((8.8, 4.6), 4.0, 2.0,
                    boxstyle="round,pad=0.04,rounding_size=0.14",
                    facecolor=GOLD, edgecolor=INK, linewidth=2.4, zorder=4)
ax.add_patch(p3)
ax.text(10.8, 6.10, '当  下', ha='center', va='center',
        fontsize=26, color=INK, weight='bold', family='KaiTi', zorder=5)
ax.text(10.8, 5.55, '"慢" = 沉淀 · 远见 · 定力', ha='center', va='center',
        fontsize=14, color=INK, weight='bold', family='KaiTi', zorder=5)
ax.text(10.8, 5.05, '老子"治大国若烹小鲜"', ha='center', va='center',
        fontsize=10, color=INK, family='KaiTi', zorder=5)
ax.text(10.8, 4.78, '庖丁解牛 19 年 · 达·芬奇 16 年', ha='center', va='center',
        fontsize=10, color=INK, family='KaiTi', zorder=5)
ax.text(10.8, 4.30, '南仁东 22 年 · 黄旭华 30 年 · 苏炳添 10 年',
        ha='center', va='center', fontsize=10, color=INK, family='KaiTi', zorder=5)

# 上升箭头（蜕变方向）
arrow1 = FancyArrowPatch((4.6, 5.1), (5.0, 5.35),
                         arrowstyle='->', mutation_scale=22,
                         color=INK, linewidth=2.0, zorder=6)
ax.add_patch(arrow1)
arrow2 = FancyArrowPatch((8.4, 5.35), (8.8, 5.85),
                         arrowstyle='->', mutation_scale=24,
                         color=INK, linewidth=2.2, zorder=6)
ax.add_patch(arrow2)

# 上升文字（蜕变关键词）
ax.text(4.8, 5.55, '重 审', ha='center', va='center',
        fontsize=9, color=RED, family='KaiTi', rotation=-30, zorder=5)
ax.text(8.6, 6.20, '方 悟', ha='center', va='center',
        fontsize=11, color=RED, family='KaiTi', rotation=-30, zorder=5, weight='bold')

# ---------- 上方：快时代的"诱惑" ----------
ax.text(7.0, 7.30, '▲ 时代之"快"  ▲',
        ha='center', va='center', fontsize=12, color=RED, weight='bold', family='KaiTi', zorder=5)
fast_items = 'AI 一键生成  ·  5 秒短视频  ·  算法推送  ·  即时满足  ·  ChatGPT 秒答'
ax.text(7.0, 7.00, fast_items, ha='center', va='center',
        fontsize=11, color=INK_SOFT, family='KaiTi', zorder=5)

# 引出 → 慢
ax.annotate('', xy=(2.9, 5.7), xytext=(2.9, 6.85),
            arrowprops=dict(arrowstyle='->', color=GRAY, lw=1.2, alpha=0.6, zorder=3))

# ---------- 下方：底部金句与时间轴 ----------
# 分隔线
ax.plot([0.8, 13.2], [3.85, 3.85], color=INK, linewidth=0.8, alpha=0.5, zorder=2)

# 时间轴标题
ax.text(7.0, 3.55, '— 古今中外 "慢"之大成 —',
        ha='center', va='center', fontsize=12, color=INK, weight='bold', family='KaiTi', zorder=5)

# 时间轴主线
ax.plot([1.0, 13.0], [2.45, 2.45], color=INK, linewidth=1.6, zorder=4)
# 箭头端
ax.annotate('', xy=(13.2, 2.45), xytext=(13.0, 2.45),
            arrowprops=dict(arrowstyle='->', color=INK, lw=1.6, zorder=4))

# 时间节点 + 人物
events = [
    # (x, label_top, year_top, label_bottom, year_bottom)
    (1.6, '庖丁解牛',  '19年',  '《庄子·养生主》',          '约公元前 300 年'),
    (4.0, '达·芬奇',    '16年',  '《蒙娜丽莎》反复修改',     '1503 — 1519'),
    (6.6, '王羲之',     '20年',  '临池学书，池水尽墨',       '东晋'),
    (8.9, '黄旭华',     '30年',  '中国核潜艇',                '1958 — 1988'),
    (11.0, '南仁东',    '22年',  'FAST 中国天眼',             '1994 — 2016'),
    (12.7, '苏炳添',    '10年',  '9.83 秒 亚洲新纪录',        '2010 — 2021'),
]

for (x, name, years, desc, era) in events:
    # 节点圆点
    circ = Circle((x, 2.45), 0.10, facecolor=RED, edgecolor=INK, linewidth=0.8, zorder=5)
    ax.add_patch(circ)
    # 上方：人物 + 年数
    ax.text(x, 3.10, name, ha='center', va='center',
            fontsize=11, color=INK, weight='bold', family='KaiTi', zorder=5)
    ax.text(x, 2.85, years, ha='center', va='center',
            fontsize=9, color=RED, family='KaiTi', zorder=5)
    # 下方：描述 + 时代
    ax.text(x, 2.05, desc, ha='center', va='center',
            fontsize=8.5, color=INK_SOFT, family='KaiTi', zorder=5)
    ax.text(x, 1.75, era, ha='center', va='center',
            fontsize=8, color=GRAY, family='KaiTi', style='italic', zorder=5)

# ---------- 底部金句 ----------
ax.plot([0.8, 13.2], [1.30, 1.30], color=INK, linewidth=0.6, alpha=0.4, zorder=2)

ax.text(7.0, 0.95,
        '"快" 的廉价，正是 "慢" 的稀缺',
        ha='center', va='center', fontsize=18, color=RED, weight='bold', family='KaiTi', zorder=5)

ax.text(7.0, 0.55,
        '在 "快" 中守住 "慢"   ·   在 "新" 中守住 "深"   ·   让 "慢" 写进我们这一代人的成长印记',
        ha='center', va='center', fontsize=10.5, color=INK_SOFT, family='KaiTi', zorder=5)

# ---------- 四角装饰小元素 ----------
# 右上角小朱印
seal2 = Rectangle((12.55, 7.55), 0.4, 0.4, facecolor=RED, edgecolor=RED, zorder=5)
ax.add_patch(seal2)
ax.text(12.75, 7.75, '悟', ha='center', va='center',
        fontsize=14, color='#fff5e6', weight='bold', family='KaiTi', zorder=6)

# ---------- 保存 ----------
out_png = r'C:\download\develop\gaokao-essay-project\essay-illustration.png'
out_pdf = r'C:\download\develop\gaokao-essay-project\essay-illustration.pdf'

plt.savefig(out_png, dpi=180, facecolor=BG, bbox_inches='tight', pad_inches=0.2)
plt.savefig(out_pdf,            facecolor=BG, bbox_inches='tight', pad_inches=0.2)
plt.close()

print(f'配图已生成：\n  PNG: {out_png}\n  PDF: {out_pdf}')
