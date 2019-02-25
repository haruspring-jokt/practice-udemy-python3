from setuptools import setup, find_packages

setup(
    name='python_programing_demo_app',
    version='0.0.2',
    packages=find_packages(),
    package_data={'roboter': ['templates/*.txt']},
    url='http:example.com',
    license='MIT',
    author='haruspring',
    author_email='hogefuga@example.com',
    install_requires=['termcolor==1.1.0'],
    description='roboter description',
    # テストフォルダーがあったらその中のテストを実行する
    test_suites='tests',
)
