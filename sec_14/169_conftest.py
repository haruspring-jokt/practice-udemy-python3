import os
import pytest
import sec_14.calculation as calculation


class TestCal(object):

    @classmethod
    def setup_class(cls):
        print('start')
        cls.cal = calculation.Cal()
        cls.test_dir = '/tmp/test_dir'
        cls.test_file_name = 'test.txt'

    def teardown_class(cls):
        import shutil
        # テスト終了後、ディレクトリ内をすべて削除
        if os.path.exists(cls.test_dir):
            shutil.rmtree(cls.test_dir)

    def test_save_no_dir(self):
        self.cal.save(self.test_dir, self.test_file_name)
        test_file_path = os.path.join(
            self.test_dir, self.test_file_name
        )
        assert os.path.exists(test_file_path) is True

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

    def test_add_num_and_double(self, csv_file):
        print(csv_file)
        assert self.cal.add_num_and_double(1, 1) == 4

    # tmpdirで一時的なディレクトリを作成
    def test_save(self, tmpdir):
        self.cal.save(tmpdir, self.test_file_name)
        test_file_path = os.path.join(
            tmpdir, self.test_file_name
        )
        assert os.path.exists(test_file_path) is True

    def test_add_num_and_double_raise(self):
        with pytest.raises(ValueError):
            self.cal.add_num_and_double('1', '1')
