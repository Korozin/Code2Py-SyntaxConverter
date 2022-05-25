import sys
import os
import pyperclip

# RAM Write to Cemu converter
# By Korozin

print('\nSpecify location of code')
print('Example: /home/user/Desktop/Code.txt\n')
path = input('Input Here: ')

while not os.path.isfile(path):
    print('No files found.')
    break

with open(path,encoding="utf-8") as f:
    src = f.readlines()

print('\nConverted: ')
print('')
for line in src:
  line_parts = line.split()
  print(f'tcp.pokemem(0x{line_parts[0]}, 0x{line_parts[1]})')


pyperclip.copy(f'tcp.pokemem(0x{line_parts[0]}, 0x{line_parts[1]})')
spam = pyperclip.paste()
