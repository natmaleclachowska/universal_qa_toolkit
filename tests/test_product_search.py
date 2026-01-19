'''
TESTY WYSZUKIWARKI WEWNĘTRZNEJ
'''

import re
import pytest
from playwright.sync_api import expect
from config.settings import BASE_URL

def test_search_button(page):
    page.goto(BASE1_URL)

    # Test 1. Wyszukiwanie z kliknięciem przycisku
    page.locator("//a[contains(text(), 'Products')]").click(force=True)
    page.wait_for_selector("//*[@id='search_product']", state="visible")
    search_bar = page.locator("//*[@id='search_product']")
    search_bar.fill("tshirt")
    page.locator("//*[@id='submit_search']").click()
    expect(page).to_have_url(re.compile(".*search.*"))
    count = page.locator("//div[contains(@class, 'productinfo')]").count()
    print(f"\nTest 1: Znaleziono {count} produktów.")

def test_search_no_results(page):
    page.goto(BASE1_URL)

    # Test 2. Wyszukiwanie frazy, która nie istnieje (negatywny)
    page.locator("//a[contains(text(), 'Products')]").click(force=True)
    page.wait_for_selector("//*[@id='search_product']", state="visible")
    page.locator("//*[@id='search_product']").fill("produkt_widmo_123")
    page.locator("//*[@id='submit_search']").click()
    expect(page).to_have_url(re.compile(".*search.*"))
    count = page.locator("//div[contains(@class, 'productinfo')]").count()
    print(f"\nTest 3: Znaleziono {count} produktów dla nieistniejącej frazy.")

def test_search_case_insensitive(page):
    page.goto(BASE1_URL)

    # Test 3. Wyszukiwanie z wielkimi literami (Case Insensitive)
    page.locator("//a[contains(text(), 'Products')]").click(force=True)
    page.wait_for_selector("//*[@id='search_product']", state="visible")
    page.locator("//*[@id='search_product']").fill("TSHIRT")
    page.locator("//*[@id='submit_search']").click()
    expect(page).to_have_url(re.compile(".*search.*"))
    count = page.locator("//div[contains(@class, 'productinfo')]").count()
    print(f"\nTest 4: Znaleziono {count} produktów dla zapytania TSHIRT.")