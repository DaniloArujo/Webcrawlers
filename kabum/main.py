# cabecalho padrão 
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# bibliotecas: bf4, selenium, webdriver, webdriver-manager, pandas, wheels, 

def main():
    
    lista_itens = []

    # abre o navegador com o selenium 
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(
        'https://www.kabum.com.br/')
    
    # procura a barra e pesquisa automaticamente
    time.sleep(10)
    input_place = driver.find_element(by=By.TAG_NAME, value='input')
    input_place.send_keys('cpu')
    input_place.submit()

    #procura e clica em um botão qualquer
    time.sleep(5)
    button01 = driver.find_element(by=By.CSS_SELECTOR, value= '#listingOrdenation > div.sc-grVGCS.cieVSf > button:nth-child(1)')
    button01.click()

    #tira uma especie de print do html
    page_content = driver.page_source
    site = BeautifulSoup(page_content,'html.parser')
    
    #procura pelo item
    item = site.find('div', attrs={'class':'sc-lkwKjF dAuLUu cardProdutoListagem'})
    
    for produto in item:

        
        titulo = produto.find('span', attrs={'class': 'sc-csvncw cFfAoy"'})
        preço = produto.find('span', attrs={'class': 'sc-dwLEzm bXwgF priceCard'})
        link = produto.find('a', attrs={'class': 'sc-jmNpzm kSnHxD"'})
        






    arquivo = pd.DataFrame(lista_itens,columns=['titulo', 'preço', 'link'])

    arquivo.to_csv('tabela.csv', index=False)

    print(arquivo)
    time.sleep(10)

main()