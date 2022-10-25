from pages.base_page import BasePage
from altunityrunner import By
from altunityrunner import AltUnityKeyCode

class GameplayPage(BasePage):

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
    def menu_button(self):
        return self.altdriver.wait_for_object(By.NAME, 'Canvas/Menu/Menu Button', timeout=2)

    @property
    def char_astronaut(self):
        return self.altdriver.wait_for_object(By.NAME, 'Player Minifig')

    def is_displayed(self):
        if self.char_astronaut:
            return True
    
    def press_start(self):
        self.start_button.click()
    
    def run_to_death(self):
    #    self.AltUnityDriver.press_key(key_code=AltUnityKeyCode.Tab, power=1, duration=10, wait=True)
        # self.altdriver.key_down(key_code=AltUnityKeyCode.Tab, power=1)
        self.altdriver.press_key(key_code=AltUnityKeyCode.Tab, power=1, duration=4, wait=True)
        # self.altunitydriver.pres_key(AltUnityKeyCode.Tab, power=1, duration=10)
        # self.altdriver.PressKey(AltUnityKeyCode.RightArrow, 0, 0)
        # self.altdriver.press_key(AltUnityKeyCode.RightArrow)