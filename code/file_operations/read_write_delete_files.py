import csv
import os
import shutil
from os import walk

filepath = '/content/sample_data'

files = []
for (dirpath, dirnames, filenames) in walk(filepath):
    files.extend(filenames)

print(files)

with open('/content/sample_data/test_file.txt') as fr:
  parent_dir = '/content/sample_data/'
  path = ''
  csv_data = csv.reader(fr, delimiter='|')
  for row in csv_data:
    # print(row)
    for i in row:
      col, val = i.strip().split(sep=':')
      # print(col, val)
      path = os.path.join(parent_dir,col)
      print(path)

      try:
          shutil.rmtree(path)
          print("{} removed successfully".format(path))
      except OSError as error:
          print("Error: {} : {}".format(path, error.strerror))

      try: 
          os.makedirs(path,exist_ok = True) 
          print("Directory {} created successfully".format(path)) 
      except OSError as error: 
          print("Directory {} can not be created. {}".format(path, error))

      with open(path+'/'+col+'.txt', 'a') as fw:
        fw.write(''.join(val) + '\n')
