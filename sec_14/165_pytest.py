import sec_14.calculation as calculation
import pytest

# pytestの場合はtest_で始まるメソッドはテストとして認識する
def test_add_num_and_double():
    cal = calculation.Cal()
    # assert文がテストケースとして機能する
    assert cal.add_num_and_double(1, 1) == 4

# テストクラスを作成し、その中でテストケースを書くことも可能
class TestCal(object):
    def test_add_num_and_double(self):
        cal = calculation.Cal()
        # assert文がテストケースとして機能する
        assert cal.add_num_and_double(1, 1) == 4

    # 例外のpytest
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
