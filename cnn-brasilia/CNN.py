from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pandas as pd



contador = 1
tabelalinks = []
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


for i in range(2):
    driver.get(f"https://www.cnnbrasil.com.br/politica/ultimas-noticias/pagina/{contador}/")
    time.sleep(2)

    container = driver.find_elements(By.CLASS_NAME, 'home__list__tag')

    for elem in container:
        link = elem.get_attribute("href")
        if(link):
            tabelalinks.append(link)
    contador += 1 

contador = 0
for elem in tabelalinks:
    

    driver.get(f'{tabelalinks[contador]}')
    time.sleep(2)
    try:
        varlink = (tabelalinks[contador])

        titulo = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/main/article/header/h1')
        vartitulo = titulo.text
        vartitulo = vartitulo.replace(",","")
        print(vartitulo)
        
        subtitulo = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/main/article/header/p')
        varsubtitulo = subtitulo.text
        varsubtitulo = varsubtitulo.replace(",","")
        print(varsubtitulo)
        
        autor = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/main/article/header/section/figure/figcaption/p[1]/span/span[1]/a')
        varautor = autor.text
        varautor = varautor.replace(",","")
        print(varautor)
    
        data = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/main/article/header/div/span')
        vardata = data.text
        vardata = vardata.replace(",","")
        print(vardata)
        
        p1 = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/main/article/div/p[1]')
        varp1 = p1.text
        varp1 = varp1.replace(",","")
        print(varp1)

        p2 = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/main/article/div/p[2]')
        if(p2):
            varp2 = p2.text
            varp2 = varp2.replace(",","")
            print(varp2)
        else:
            varp2 = ''

        p3 = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/main/article/div/p[3]')
        if(p3):
            varp3 = p3.text
            varp3 = varp3.replace(",","")
            print(varp3)
        else:
            varp3 = ''
            
        p4 = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/main/article/div/p[4]')
        if(p4):
            varp4 = p4.text
            varp4 = varp4.replace(",","")
            print(varp4)
        else:
            varp4 = ''

        p5 = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/main/article/div/p[5]')
        if(p5):
            varp5 = p5.text
            varp5 = varp5.replace(",","")
            print(varp5)
        else:
            varp5 = ''
        
        p6 = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/main/article/div/p[6]')
        if(p6):
            varp6 = p6.text
            varp6 = varp6.replace(",","")
            print(varp6)
        else:
            varp6 = ''

        p7 = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/main/article/div/p[7]')
        if(p7):
            varp7 = p7.text
            varp7 = varp7.replace(",","")
            print(varp7)
        else:
            varp7 = ''
        

        tabela.append([varlink,varautor,vardata,vartitulo,varsubtitulo,varp1,varp2,varp3,varp4,varp5,varp6,varp7])





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





        print('###########################################################################')
    except:
        pass





    
    contador +=1

arquivo = pd.DataFrame(tabela,columns=['link','autor','data_publicação','titulo','subtitulo','paragrafo_01','paragrafo_02','paragrafo_03','paragrafo_04','paragrafo_05','paragrafo_06','paragrafo_07'])
arquivo.to_csv(f'CNN.csv', index=False)

contador_palavras.append([contador_PL,contador_bolsonaro,contador_lula,contador_MDB,contador_MDB_DF,contador_Republicanos,contador_Republicanos_DF,contador_PSOL,contador_PSOL_DF,contador_PT,contador_PT_DF])
Contador_palavras = pd.DataFrame(contador_palavras,columns=['contador_PL','contador_bolsonaro','contador_lula','contador_MDB','contador_MDB_DF','contador_Republicanos','contador_Republicanos_DF','contador_PSOL','contador_PSOL_DF','contador_PT','contador_PT_DF'])
Contador_palavras.to_csv(f'CNN_Contador_palavras.csv', index=False)