import subprocess

# subprocess.run('dir', shell=True)
# Windowsでshell=Trueを付けると，実際にはコマンドプロンプト cmd.exe
# が呼び出されて，その上でコマンドが実行される
# subprocess.run(['dir', '/a'], shell=True)

# UNIXでの使用例
# subprocess.run(['ls', '-al', '|', 'grep', 'hoge'])
# cmd = 'ls -al | rm -rf'
# subprocess.run(cmd, shell=True)

# 実行結果のチェック（UNIX）
# r = subprocess.run('ls', shell=True, check=True)

# PowerShellを呼ぶ
subprocess.run("powershell.exe -Command ls")
