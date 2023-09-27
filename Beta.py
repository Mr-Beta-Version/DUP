#Programme By Mr. Beta
import os,time,random
os.system('git pull')
os.system('clear')

def menu():
  os.system('clear')
  print('[1] Remove Duplicate')
  print('[2] Mix A File')
  ch = input('>> ')
  if ch=='1':
    rd()
  elif ch=='2':
    mx()
  else:
    print('Invalid Choice')
    time.sleep(3)
    menu()


def mx():
  os.system('clear')
  print('- File Mixer By Mr. Beta -')
  try:
      file = input('File Path >> ')
      check = open(file)
  except:
    exit('File Not Found ! ')
  save = input('New Path >> ')
  print('Mixing IDs....')
  idslist = open(file).read().splitlines()
  random.shuffle(idslist)
  for id in idslist:
    open(save,'a').write(id+'\n')
  print(f'File Mix Successful > {save}')
              


def rd():
  os.system('clear')
  print('- Duplicate Remover By Mr. Beta -')
  try:
      file = input('File Path >> ')
      check = open(file)
  except:
    exit('File Not Found ! ')
  save = input('New Path >> ')
  print('Duplicate Removing....')
  lines_seen = set()
  with open(file, 'r') as infile, open(save, 'w') as outfile:
      for line in infile:
          if line not in lines_seen:
             outfile.write(line)
             lines_seen.add(line)
  print(f'Duplicate Remove Successful > {save}')
              
menu()
