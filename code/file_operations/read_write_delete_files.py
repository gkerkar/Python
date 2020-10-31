import csv
import os
import shutil
from os import walk

filepath = '/content/sample_data'
path = ''

# get list of files in directories
files = []
for (dirpath, dirnames, filenames) in walk(filepath):
    files.extend(filenames)

print(files)

with open('/content/sample_data/test_file.txt') as fr:
  csv_data = csv.reader(fr, delimiter='|')
  for count, row in enumerate(csv_data):
    # print(count, row)
    if count > 0: # ignore header
      for i in row:
        col, val = i.strip().split(sep=':')
        # print(col, val)
        path = os.path.join(filepath,col) #add directory using first column value from csv file.
        print(path)

        # remove existing directories
        try:
            shutil.rmtree(path)
            print("{} removed successfully".format(path))
        except OSError as error:
            print("Error: {} : {}".format(path, error.strerror))

        # create directories
        try: 
            os.makedirs(path,exist_ok = True) 
            print("Directory {} created successfully".format(path)) 
        except OSError as error: 
            print("Directory {} can not be created. {}".format(path, error))

        # create files in directories
        with open(path+'/'+col+'.txt', 'a') as fw:
          fw.write(''.join(val) + '\n')
