import tarfile

# tar作成
with tarfile.open('test.tar.gz', 'w:gz') as tr:
    tr.add('tardir')

# tarオープン、確認
with tarfile.open('test.tar.gz', 'r:gz') as tr:
    # tr.extractall(path='test_tar')
    with tr.extractfile('tardir/subdir/sub_test.txt') as f:
        print(f.read())
