import glob

file_list =[]
for file in glob.glob('file/*.txt'):
  file_list.append(file)
# print(file_list)

new_list =[]
for name in file_list:
  with open(name) as f:
    count = len(f.readlines())
    # print(count)
    new_list.append([count, name])
  f.close()
# print(new_list)  
new_list.sort()
# print(new_list)

with open('newfile.txt', 'w') as f:
  for i in new_list:
    # print(i[1])
    with open(i[1]) as d:
      sur = i[1].replace('file/', '')
      f.write(f'{sur} \n {i[0]} \n {d.read()}\n')
