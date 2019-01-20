import os
import pathlib
import glob
import shutil

print(os.path.exists('test.txt'))
print(os.path.isfile('test.txt'))
print(os.path.isdir('testdir'))

# os.rename('test.txt', 'renamed.txt')
# os.rename('renamed.txt', 'test.txt')

# os.symlink('test.txt', 'symlink') # only UNIX

pathlib.Path('empty.txt').touch()
os.remove('empty.txt')

print(os.listdir('.'))

print(glob.glob('*'))

# shutil.copy('test.txt', 'test2.txt')

# shutil.rmtree('./testdir')
