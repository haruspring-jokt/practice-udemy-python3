import tempfile

with tempfile.TemporaryFile(mode='w+') as t:
    t.write('hello')
    t.seek(0) # ファイルオブジェクトの位置を移動（readを使うために最初に戻る）
    print(t.read())

with tempfile.NamedTemporaryFile(delete=False) as t:
    print(t.name)
    with open(t.name, 'w+') as f:
        f.write('test\n')
        f.seek(0)
        print(f.read())

with tempfile.TemporaryFile() as td:
    print(td)

temp_dir = tempfile.mkdtemp()
print(temp_dir)