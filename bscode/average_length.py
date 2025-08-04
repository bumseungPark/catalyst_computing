# -*- coding: utf-8 -*-
"""
Created on Mon Aug  4 16:57:02 2025

@author: CCMD
"""

from ase.io import read
from ase.data import covalent_radii, atomic_numbers
import numpy as np
from itertools import combinations # combinations 임포트 추가

# 1. 계산 완료된 CONTCAR 파일 불러오기
atoms = read('CONTCAR')

# 2. 시스템 내의 모든 고유한 원소들을 찾아 원소 쌍을 자동으로 정의
unique_elements = sorted(list(set(atoms.get_chemical_symbols())))
element_pairs_to_measure = list(combinations(unique_elements, 2))
print("--- 평균 결합 길이 분석 결과 ---")
print(f"시스템에서 발견된 원소: {unique_elements}")
print(f"분석할 결합 쌍: {element_pairs_to_measure}")

# 3. 결합 길이 찾기 위한 최대 거리 임계값 설정
#    Key를 frozenset으로 만들어 순서에 독립적이게 함
max_bond_length_thresholds = {}
for sym1_key, sym2_key in element_pairs_to_measure:
    key_frozenset = frozenset({sym1_key, sym2_key})

    try:
        radius1 = covalent_radii[atomic_numbers[sym1_key]]
        radius2 = covalent_radii[atomic_numbers[sym2_key]]
        # 공유 결합 반지름의 합에 0.3 Å 여유 추가
        max_bond_length_thresholds[key_frozenset] = radius1 + radius2 + 0.3
    except KeyError:
        print(f"경고: 원소 {sym1_key} 또는 {sym2_key}의 공유 결합 반지름을 찾을 수 없습니다. 기본값 2.5 Å 사용.")
        # 만약 covalent_radii에 없는 원소라면, 합리적인 기본값 설정
        max_bond_length_thresholds[key_frozenset] = 2.5

# ---- 추가된 기본 임계값 (필요시 수동 조정) ----
# ---------------------------------------------


for (sym1, sym2) in element_pairs_to_measure:
    bond_lengths = []

    # sym1과 sym2가 CONTCAR에 존재하는지 먼저 확인 (이 부분은 이제 필요 없지만, 안정성을 위해 유지)
    # 자동 정의 기능으로 인해 항상 존재한다고 가정할 수 있음.
    
    # 시스템 내 모든 원자들을 순회하여 결합 쌍 찾기
    for i, atom1 in enumerate(atoms):
        if atom1.symbol == sym1:
            for j, atom2 in enumerate(atoms):
                if atom2.symbol == sym2:
                    # 같은 원자 제외 (i == j 일 때는 거리가 0)
                    if i == j:
                        continue

                    # 주기적 경계 조건을 고려하여 두 원자 간의 거리 계산
                    distance = atoms.get_distance(i, j, mic=True)

                    # 설정한 최대 결합 길이 임계값 내에 있는지 확인
                    if distance <= max_bond_length_thresholds[frozenset({sym1, sym2})]:
                        bond_lengths.append(distance)

    if bond_lengths:
        avg_bond_length = sum(bond_lengths) / len(bond_lengths)
        print(f"평균 {sym1}-{sym2} 결합 길이: {avg_bond_length:.3f} Å (총 {len(bond_lengths)}개 결합)")
    else:
        print(f"주의: {sym1}-{sym2} 결합을 찾지 못했습니다. 최대 결합 길이 임계값 '{max_bond_length_thresholds.get(frozenset({sym1, sym2}), 2.5):.1f} Å'을 확인하거나 조정하세요.")