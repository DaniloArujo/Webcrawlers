from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pandas as pd 


#varaveis usadas no código

x = 1
contador = 1
links = []
tabela = []

contador_palavras = []
contador_PL = 0
contador_bolsonaro = 0
contador_lula = 0
contador_MDB = 0
contador_MDB_DF = 0
contador_Republicanos = 0
contador_Republicanos_DF = 0
contador_PSOL = 0
contador_PSOL_DF = 0
contador_REDE = 0
contador_REDE_DF = 0
contador_PT = 0
contador_PT_DF = 0











driver = webdriver.Chrome(ChromeDriverManager().install())



#abre um numero x de abas dentro do site
while(x < 2):
    div = 1
    driver.get(f"https://www.brasildefatodf.com.br/politica?pagina={contador}")

    time.sleep(5)

    #procura todas as noticas dentro do site e salva os respectivos links
    noticia_container = driver.find_elements(By.XPATH, '/html/body/main/section/div')

    for elem in noticia_container:
        link = driver.find_element(By.XPATH, f'/html/body/main/section/div[{div}]/a')
        varlink = link.get_attribute("href")
        varlink = varlink.replace("'","")

        links.append(varlink)

        div = div + 1
    contador = contador + 1 
    x = x + 1



# abre todos os links um a um
x = 1
contador = 0
for elem in links:
    try:
        driver.get(f"{links[contador]}")
        time.sleep(5)
        
        
        #procura dentro de cada link o titulo, subtitulo, autor e a data.

        titulo = driver.find_element(By.XPATH, f'/html/body/main/article/header/h1')
        subtitulo = driver.find_element(By.XPATH, f'/html/body/main/article/header/h2')
        autor = driver.find_element(By.XPATH, f'/html/body/main/article/header/div/div/div[1]')
        data = driver.find_element(By.XPATH, f'/html/body/main/article/header/div/div/div[2]/time')
        p1 = driver.find_element(By.XPATH, f'/html/body/main/article/div[2]/div/p[1]')
        p2 = driver.find_element(By.XPATH, f'/html/body/main/article/div[2]/div/p[2]')
        p3 = driver.find_element(By.XPATH, f'/html/body/main/article/div[2]/div/p[3]')
        p4 = driver.find_element(By.XPATH, f'/html/body/main/article/div[2]/div/p[4]')
        p5 = driver.find_element(By.XPATH, f'/html/body/main/article/div[2]/div/p[5]')
        p6 = driver.find_element(By.XPATH, f'/html/body/main/article/div[2]/div/p[6]')
        p7 = driver.find_element(By.XPATH, f'/html/body/main/article/div[2]/div/p[7]')
        p8 = driver.find_element(By.XPATH, f'/html/body/main/article/div[2]/div/p[8]')
        p9 = driver.find_element(By.XPATH, f'/html/body/main/article/div[2]/div/p[9]')
        p10 = driver.find_element(By.XPATH, f'/html/body/main/article/div[2]/div/p[10]')




        #edita as informações encontradas no HTML
        vartitulo = titulo.text
        vartitulo = vartitulo.replace(',',' ')

        varsubtitulo = subtitulo.text
        varsubtitulo = varsubtitulo.replace(',',' ')
        
        varautor = autor.text
        varautor = varautor.replace(',',' ')


        vardata = data.text
        vardata = vardata.replace(',',' ')
        
        varlink = links[contador]

        varp1 = p1.text
        varp1 = varp1.replace(',',' ')

        varp2 = p2.text
        varp2 = varp2.replace(',',' ')
        
        
        varp3 = p3.text
        varp3 = varp3.replace(',',' ')

        varp4 = p4.text
        varp4  = varp4.replace(',',' ')

        varp5 = p5.text
        varp5 = varp5.replace(',',' ')

        varp6 = p6.text
        varp6 = varp6.replace(',',' ')

        varp7 = p7.text
        varp7 = varp7.replace(',',' ')

        varp8 = p8.text
        varp8 = varp8.replace(',',' ')

        varp9 = p9.text
        varp9 = varp9.replace(',',' ')
        
        varp10 = p10.text
        varp10 = varp10.replace(',',' ')


        #salva tudo em um uma tabela
        tabela.append([vartitulo,varsubtitulo,varautor,vardata,varlink,varp1,varp2,varp3,varp4,varp5,varp6,varp7,varp8,varp9,varp10])


            #contador de ocorrencias
        #PL
        contador_PL +=  vartitulo.count("PL")
        contador_PL +=  varautor.count("PL")
        contador_PL +=  vardata.count("PL")
        contador_PL +=  varp1.count("PL")
        contador_PL +=  varp2.count("PL")
        contador_PL +=  varp3.count("PL")
        contador_PL +=  varp4.count("PL")
        contador_PL +=  varp5.count("PL")
        contador_PL +=  varp6.count("PL")
        contador_PL +=  varp7.count("PL")
        contador_PL +=  varp8.count("PL")
        contador_PL +=  varp9.count("PL")
        contador_PL +=  varp10.count("PL")


        #Bolsonaro
        contador_bolsonaro +=  vartitulo.count("Bolsonaro")
        contador_bolsonaro +=  varautor.count("Bolsonaro")
        contador_bolsonaro +=  vardata.count("Bolsonaro")
        contador_bolsonaro +=  varp1.count("Bolsonaro")
        contador_bolsonaro +=  varp2.count("Bolsonaro")
        contador_bolsonaro +=  varp3.count("Bolsonaro")
        contador_bolsonaro +=  varp4.count("Bolsonaro")
        contador_bolsonaro +=  varp5.count("Bolsonaro")
        contador_bolsonaro +=  varp6.count("Bolsonaro")
        contador_bolsonaro +=  varp7.count("Bolsonaro")
        contador_bolsonaro +=  varp8.count("Bolsonaro")
        contador_bolsonaro +=  varp9.count("Bolsonaro")
        contador_bolsonaro +=  varp10.count("Bolsonaro")
        
        #Lula
        contador_lula +=  vartitulo.count("Lula")
        contador_lula +=  varautor.count("Lula")
        contador_lula +=  vardata.count("Lula")
        contador_lula +=  varp1.count("Lula")
        contador_lula +=  varp2.count("Lula")
        contador_lula +=  varp3.count("Lula")
        contador_lula +=  varp4.count("Lula")
        contador_lula +=  varp5.count("Lula")
        contador_lula +=  varp6.count("Lula")
        contador_lula +=  varp7.count("Lula")
        contador_lula +=  varp8.count("Lula") 
        contador_lula +=  varp9.count("Lula") 
        contador_lula +=  varp10.count("Lula")       
        
        
        #MDB
        contador_MDB +=  vartitulo.count("MDB")
        contador_MDB +=  varautor.count("MDB")
        contador_MDB +=  vardata.count("MDB")
        contador_MDB +=  varp1.count("MDB")
        contador_MDB +=  varp2.count("MDB")
        contador_MDB +=  varp3.count("MDB")
        contador_MDB +=  varp4.count("MDB")
        contador_MDB +=  varp5.count("MDB")
        contador_MDB +=  varp6.count("MDB")
        contador_MDB +=  varp7.count("MDB")
        contador_MDB +=  varp8.count("MDB")
        contador_MDB +=  varp9.count("MDB")
        contador_MDB +=  varp10.count("MDB")

        #MDB_DF
        contador_MDB_DF +=  vartitulo.count("MDB-DF")
        contador_MDB_DF +=  varautor.count("MDB-DF")
        contador_MDB_DF +=  vardata.count("MDB-DF")
        contador_MDB_DF +=  varp1.count("MDB-DF")
        contador_MDB_DF +=  varp2.count("MDB-DF")
        contador_MDB_DF +=  varp3.count("MDB-DF")
        contador_MDB_DF +=  varp4.count("MDB-DF")
        contador_MDB_DF +=  varp5.count("MDB-DF")
        contador_MDB_DF +=  varp6.count("MDB-DF")
        contador_MDB_DF +=  varp7.count("MDB-DF")
        contador_MDB_DF +=  varp8.count("MDB-DF")
        contador_MDB_DF +=  varp9.count("MDB-DF")
        contador_MDB_DF +=  varp10.count("MDB-DF")

        #republicanos
        contador_Republicanos +=  vartitulo.count("Republicanos")
        contador_Republicanos +=  varautor.count("Republicanos")
        contador_Republicanos +=  vardata.count("Republicanos")
        contador_Republicanos +=  varp1.count("Republicanos")
        contador_Republicanos +=  varp2.count("Republicanos")
        contador_Republicanos +=  varp3.count("Republicanos")
        contador_Republicanos +=  varp4.count("Republicanos")
        contador_Republicanos +=  varp5.count("Republicanos")
        contador_Republicanos +=  varp6.count("Republicanos")
        contador_Republicanos +=  varp7.count("Republicanos")
        contador_Republicanos +=  varp8.count("Republicanos")
        contador_Republicanos +=  varp9.count("Republicanos")
        contador_Republicanos +=  varp10.count("Republicanos")

        #republicanos_df
        contador_Republicanos_DF +=  vartitulo.count("Republicanos-DF")
        contador_Republicanos_DF +=  varautor.count("Republicanos-DF")
        contador_Republicanos_DF +=  vardata.count("Republicanos-DF")
        contador_Republicanos_DF +=  varp1.count("Republicanos-DF")
        contador_Republicanos_DF +=  varp2.count("Republicanos-DF")
        contador_Republicanos_DF +=  varp3.count("Republicanos-DF")
        contador_Republicanos_DF +=  varp4.count("Republicanos-DF")
        contador_Republicanos_DF +=  varp5.count("Republicanos-DF")
        contador_Republicanos_DF +=  varp6.count("Republicanos-DF")
        contador_Republicanos_DF +=  varp7.count("Republicanos-DF")
        contador_Republicanos_DF +=  varp8.count("Republicanos-DF")
        contador_Republicanos_DF +=  varp9.count("Republicanos-DF")
        contador_Republicanos_DF +=  varp10.count("Republicanos-DF")

        #PSOL
        contador_PSOL_DF +=  vartitulo.count("PSOL")
        contador_PSOL_DF +=  varautor.count("PSOL")
        contador_PSOL_DF +=  vardata.count("PSOL")
        contador_PSOL_DF +=  varp1.count("PSOL")
        contador_PSOL_DF +=  varp2.count("PSOL")
        contador_PSOL_DF +=  varp3.count("PSOL")
        contador_PSOL_DF +=  varp4.count("PSOL")
        contador_PSOL_DF +=  varp5.count("PSOL")
        contador_PSOL_DF +=  varp6.count("PSOL")
        contador_PSOL_DF +=  varp7.count("PSOL")
        contador_PSOL_DF +=  varp8.count("PSOL")
        contador_PSOL_DF +=  varp9.count("PSOL")
        contador_PSOL_DF +=  varp10.count("PSOL")


        #PSOL_DF
        contador_PSOL_DF +=  vartitulo.count("PSOL-DF")
        contador_PSOL_DF +=  varautor.count("PSOL-DF")
        contador_PSOL_DF +=  vardata.count("PSOL-DF")
        contador_PSOL_DF +=  varp1.count("PSOL-DF")
        contador_PSOL_DF +=  varp2.count("PSOL-DF")
        contador_PSOL_DF +=  varp3.count("PSOL-DF")
        contador_PSOL_DF +=  varp4.count("PSOL-DF")
        contador_PSOL_DF +=  varp5.count("PSOL-DF")
        contador_PSOL_DF +=  varp6.count("PSOL-DF")
        contador_PSOL_DF +=  varp7.count("PSOL-DF")
        contador_PSOL_DF +=  varp8.count("PSOL-DF")
        contador_PSOL_DF +=  varp9.count("PSOL-DF")
        contador_PSOL_DF +=  varp10.count("PSOL-DF")


        #Rede
        contador_REDE +=  vartitulo.count("Rede")
        contador_REDE +=  varautor.count("Rede")
        contador_REDE +=  vardata.count("Rede")
        contador_REDE +=  varp1.count("Rede")
        contador_REDE +=  varp2.count("Rede")
        contador_REDE +=  varp3.count("Rede")
        contador_REDE +=  varp4.count("Rede")
        contador_REDE +=  varp5.count("Rede")
        contador_REDE +=  varp6.count("Rede")
        contador_REDE +=  varp7.count("Rede")
        contador_REDE +=  varp8.count("Rede")
        contador_REDE +=  varp9.count("Rede")
        contador_REDE +=  varp10.count("Rede")

        #PSOL
        contador_REDE_DF +=  vartitulo.count("Rede-DF")
        contador_REDE_DF +=  varautor.count("Rede-DF")
        contador_REDE_DF +=  vardata.count("Rede-DF")
        contador_REDE_DF +=  varp1.count("Rede-DF")
        contador_REDE_DF +=  varp2.count("Rede-DF")
        contador_REDE_DF +=  varp3.count("Rede-DF")
        contador_REDE_DF +=  varp4.count("Rede-DF")
        contador_REDE_DF +=  varp5.count("Rede-DF")
        contador_REDE_DF +=  varp6.count("Rede-DF")
        contador_REDE_DF +=  varp7.count("Rede-DF")
        contador_REDE_DF +=  varp8.count("Rede-DF")
        contador_REDE_DF +=  varp9.count("Rede-DF")
        contador_REDE_DF +=  varp10.count("Rede-DF")

        #PT
        contador_PT +=  vartitulo.count("PT")
        contador_PT +=  varautor.count("PT")
        contador_PT +=  vardata.count("PT")
        contador_PT +=  varp1.count("PT")
        contador_PT +=  varp2.count("PT")
        contador_PT +=  varp3.count("PT")
        contador_PT +=  varp4.count("PT")
        contador_PT +=  varp5.count("PT")
        contador_PT +=  varp6.count("PT")
        contador_PT +=  varp7.count("PT")
        contador_PT +=  varp8.count("PT")
        contador_PT +=  varp9.count("PT")
        contador_PT +=  varp10.count("PT")


        #PT-DF
        contador_PT_DF +=  vartitulo.count("PT-DF")
        contador_PT_DF +=  varautor.count("PT-DF")
        contador_PT_DF +=  vardata.count("PT-DF")
        contador_PT_DF +=  varp1.count("PT-DF")
        contador_PT_DF +=  varp2.count("PT-DF")
        contador_PT_DF +=  varp3.count("PT-DF")
        contador_PT_DF +=  varp4.count("PT-DF")
        contador_PT_DF +=  varp5.count("PT-DF")
        contador_PT_DF +=  varp6.count("PT-DF")
        contador_PT_DF +=  varp7.count("PT-DF")
        contador_PT_DF +=  varp8.count("PT-DF")
        contador_PT_DF +=  varp9.count("PT-DF")
        contador_PT_DF +=  varp10.count("PT-DF")

        print(f'PL: {contador_PL}')
        print(f'Bolsonaro: {contador_bolsonaro}')
        print(f'Lula: {contador_lula}')
        print(f'MDB: {contador_MDB}')
        print(f'MDB_DF: {contador_MDB_DF}')
        print(f'Republicanos: {contador_Republicanos}')
        print(f'Republicanos_DF: {contador_Republicanos_DF}')
        print(f'PSOL: {contador_PSOL}')
        print(f'PSOL_DF: {contador_PSOL_DF}')
        print(f'PT: {contador_PT}')
        print(f'PT_DF: {contador_PT_DF}')
        print('#####################################################')

    except:
        pass

    contador = contador + 1

#pega a tabela e transforma em um dataframe do pandas. depois Salva em .scv
arquivo = pd.DataFrame(tabela,columns=['titulo','subtitulo','autor','data','link','paragrafo_01','paragrafo_02','paragrafo_03','paragrafo_04','paragrafo_05','paragrafo_06','paragrafo_07','paragrafo_08','paragrafo_09','paragrafo_010'])
arquivo.to_csv(f'brasil_de_fato.csv', index=False)






contador_palavras.append([contador_PL,contador_bolsonaro,contador_lula,contador_MDB,contador_MDB_DF,contador_Republicanos,contador_Republicanos_DF,contador_PSOL,contador_PSOL_DF,contador_PT,contador_PT_DF])
Contador_palavras = pd.DataFrame(contador_palavras,columns=['contador_PL','contador_bolsonaro','contador_lula','contador_MDB','contador_MDB_DF','contador_Republicanos','contador_Republicanos_DF','contador_PSOL','contador_PSOL_DF','contador_PT','contador_PT_DF'])
Contador_palavras.to_csv(f'Brasildefato_contadorpalavras.csv', index=False)