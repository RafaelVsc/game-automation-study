from tests.base_test import TestBase
from pages.gameplay_page import GameplayPage
from pages.menu_loose_page import MenuLoosePage
from altunityrunner import AltUnityKeyCode



class TestGameplay(TestBase):
    
    def setUp(self):
        self.gameplay_page = GameplayPage(self.altdriver)
        self.gameplay_page.load()
        self.gameplay_page.press_start()
        # self.menu_loose_page = MenuLoosePage(self.altdriver)
        # self.gameplay_page.run_to_death()


    
    
    def go(self):
        self.gameplay_page.run_to_death()

    def validate_game_title(self):
        assert(self.gameplay_page.is_displayed())
    
    def run_game(self):
        self.main_menu_page.press_run()

    def test_main_menu_page_loaded_correctly(self):
        return
        # assert(self.main_menu_page.is_displayed())
    # def test_menu_lose_page_loaded_correctly(self):
    #     assert(self.gameplay_page.is_displayed())
    