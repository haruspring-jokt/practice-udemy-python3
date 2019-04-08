import unittest
from unittest.mock import MagicMock
import sec_14_mock.salary as salary
from unittest import mock


class TestSalary(unittest.TestCase):

    def test_calculation_salary(self):
        s = salary.Salary(year=2017)
        s.bonus_api.bonus_price = MagicMock(return_value=1)
        self.assertEqual(s.calculation_salary(), 101)
        s.bonus_api.bonus_price.assert_called()
        s.bonus_api.bonus_price.assert_called_once()
        s.bonus_api.bonus_price.assert_called_with(year=2017)
        self.assertEqual(s.bonus_api.bonus_price.call_count, 1)

    def test_calculation_salary_no_salary(self):
        s = salary.Salary(year=2050)
        s.bonus_api.bonus_price = MagicMock(return_value=1)
        self.assertEqual(s.calculation_salary(), 100)
        s.bonus_api.bonus_price.assert_not_called()

    @mock.patch('sec_14_mock.salary.ThirdPartyBonusRestApi.bonus_price')
    def test_calculation_salary_patch(self, mock_bonus):
        mock_bonus.return_value = 1

        s = salary.Salary(year=2017)
        salary_price = s.calculation_salary()

        self.assertEqual(salary_price, 101)
        mock_bonus.assert_called()

    def test_calculation_salary_patch_with(self):
        with mock.patch(
                'sec_14_mock.salary.ThirdPartyBonusRestApi.bonus_price') as mock_bonus:
            mock_bonus.return_value = 1

            s = salary.Salary(year=2017)
            salary_price = s.calculation_salary()

            self.assertEqual(salary_price, 101)
            mock_bonus.assert_called()

    def setUp(self):
        self.patcher = mock.patch('salary.ThirdPartyBonusRestApi.bonus_price')
        self.mock_bonus = self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    def test_calculation_salary_patch_pathcer(self):
        patcher = mock.patch('sec_14_mock.salary.ThirdPartyBonusRestApi.bonus_price')
        mock_bonus = patcher.start()
        mock_bonus.return_value = 1

        s = salary.Salary(year=2017)
        salary_price = s.calculation_salary()

        self.assertEqual(salary_price, 101)
        mock_bonus.assert_called()
        # patcher.stop()

    def test_calculation_salary_patch_side_effect(self):
        # def f(year):
        #     return 1

        self.mock_bonus.side_effect = lambda year: 1

        s = salary.Salary(year=2017)
        salary_price = s.calculation_salary()

        self.assertEqual(salary_price, 101)
        # self.mock_bonus.assert_called()
