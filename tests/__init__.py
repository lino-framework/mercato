from unipath import Path

from lino.utils.pythontest import TestCase
from lino_mercato import SETUP_INFO


class PackagesTests(TestCase):
    def test_01(self):
        self.run_packages_test(SETUP_INFO['packages'])


class DemoTests(TestCase):
    def test_demo(self):
        self.run_django_manage_test("lino_mercato/projects/mercato1")
