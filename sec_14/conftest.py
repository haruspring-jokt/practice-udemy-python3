import os
import pytest


# 独自のfixtureを作成する
@pytest.fixture
def csv_file(tmpdir):
    # return 'csv file!!'
    # yieldを使用する：テストの前処理・後処理を簡略化
    # with open('test.csv', 'w+', encoding='utf-8') as c:
    # 既存のfixtureとも共存する
    with open(os.path.join(tmpdir, 'test.csv'), 'w+', encoding='utf-8') as c:
        print('before test')
        yield c
        print('after test')


def pytest_addoption(parser):
    parser.addoption('--os-name', default='linux', help='os name')

# conftestの記述方法
# テストファイルと同階層にこのファイル名で作成する
