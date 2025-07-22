# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 14:58:51 2025

@author: CCMD
"""

import numpy as np

# 절대 경로 (Windows에서는 \ 대신 / 또는 r'' 형태의 raw string 사용)
file_path = r'C:/Users/CCMD/Desktop/code/PLANAR_AVERAGE_pure.dat'

# 또는 백슬래시 그대로 쓸 경우, raw string으로 처리해야 함
# file_path = r'C:\Users\CCMD\Desktop\code\PLANAR_AVERAGE_pure.dat'

# 데이터 불러오기
data = np.loadtxt(file_path, comments='#')

# 데이터 분리
z = data[:, 0]
potential = data[:, 1]

# 그래프 그리기
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))
plt.plot(z, potential, label='Planar-Averaged Potential', color='blue')
plt.xlabel('z (Å)')
plt.ylabel('Potential (eV)')
plt.title('Planar-Averaged Electrostatic Potential')
plt.grid(False)
plt.legend()
plt.tight_layout()
plt.show()
