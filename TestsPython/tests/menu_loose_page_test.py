from tests.base_test import TestBase
from pages.menu_loose_page import MenuLoosePage


class TestMainMenuPage(TestBase):
    
    def setUp(self):
        self.menu_loose_page = MenuLoosePage(self.altdriver)
        self.menu_loose_page.load()

    def test_menu_loose_page_loaded_correctly(self):
        assert(self.menu_loose_page.is_displayed())
    
    def get_another_chance(self):
        self.menu_loose_page.try_again()
