# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 13:58:48 2025

@author: bspark
"""

import matplotlib.pyplot as plt
import numpy as np


#create_line_plot_with_custom_ticks= 그래프를 만드는 함수, 주어진 데이터를 이용해 그래프를 생성합니다.
def create_line_plot_with_custom_ticks(x_data, y_data, title="꺾은선 그래프", x_label="X축", y_label="Y축",
                                       main_font_size=14, # <--- 메인폰트 사이즈
                                       title_font_size=18, # <--- 제목폰트 사이즈
                                       label_font_size=16, # <--- 라벨폰트 사이즈
                                       tick_font_size=12, # <--- 간격 부분 폰트 사이즈
                                       x_tick_interval=1, # <--- 매개변수: x축 눈금 간격
                                       y_min=None,
                                       y_max=None,
                                       color='blue', marker='o', linestyle='-'): # <--- 색깔, 마커, 선 유형은 자유롭게 변형 가능합니다.

    plt.figure(figsize=(10, 6)) # <---figure size를 가로 10인치, 세로 6인치로 한다.

    plt.plot(x_data, y_data, color=color, marker=marker, linestyle=linestyle)

    plt.title(title, fontsize=title_font_size)
    plt.xlabel(x_label, fontsize=label_font_size)
    plt.ylabel(y_label, fontsize=label_font_size, rotation=0, ha='right') # <--- 라벨을 회전시킬 때 사용합니다.

    # X축 눈금 간격 설정
    # x_data의 최소값부터 최대값까지 x_tick_interval 간격으로 눈금 생성합니다.
    min_x = np.floor(np.min(x_data)) # x_data의 최소값을 내림하여 시작점 설정
    max_x = np.ceil(np.max(x_data))  # x_data의 최대값을 올림하여 끝점 설정
    x_ticks = np.arange(min_x, max_x + x_tick_interval, x_tick_interval)
    plt.xticks(x_ticks) # <--- 이 부분이 x축 눈금 간격을 조절합니다.
    
    # Y축 범위 설정
    if y_min is not None or y_max is not None: # <--- 
        plt.ylim(y_min, y_max) # y_min 또는 y_max가 제공된 경우에만 설정합니다.

    # 눈금 라벨 폰트 사이즈를 설정합니다.
    plt.tick_params(axis='x', labelsize=tick_font_size)
    plt.tick_params(axis='y', labelsize=tick_font_size)

    plt.grid(True, linestyle='', alpha=0.7)
    plt.show()

# 실제 데이터가 들어간 부분
x_nitrogen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
delta_e = [0.00, 0.06, 0.06, 0.08, 0.15, 0.25, 0.27, 0.32, 0.60, 0.61]

print("질소 도핑 에너지 그래프: x축 눈금 간격 1로 조절")
create_line_plot_with_custom_ticks(x_nitrogen, delta_e,
                                           title="Nitrogen doping energy",
                                           x_label="# of Nitrogen",
                                           y_label="ΔE",
                                           title_font_size=18,
                                           label_font_size=16,
                                           tick_font_size=12,
                                           x_tick_interval=1, # <-- 여기에 1을 넣어 간격을 1로 설정
                                           y_min=-0.05,
                                           y_max=0.8,
                                           color='blue',
                                           marker='o')

# 만약 x_data가 정수가 아니라 소수점 값을 포함하고,
# 소수점 단위의 눈금 간격을 원한다면 x_tick_interval에 0.5 등을 넣어볼 수 있습니다.
# x_data_float = np.linspace(0, 10, 100)
# y_data_float = np.sin(x_data_float)
# create_line_plot_with_custom_ticks(x_data_float, y_data_float,
#                                            title="사인 함수 (소수점 간격)",
#                                            x_label="값",
#                                            y_label="함수 값",
#                                            x_tick_interval=0.5)
