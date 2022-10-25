from pages.base_page import BasePage
from altunityrunner import By 

class MenuLoosePage(BasePage):

    def __init__(self, altdriver):
        BasePage.__init__(self, altdriver)

    def load(self):
        self.altdriver.load_scene('Menu Lose')
    
    @property
    def menu_loose_title(self):
        return self.altdriver.wait_for_object(By.NAME, 'Canvas/Menu/Title')

    @property
    def play_again_button(self):
        return self.altdriver.wait_for_object(By.NAME,'Canvas/Menu/Play Button', timeout=2)

    @property
    def menu_button(self):
        return self.altdriver.wait_for_object(By.NAME, 'Canvas/Menu/Menu Button', timeout=2)

    def is_displayed(self):
        if self.play_again_button and self.menu_button and self.menu_loose_title:
            return True
    
    def try_again(self):
        self.play_again_button.click()