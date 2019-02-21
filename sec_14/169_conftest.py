import os
import pytest
import sec_14.calculation as calculation


class TestCal(object):

    @classmethod
    def setup_class(cls):
        print('start')
        cls.cal = calculation.Cal()
        cls.test_file_name = 'test.txt'

    # requestにオプションの変数が入る
    def test_add_num_and_double(self, request):
        # オプションの内容を取得
        os_name = request.config.getoption('--os-name')
        # os_name = 'mac'
        print(os_name)
        if os_name == 'mac':
            print('ls')
        elif os_name == 'windows':
            print('dir')
        assert self.cal.add_num_and_double(1, 1) == 4

    # tmpdirで一時的なディレクトリを作成
    def test_save(self, tmpdir):
        self.cal.save(tmpdir, self.test_file_name)
        test_file_path = os.path.join(
            tmpdir, self.test_file_name
        )
        assert os.path.exists(test_file_path) is True
