'''
TESTY DODAWANIA PRODUKTU DO KOSZYKA
'''

import pytest
from playwright.sync_api import expect
from config.settings import BASE1_URL, PRODUCT1_URL

def test_add_and_remove_product_from_homepage(page):
    page.goto(BASE1_URL)
    product_in_cart = page.locator("//td//a[text()='Blue Top']")

    # Test 1. Dodanie produktu do koszyka ze strony głównej
    page.locator("(//a[@data-product-id='1'])").first.click()
    page.locator("(//u[text()='View Cart'])").click()
    expect(product_in_cart).to_be_visible()

    # Test 2. Usunięcie produktu z koszyka
    page.locator("(//a[@class='cart_quantity_delete'])").click()
    expect(product_in_cart).not_to_be_visible()

def test_add_product_to_cart_from_details(page):
    page.goto(PRODUCT1_URL)
    product_in_cart = page.locator("//td//a[text()='Men Tshirt']")

    # Test 3. Dodanie produktu do koszyka z karty produktu
    page.locator("//button[contains(@class, 'cart')]").click()
    page.locator("//u[text()='View Cart']").click()
    expect(product_in_cart).to_be_visible()