#Programme By Mr. Beta
import os
os.system('git pull')
os.system('clear')
print('- Duplicate Remover By Mr. Beta -')


def rd():
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
  print('Duplicate Remove Successful')
              
rd()
