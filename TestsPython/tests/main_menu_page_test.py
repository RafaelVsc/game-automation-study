from tests.base_test import TestBase
from pages.main_menu_page import MainMenuPage


class TestMainMenuPage(TestBase):
    
    def setUp(self):
        self.main_menu_page = MainMenuPage(self.altdriver)
        self.main_menu_page.load()

    def test_main_menu_page_loaded_correctly(self):
        assert(self.main_menu_page.is_displayed())
    
    def validate_game_title(self):
        self.main_menu_page.validade_text()
    
    def run_game(self):
        self.main_menu_page.press_run()
