import csv
with open('/content/sample_data/test_file.txt') as fr:
  csv_data = csv.reader(fr, delimiter='|')
  for row in csv_data:
    # print(row)
    for i in row:
      # col, val = i.strip().split(sep=':')
      # print(col, val)

      with open('/content/sample_data/output_file.txt', 'a') as fw:
        fw.write(''.join(i.strip()) + '\n')
