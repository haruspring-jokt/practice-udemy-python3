def pytest_addoption(parser):
    parser.addoption('--os-name', default='linux', help='os name')

# conftestの記述方法
# テストファイルと同階層にこのファイル名で作成する
