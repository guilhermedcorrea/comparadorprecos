from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd



from abc import ABC, abstractmethod



class Produto(ABC):

    options = webdriver.ChromeOptions() 
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--start-maximized")
    options.add_argument('--disable-infobars')
    driver = webdriver.Chrome(options=options, executable_path=r'/home/debian/Documentos/comparador/chromedriver/chromedriver')
    def call_func(self) -> None:
        self.get()
        self.get_produtos()
        self.compara_precos()

    def hook_after(self)-> None: pass

    def hook_before(self) -> None: pass

    def get(self) -> None: pass

    @abstractmethod
    def get_produtos(self) -> None: pass

    @abstractmethod
    def compara_precos(self) -> None: pass




