'''
DODANIA PRODUKTU DO KOSZYKA
'''

import re
from playwright.sync_api import sync_playwright , expect
from config.settings import BASE_URL, PRODUCT_URL


def test_add_product_to_cart_from_homepage():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto(BASE_URL)

        product_in_cart = page.locator("//td//a[text()='Blue Top']")

        # Test 1. Dodanie produktu do koszyka ze strony głównej
        page.locator("(//a[@data-product-id='1'])").first.click() # Klikamy w pierwszy przycisk "Add to cart"
        page.locator("(//u[text()='View Cart'])").click() # Klikamy w przycisk "View Cart"
        page.wait_for_timeout(2000)
        expect(product_in_cart).to_be_visible() # Produkt jest widoczny w koszyku
        print(f"Test 1: Produkt został dodany do koszyka ze strony głównej.")

        # Usunięcie produktu z koszyka
        print("Rozpoczynam usunięcie produktu z koszyka")

        # Test 2. Usunięcie produktu z koszyka
        page.locator("(//a[@class='cart_quantity_delete'])").click()
        page.wait_for_timeout(2000)
        expect(product_in_cart).not_to_be_visible() # Produkt nie jest już widoczny w koszyku
        print(f"Test 2: Produkt został usunięty z koszyka.")
        browser.close()

test_add_product_to_cart_from_homepage()

def test_add_product_to_cart_from_details():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto(PRODUCT_URL)

        product_in_cart = page.locator("//td//a[text()='Men Tshirt']")

        # Test 3. Dodanie produktu do koszyka z karty produktu
        page.locator("//button[contains(@class, 'cart')]").click()
        page.locator("//u[text()='View Cart']").click()
        page.wait_for_timeout(2000)
        expect(product_in_cart).to_be_visible()
        print(f"Test 3: Produkt został dodany do koszyka z karty produktu.")
        browser.close()

test_add_product_to_cart_from_details()