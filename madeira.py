from produto import Produto
import pandas as pd
import time
import random
from selenium.webdriver.common.by import By


def get_random():
    num2 = random.randint(1, 6)
    yield num2


class MadeiraMadeira(Produto):
    def hook_after(self):
        lista_urls = []
        data = pd.read_excel(r'/home/debian/Documentos/comparador/databases/madeirateste.xlsx')
        for i, row in data.iterrows():
         
            lista_urls.append(row[2])
        return lista_urls

       
    def get_produtos(self):
        urls = self.hook_after()
        for url in urls:
            self.driver.get(url)
            time.sleep(1)
                
            try:
                nomes = self.driver.find_elements(
                    By.XPATH, '/html/body/div[1]/div/main[1]/div[2]/div[2]/div[2]/div/div[2]/h1')[0].text
                print(nomes)
            except:
                pass
            
            try:
                precos = self.driver.find_elements(By.CSS_SELECTOR, 
                    '#control-box-content > div:nth-child(2) > div.cav--c-gkGAKm.cav--c-gkGAKm-ihkScrX-css > div:nth-child(2) > div > div.cav--c-lesPJm.cav--c-lesPJm-ifGHEql-css > div.cav--c-lesPJm.cav--c-bsUccK.cav--c-bsUccK-ilcUPDd-css > div > div.cav--c-gqwkJN.cav--c-gqwkJN-ikNResF-css > span')[0].text
                print(precos)
            except:
                pass

            try:
                imagens = self.driver.find_elements(By.XPATH,'//*[@id="control-box-content"]/div[2]/div[2]/div[1]/div/div/div[1]/div[2]/ul[1]/li[1]/a/div/img')
                for img in imagens:
                    print(img.get_attribute('href'))
            except:
                pass

    def compara_precos(self):
        for i in range(10):
            print("comparando preco Madeira")


