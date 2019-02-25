import unittest
from tests.unit.roboter.models import robot


class TestRobot(unittest.TestCase):

    def test_robot_init(self):
        r = robot.Robot(name='test_robot')
        self.assertEqual(r.name, 'test_robot')
