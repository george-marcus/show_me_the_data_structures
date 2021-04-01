import os
from find_files import find_files

dirname = os.path.dirname(__file__)
test_dir_path = os.path.realpath(dirname + '/testdir')


find_files('', None)
find_files('', -1)
find_files("", test_dir_path)
find_files(".py", test_dir_path)
find_files(".pdf", test_dir_path)
find_files(".c", test_dir_path)
find_files(".gitkeep", test_dir_path)
