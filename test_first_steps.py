import re # (narzedzie) Importujemy możliwość odczytywania URL przez wyrażenia regularne

from playwright.sync_api import sync_playwright, expect
# Idź do szafki playwright i szuflady sync_api (czyli testów synchronicznych)
# Import (wyjmij) sterownik (narzedzie) sync_playwright to sterowania przegladarka
# Po przeciku mamy sterownik (narzedzie) expect (do sprawdzenia asercji czyli tego czy test się udał)
# Bez tego Python nie wiedziałby, jak sterować przeglądarką.

import time # (narzedzie) Importujemy moduł czasu

def test_load_page():
# Definiujemy funkcje, czyli nazwe dla procesu ktory bedziemy chcieli wiele razy wykonac
# Zaczynamy od test, w () przekazujemy argumenty jesli do startu potrzebujemy jakis danych

    with sync_playwright() as p:
    # Menadzer kontekstu, dzieki niemu bezpiecznie otwieramy i obowiazkowo zamykamy przegladarke
    # with gwarantuje, że python poprawnie zamknie wszystkie procesy w tle
    # as p że narzedzie bedzie teraz dostepne jako p

        # Odpalenie przeglądarki i strony
        browser = p.chromium.launch(headless=False) # Otwieramy przeglądarkę, headless=False oznacza ze bedzie ona widoczna
        context = browser.new_context() # Tworzymy nowy kontekst (czysta sesja)
        page = context.new_page() # Otwieramy nową stronę
        page.goto("http://opencart.abstracta.us/") # Przechodzimy pod adres

        # Test 1 - Wyszukiwarki wewnetrznej
        page.locator("//input[@name='search']").fill("iPhone")
        page.locator("//input[@name='search']").press("Enter")
        expect(page).to_have_url(re.compile(".*iphone.*", re.IGNORECASE)) # Asercja, najpierw sprawdzamy URL (Twój główny cel analityczny)
        count = page.locator(".product-layout").count() # Jeśli URL jest OK, wykonujemy dodatkowe sprawdzenie zawartości
        print(f"Test zaliczony, adres URL jest poprawny. Znaleziono {count} produktów.")

        time.sleep(5) # Tu prosimy skrypt, żeby "poczekał" np. 5 s

        browser.close()

test_load_page()