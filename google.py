from produto import Produto
import pandas as pd
import time
import random
from selenium.webdriver.common.by import By

def get_random():
    num2 = random.randint(1, 6)
    yield num2

class GoogleShopping(Produto):

    def hook_after(self):
        listas = []
        data = pd.read_excel(r'/home/debian/Documentos/comparador/databases/googlehausz0506.xlsx')
        lista_urls = data['Urls'].to_list()
      
        for urls in lista_urls:
            listas.append(urls)

        return listas

    def get_produtos(self):
        lista_dicts = []
        urls = self.hook_after()
        for url in urls:
            produto_preco = {}
            self.driver.get(url)
            
            try:
                precos = self.driver.find_elements(By.XPATH, '//*[@id="sh-osd__online-sellers-cont"]/tr/td[4]/div/div[1]')
                for preco in precos:
                    print(preco.text)
                 
            except:
                pass
            
            try:
                sellers = self.driver.find_elements(By.XPATH,'//*[@id="sh-osd__online-sellers-cont"]/tr/td[1]/div[1]/a')
                for seller in sellers:
                    print(seller.text)
                    
            except:
                pass
            
            try:
                perfil = self.driver.find_elements(By.XPATH, '//*[@id="sh-osd__online-sellers-cont"]/tr/td[5]/div/a')
                for p in perfil:
                    print(p.get_attribute('href'))

            except:
                pass



    def compara_precos(self):
        for i in range(10):
            print("comparando preco google")

