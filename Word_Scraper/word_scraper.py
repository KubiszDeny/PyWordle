from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By

#Nastavení Driveru
options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-sll-errors')
options.add_argument('log-level=3') #Ignorovat výpis erorů

#DISABLE: Edge is being controlled by automated test software
options.add_argument("--disable-infobars")
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])

#options.add_argument('headless') #Bez Hlavičky
options.add_argument('--blink-settings=imagesEnabled=false') #Bez Obrázků
#options.add_argument("--no-first-run") 
#options.add_argument("--disable-default-apps") 
options.add_argument("--disable-extensions")

options.add_argument("--disable-javascript") #Vypnout JS 2
options.add_experimental_option( "prefs",{'profile.managed_default_content_settings.javascript': 2}) #Vypnout JS 1
options.add_argument("InPrivate")

driver = webdriver.Edge(options = options)
#Konec nastavení driveru

#Hlavní url: https://www.slovana.cz/hledat-slova/_____/
#Stránky url: https://www.slovana.cz/hledat-slova/_____/1/ 

driver.get('https://www.slovana.cz/hledat-slova/_____/')
file = open("slova.txt","a", encoding='utf-8')

def scrap_slova():
    slovo = 1
    while slovo <= 100:
        frm_slovo = driver.find_element(By.XPATH,'//*[@id="obsah2"]/div[2]/ul/li[{}]'.format(slovo))
        print(frm_slovo.text)      
        file.write(frm_slovo.text)
        file.write('\n')
        slovo += 1

def init_run():
    strana = 1
    while strana <= 278:
        frm_strana = 'https://www.slovana.cz/hledat-slova/_____/{}/.'.format(strana)
        print(frm_strana)
        driver.get(frm_strana)
        scrap_slova()
        strana += 1

init_run()
file.close()