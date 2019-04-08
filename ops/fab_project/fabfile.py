# fabfileであるという前提があるのでimport *してもOKという思想があるとのこと
from fabric.api import *
from fabric.contrib.files import *
from db import checking
from fabric.colors import green, red

# envに設定を記述することでコマンド入力を省略する
env.hosts = ['root@172.16.200.101:22', 'root@172.16.200.102:22']
env.passwords = {
    'root@172.16.200.101:22': 'root',
    'root@172.16.200.102:22': 'root',
}
env.roledefs = {
    'web': ['root@172.16.200.101:22'],
    'db': ['root@172.16.200.102:22'],
}


# 引数に対応するroleに対してのみ実行する
@roles('web')
def host_type():
    run('uname -s')


@roles('db')
def host_files():
    run('ls -al')


# デコレータがない場合は`fab all_files`として実行
def all_files():
    run('ls -al')


# @taskを付けると、@taskを付けていないメソッドを実行しなくなる
@task
def go():
    all_files()
    # run('ls -al')


# `defalt=True`にすることでメソッド名を指定していなくても実行される
@task(default=True)
def who():
    run('whoami')


# @parallelによって同時にサーバへのコマンドを実行する
@task
@parallel(pool_size=2)
def para():
    run('ls -al')


@task
def argtest(arg1, arg2):
    print(arg1, arg2)


# returnすることでfabの実行結果を受け取ることができる
def test():
    return run('ls -al')


# returnにより受け取った実行結果を標準出力する
@task
def org():
    r = execute(test)
    print(r)


# 一度だけ実行する
@runs_once
def db_init():
    print('init')


@task
def deploy_db():
    db_init()


@task
def clean_and_upload():
    # localでfabを実行するローカル環境でコマンド実行できる
    local('ls -al')
    # ファイルをローカルからリモートにコピー
    put('fabfile.py', '/tmp/fabfile.py')
    # リモート環境のcdを指定
    with cd('/tmp'):
        run('pwd')
        run('ls -al')
        print(exists('/tmp/fabfile.py'))


@task
def split_test():
    # 分割したスクリプトの実行結果を受け取る
    r = execute(checking.check)
    print(r)
    # colorsを使うことでコンソールに色付き表示できる
    print(red('fail'))
    print(green('success'))
