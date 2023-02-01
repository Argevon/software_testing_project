import json
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

# Utworzenie zmiennej, ktora otwiera przegladarke Chrome
# przy uzyciu browserstack nie ma znaczenia co tu wpiszemy,
# bo rodzaj przegladarki bedzie podstawiony przez browserstack

driver = webdriver.Chrome()

##################################### TEST CASE 1 ########################################
# DODANIE NOWEJ RECENZJI DO LOSOWEJ RESTAURACJI #
# Wejscie na strone FriendlyEats
driver.get('https://airspace.com.pl/')
time.sleep(3)
# Sprawdzenie czy tytul zawiera 'FriendlyEats', czyli czy jestesmy na dobrej stronie www.
WebDriverWait(driver, 10).until(EC.title_contains('FriendlyEats'))
# Wejscie w zakladke z dana restauracja
WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
    (By.XPATH, '/html/body/div/main/div/div/div/div[2]/div/div[2]/h2'))).click()
# Zapisanie w zmiennej aktualnej liczby recenzji
before_rating_count = driver.find_elements(By.ID, 'review-card')
# Klikniecie przycisku + aby dodac restauracje
WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
    (By.XPATH, '/html/body/div/div[1]/div/header/div/div/div[2]/div/button/i'))).click()
# Klikniecie w ocene/gwiazdke recenzji
WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
    (By.XPATH, '/html/body/div/aside[2]/div[1]/section/div/i[1]'))).click()
# Zlokalizowanie pola tekstowego i dodanie tekstu recenzji
adding_review = driver.find_element(By.ID, 'text')
adding_review.send_keys('worst restaurant ever')
time.sleep(1)
# Klikniecie save
WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
    (By.XPATH, '/html/body/div/aside[2]/div[1]/footer/button[2]'))).click()
time.sleep(3)
# Zapisanie w zmiennej dodanej recenzji (powinna byc o 1 wieksza niz przed oczywiscie)
after_rating_count = driver.find_elements(By.ID, 'review-card')
# Sprawdzenie czy dodano recenzje poprawnie i wyswietlenie komunikatu
if len(before_rating_count) < len(after_rating_count):
    print("Recenzja dodana")
else:
    print("Nie udalo sie dodac recenzji")
# Powrot do strony glownej
WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
    (By.XPATH, '// *[ @ id = "close"]'))).click()
time.sleep(3)
# Zatrzymanie dzialania testu
driver.quit()

##################################### TEST CASE 2 ########################################
# SPRAWDZENIE DZIALANIA SORTOWANIA #
driver = webdriver.Chrome()
# Wejscie na strone FriendlyEats
driver.get('https://airspace.com.pl/')
# Sprawdzenie czy tytul zawiera 'FriendlyEats', czyli czy jestesmy na dobrej stronie www.
WebDriverWait(driver, 10).until(EC.title_contains('FriendlyEats'))
time.sleep(6)
# Wyszukanie na stronie slowa Pizza, po ktorym bedziemy filtrowac restauracje
pizza_places_before_sorting = driver.page_source.count('"category">Pizza</span>')
print(pizza_places_before_sorting)
# Klikniecie w przycisk sortowania
WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
    (By.XPATH, '/html/body/div/div[1]/div/header/div[2]/div/div/div/div/i'))).click()
time.sleep(1)
# Klikniecie w przycisk kategoria
WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
    (By.XPATH, '/html/body/div/aside[1]/div[1]/div[1]/section/div/ul/li[1]/span'))).click()
time.sleep(1)
# Klikniecie w przycisk Pizza
WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
    (By.XPATH, '/html/body/div/aside[1]/div[1]/div[2]/section/div/ul/li[11]'))).click()
time.sleep(1)
# Klikniecie w przycisk Accept
WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
    (By.XPATH, '/html/body/div/aside[1]/div[1]/div[1]/footer/button'))).click()
time.sleep(2)
# Sprawdzenie czy slowo pizza pojawia sie tyle samo razy na stronie co wczesniej
pizza_places_after_sorting = driver.page_source.count('"category">Pizza</span>')
if pizza_places_before_sorting == pizza_places_after_sorting:
    print('Sortowanie pomyslne dwa miejsca z pizza')
else:
    print('Blad cos poszlo nie tak')
driver.quit()

##################################### TEST CASE 3 ########################################
# SPRAWDZENIE SCROLLOWANIA STRONY #
driver = webdriver.Chrome()
# Wejscie na strone FriendlyEats
driver.get('https://airspace.com.pl/')
# Sprawdzenie czy tytul zawiera 'FriendlyEats', czyli czy jestesmy na dobrej stronie www.
WebDriverWait(driver, 10).until(EC.title_contains('FriendlyEats'))
time.sleep(3)
# Scrolowanie na sam dol strony
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(1)
# Scrolowanie na gore strony
driver.execute_script("window.scrollTo(document.body.scrollHeight, 0)")
time.sleep(1)
driver.quit()