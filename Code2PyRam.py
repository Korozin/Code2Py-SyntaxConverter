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

for line in src:
  line_parts = line.split()
  file = open('output.txt', "a")
  file.write(f'tcp.pokemem(0x{line_parts[0]}, 0x{line_parts[1]})\n')
  file.close()

print('\nConverted, see output.txt')
