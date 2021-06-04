import glob
import os

source_files = glob.glob("source/**/*.cpp", recursive=True)
built_files = []

for file in source_files:
  print('\x1b[32mBuilding ' + file + '\x1b[0m')

  out_folder = 'o' + os.path.sep + file[7:file.rindex(os.path.sep)]
  out_file_name = 'o' + os.path.sep + file[7:file.rindex('.cpp')] + '.o'

  os.makedirs(out_folder, exist_ok=True)
  code = os.system('g++ -c ' + file + ' -o ' + out_file_name)
  if code != 0:
    exit(-1)
  built_files.append(out_file_name)

  print('\x1b[35m - Built ' + file + '(to \x1b[34m' + out_file_name + '\x1b[35m)\x1b[0m')

files_string = ' '.join(built_files)
code = os.system('g++ ' + files_string + ' -o o/summit')
if code != 0:
  exit(-1)

for file in built_files:
  os.remove(file)