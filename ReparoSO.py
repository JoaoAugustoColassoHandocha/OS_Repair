import os

os.system('color 1f')

print('\n=============================')
print('Reparo do Sistema Operacional')
print('=============================\n')

os.system('pause')
os.system('cls')

os.system('DISM /online /cleanup-image /checkhealth')
print('\n')
os.system('pause')
os.system('cls')

os.system('sfc /scannow')
print('\n')
os.system('pause')
os.system('cls')