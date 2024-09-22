import pytest
from tests.web.test_base import WebBase
from tests.web.pages.login_page import LoginPage

class TestWeb(WebBase):

    def test_login(self):
        LoginPage(self.driver).page_elements['username'].set('admin')
