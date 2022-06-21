import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_itens = []


url_base = "https://lista.mercadolivre.com.br/"

produto_nome = input("Qual é o produto que você deseja ? ")

response = requests.get(url_base + produto_nome)

site = BeautifulSoup(response.text, 'html.parser')

produtos = site.findAll('div', attrs={'class': 'andes-card andes-card--flat andes-card--default ui-search-result ui-search-result--core andes-card--padding-default'})


for produto in produtos:

    titulo = produto.find('h2', attrs={'class': 'ui-search-item__title'})
    link = produto.find('a', attrs={'class': 'ui-search-link'})
    price = produto.find('span', attrs={'class': 'price-tag-fraction'})

    #print('Título do produto:', titulo.text)
    #print('link do produto: ', link['href'])
    #print('preço do produto: R$', real.text)
    
    lista_itens.append([titulo.text, price.text ,link['href']])

arquivo = pd.DataFrame(lista_itens,columns=['produto', 'preço', 'link'])

arquivo.to_csv('tabela.csv', index=False)

print(arquivo)

