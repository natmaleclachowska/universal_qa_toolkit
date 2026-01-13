'''
TESTY WYSZUKIWARKI WEWNĘTRZNEJ
'''

import re # Importujemy mozliwosc odczytywania URL przez wyrażenia regularne
from playwright.sync_api import sync_playwright , expect # Idź do testów synchronicznych playwright i zaimportuj sterownik do sterowania przegladarki sync_playwright i expect do sprawdzania asercji
from config.settings import BASE_URL # Laczymy plik testu z plikiem config # Idz do folderu config i pliku settings i zaimportuj zmienną
import time # Importujemy modul czasu

def test_search_button(): # Definiujemy funkcje, czyli nazwe dla procesu ktory bedziemy chcieli wiele razy wykonac, w () nie ma argumentow wejsciowych
    with sync_playwright() as p: # Menadzer kontekstu, dzieki niemu bezpiecznie otwieramy i obowiazkowo zamykamy przegladarke, dostepne dalej jako p
        browser = p.chromium.launch(headless=False) # Otwieramy przegladarke, ktora bedzie widoczna (False)
        context = browser.new_context() # Otwieramy sesje
        page = context.new_page() # Otwieramy strone
        page.goto(BASE_URL) # Wpisujemy URL

        # Test 1. Wyszukiwanie z kliknieciem przycisku
        page.locator("//a[contains(text(), 'Products')]").click(force=True) # Klikamy w podstrone
        page.wait_for_selector("//*[@id='search_product']", state="visible")
        search_bar = page.locator("//*[@id='search_product']") # Klikamy na wyszukiwarke
        search_bar.fill("tshirt") # Wpisujemy slowo
        page.locator("//*[@id='submit_search']").click() # Klikamy w przycisk
        page.wait_for_timeout(2000) # Czekamy na załadowanie wyników

        expect(page).to_have_url(re.compile(".*search.*")) # Asercja czy URL ma slowo search
        count = page.locator("//div[contains(@class, 'productinfo')]").count() # Liczymy ile produktow wyswietli sie w wynikach wyszukiwania
        print(f"Test 1: Znaleziono {count} produktów.") # W konsoli wyswietla sie komunikat: Znaleziono X produktów.
        browser.close() # Zamykamy przegladarke

test_search_button() # Koniec funkcji

'''
NOTATKA: Test 2 obecnie nie przechodzi, ponieważ strona 
automationexercise.com nie obsługuje wysyłania formularza klawiszem Enter. 
Wymagane jest kliknięcie w lupę (Test 1).
'''

# def test_search_enter():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         context = browser.new_context()
#         page = context.new_page()
#         page.goto(BASE_URL) # Wpisujemy URL
#
#         # Test 2. Wyszukiwanie z kliknieciem enter
#         page.locator("//a[contains(text(), 'Products')]").click(force=True)
#         page.wait_for_selector("//*[@id='search_product']", state="visible")
#         search_bar = page.locator("//*[@id='search_product']")
#         search_bar.fill("tshirt")
#         search_bar.press("Enter") # Naciskamy enter
#         page.wait_for_timeout(2000)
#
#         expect(page).to_have_url(re.compile(".*search.*"))
#         print("Test z 'Enter' przeszedł pomyślnie")
#         browser.close()
#
# test_search_enter()

def test_search_no_results():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto(BASE_URL)

        # Test 3. Wyszukiwanie z fraza ktora nie istnieje
        page.locator("//a[contains(text(), 'Products')]").click(force=True)
        page.wait_for_selector("//*[@id='search_product']", state="visible")
        page.locator("//*[@id='search_product']").fill("produkt_widmo_123")
        page.locator("//*[@id='submit_search']").click()
        page.wait_for_timeout(2000)

        expect(page).to_have_url(re.compile(".*search.*"))
        count = page.locator("//div[contains(@class, 'productinfo')]").count()
        print(f"Test 3 (negatywny): Znaleziono {count} produktów dla nieistniejącej frazy.")
        browser.close()

test_search_no_results()

def test_search_case_insensitive():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto(BASE_URL)

        # Test 4. Wyszukiwanie z fraza pisana z duzych liter
        page.locator("//a[contains(text(), 'Products')]").click(force=True)
        page.wait_for_selector("//*[@id='search_product']", state="visible")
        search_bar = page.locator("//*[@id='search_product']")
        search_bar.fill("TSHIRT")
        page.locator("//*[@id='submit_search']").click()
        page.wait_for_timeout(2000)

        expect(page).to_have_url(re.compile(".*search.*"))
        count = page.locator("//div[contains(@class, 'productinfo')]").count()
        print(f"Test 4 (Case Insensitive): Znaleziono {count} produktów.")
        browser.close()

test_search_case_insensitive()