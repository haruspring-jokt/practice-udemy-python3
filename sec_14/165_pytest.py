import sec_14.calculation as calculation
import pytest

# pytestの場合はtest_で始まるメソッドはテストとして認識する
# def test_add_num_and_double():
#     cal = calculation.Cal()
#     # assert文がテストケースとして機能する
#     assert cal.add_num_and_double(1, 1) == 4

is_release = True


# テストクラスを作成し、その中でテストケースを書くことも可能
class TestCal(object):

    # クラスに対するsetup
    @classmethod
    def setup_class(cls):
        print('start')
        cls.cal = calculation.Cal()

    # クラスに対するteardown
    @classmethod
    def teardown_class(cls):
        print('end')
        del cls.cal

    # テストメソッド開始前
    # methodを引数に追加し利用できる
    def setup_method(self, method):
        print(f'method={method.__name__}')

    # テストメソッド終了後
    def teardown_method(self, method):
        print(f'method={method.__name__}')

    # pytest
    def test_add_num_and_double(self):
        cal = calculation.Cal()
        # assert文がテストケースとして機能する
        assert cal.add_num_and_double(1, 1) == 4

    # 例外のpytest
    # @pytest.mark.skip(reason='hogehoge') # skip
    @pytest.mark.skipif(is_release is True,
                        reason='is_release')  # 条件付きskip
    def test_add_num_and_double_raise(self):
        # pytest.raises(Error)を使用する
        with pytest.raises(ValueError):
            cal = calculation.Cal()
            cal.add_num_and_double('1', '1')

# release_name = 'lesson'
#
#
# class CalTest(unittest.TestCase):
#     # テスト開始前
#     def setUp(self):
#         print('setup')
#         self.cal = calculation.Cal()
#
#     # テスト終了後
#     def tearDown(self):
#         print('clean up')
#         del self.cal
#
#     # 必ずskip
#     # @unittest.skip('reason of skipping')
#     # 条件次第でskip
#     @unittest.skipIf(release_name == 'lesson', 'skip!')
#     def test_add_num_and_double(self):
#         # cal = calculation.Cal()
#         self.assertEqual(self.cal.add_num_and_double(1, 1), 4)
#
#     # 例外が起こることを確認する
#     def test_add_num_and_double_raise(self):
#         # cal = calculation.Cal()
#         with self.assertRaises(ValueError):
#             self.cal.add_num_and_double('1', '1')


# if __name__ == '__main__':
#     unittest.main()
