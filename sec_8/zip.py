import glob
import zipfile

# zipの作成
with zipfile.ZipFile('test.zip', 'w') as z:
    # z.write('zip_dir')
    # z.write('zip_dir/test.txt')

    # globを使ったzipの作成
    for f in glob.glob('zip_dir/**', recursive=True):
        print(f)
        z.write(f)

with zipfile.ZipFile('test.zip', 'r') as z:
    # z.extractall('zzz2')
    with z.open('zip_dir/test.txt') as f:
        print(f.read())
