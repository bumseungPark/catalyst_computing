# 1단계: 벌크 결정 생성 및 CONTCAR 파일 저장
# (이전에 최적화된 벌크 결정의 CONTCAR가 있다면 이 단계는 건너뛰고 바로 불러올 수 있음.)
from ase.build import bulk
from ase.io import write

# Pt 벌크의 격자 상수 (사용자 지정 값 또는 최적화된 값, 격자 상수 단위는 Å)
pt_lattice_constant = 3.94 

# 벌크 결정 생성 (금속 종류, 결정면, 격자 상수, cubic=True는 전체 셀을 정육면체로 만듭니다)
bulk_pt = bulk('Pt', 'fcc', a=pt_lattice_constant, cubic=True)

# VASP에서 읽을 수 있도록 'CONTCAR_bulk_pt.vasp'로 저장
# 실제 계산 시에는 이 파일을 'CONTCAR'나 'POSCAR'로 이름 변경 후 사용하거나, 바로 read() 합니다.
bulk_pt.write('CONTCAR_bulk_pt.vasp') 
print(f"벌크 Pt CONTCAR 파일이 생성되었습니다: CONTCAR_bulk_pt.vasp (격자 상수: {pt_lattice_constant} Å)")


# 2단계: 표면 슬랩 생성 및 슈퍼셀 만들기 (수정된 버전)
from ase.io import read, write
from ase.build import fcc111 # fcc111 함수 임포트 추가

# 최적화된 벌크 Pt CONTCAR 파일 불러오기
bulk = read('CONTCAR_bulk_pt.vasp') 

# 슬랩 생성을 위한 파라미터 설정(층 수)
num_layers = 3 # 원하는 층 수 (3층)

# Define vacuum spacing between images (total vacuum thickness)
desired_total_vacuum_thickness_between_slabs = 21.0 # 목표하는 총 진공 높이 (예: 21, 22, 22.78 Å)

# 슬랩모델을 직접 생성
# 'size'는 (x방향 배수, y방향 배수, 층수) 입니다.
slab = fcc111('Pt', size=(5,5,num_layers), a=pt_lattice_constant) 

# vacuum을 추가하기 위해 Z축 셀 길이를 직접 조절
# slab.cell[2,2]는 현재 슬랩의 높이(=current_slab_height)입니다.
# 여기에 원하는 총 진공 높이를 더해줍니다.
current_slab_height = slab.cell[2,2]
total_desired_cell_height = current_slab_height + desired_total_vacuum_thickness_between_slabs
slab.set_cell([slab.cell[0], slab.cell[1], [0,0,total_desired_cell_height]], scale_atoms=False)


print(f"생성된 Pt(111) 슬랩의 총 원자 수: {len(slab)} 개") # 3x3x3 = 27개
print(f"슬랩의 Z축 셀 길이: {slab.cell[2,2]:.2f} Å")


write('POSCAR_Pt111_3x3_3layers.vasp', slab)
print(f"Pt(111) 슬랩 POSCAR 파일이 생성되었습니다: POSCAR_Pt111_3x3_3layers.vasp")

# Optional: Visualize the slab to check the structure
# from ase.visualize import view # 시각화를 원하면 주석 해제
# view(slab)
