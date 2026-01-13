# Testy wyszukiwarki wewnętrznej na podstronie produktowej

import re # Importujemy mozliwosc odczytywania URL przez wyrażenia regularne
from playwright.sync_api import sync_playwright , expect # Idź do testów synchronicznych playwright i zaimportuj sterownik do sterowania przegladarki sync_playwright i expect do sprawdzania asercji
from config.settings import BASE_URL # Laczymy plik testu z plikiem config # Idz do folderu config i pliku settings i zaimportuj zmienną
import time # Importujemy modul czasu

def test_search_product(): # Definiujemy funkcje, czyli nazwe dla procesu ktory bedziemy chcieli wiele razy wykonac, w () nie ma argumentow wejsciowych
    with sync_playwright() as p: # Menadzer kontekstu, dzieki niemu bezpiecznie otwieramy i obowiazkowo zamykamy przegladarke, dostepne dalej jako p
        browser = p.chromium.launch(headless=False) # Otwieramy przegladarke, ktora bedzie widoczna (False)
        context = browser.new_context() # Otwieramy sesje
        page = context.new_page() # Otwieramy strone
        page.goto(BASE_URL) # Wpisujemy URL

        # Test 1.
        page.locator("//a[contains(text(), 'Products')]").click() # Klikamy w sekcje w menu
        page.wait_for_url("**/products") # Czekamy na wczytania sie podstrony
        search_bar = page.locator("//*[@id='search_product']") # Klikamy na wyszukiwarke
        search_bar.fill("tshirt") # Wpisujemy slowo
        page.locator("//*[@id='submit_search']").click() # Klikamy w przycisk

        expect(page).to_have_url(re.compile(".*search.*")) # Asercja czy URL ma slowo search
        count = page.locator(".productinfo").count() # Liczymy ile produktow wyswietli sie w wynikach wyszukiwania
        print(f"Znaleziono {count} produktów.") # W konsoli wyswietla sie: Znaleziono X produktów.

        time.sleep(10) # Prosimy skrypt, żeby "poczekał" np. 10 s

        browser.close() # Zamykamy przegladarke

test_search_product() # Koniec funkcji