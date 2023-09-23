import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.read_config import config_helper


class Test_read_config_data:
    def test_01_browserName(self):
        browserName = config_helper().read_confing('browser')
        assert browserName == 'chrome'

    def test_02_timeOutSecond(self):
        timeout = config_helper().read_confing('timeOutSeconds')
        assert timeout == 5
