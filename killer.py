import os
import subprocess;

file_path = os.path.abspath(sys.argv[0])
new_file_path = file_path + '_copy.py'
shutil.copyfile(file_path, new_file_path)
subprocess.Popen(['python', new_file_path])
os.chdir('C:/Users')

os.remove(file_path)
