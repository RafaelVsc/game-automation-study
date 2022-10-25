from pages.base_page import BasePage
from altunityrunner import By 

class MainMenuPage(BasePage):

    def __init__(self, altdriver):
        BasePage.__init__(self, altdriver)

    def load(self):
        self.altdriver.load_scene('Menu Intro')

    @property
    def menu_title(self):
        return self.altdriver.wait_for_object(By.NAME, 'Canvas/Menu/Title')

    @property
    def start_button(self):
        return self.altdriver.wait_for_object(By.NAME,'Canvas/Menu/Play Button', timeout=2)

    @property
    def controls_button(self):
        return self.altdriver.wait_for_object(By.NAME, 'Canvas/Menu/Controls Button', timeout=2)

    def is_displayed(self):
        if self.start_button and self.controls_button and self.menu_title:
            return True

    def press_run(self):
        self.start_button.click()